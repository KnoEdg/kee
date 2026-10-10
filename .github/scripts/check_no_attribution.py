#!/usr/bin/env python3
"""CI check: fail a pull request or push that carries agent attribution (GitHub Actions entry point).

Uses attr_check.py (same directory). On a pull_request event it checks the PR title, body and head branch name and every
commit in base..head (message, author, committer); on a push it checks the branch or tag name and the commits the push
adds; with --all it checks every commit reachable from any branch or tag (a one-off audit). Prints GitHub error
annotations and exits 1 on any problem. Reads GITHUB_EVENT_NAME / GITHUB_EVENT_PATH; no network, no token.
"""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import attr_check as ac  # noqa: E402

ZERO = '0' * 40
FMT = '%H%x1f%an <%ae>%x1f%cn <%ce>%x1f%B%x1e'


def log(*rev):
    r = subprocess.run(['git', 'log', '--format=' + FMT, *rev], capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit('git log %s failed: %s' % (' '.join(rev), r.stderr.strip()))
    return ac.parse_log(r.stdout)


def commit_exists(sha):
    return subprocess.run(['git', 'cat-file', '-e', sha + '^{commit}'], capture_output=True).returncode == 0


def new_commits(after, branch):
    """Commits at `after` that no other branch on the remote has. In CI the checkout also fetches the pushed branch itself
    (refs/remotes/origin/<branch>), so that one ref is left out, or a new branch would always scan as empty."""
    r = subprocess.run(['git', 'for-each-ref', '--format=%(refname) %(objectname)', 'refs/remotes/'],
                       capture_output=True, text=True)
    others = []
    for line in r.stdout.splitlines():
        name, sha = line.split()
        if name.endswith('/HEAD') or (branch and name.split('/', 3)[-1] == branch):
            continue
        others.append(sha)
    return log(after, '--not', *others) if others else log(after)


def main(argv):
    problems = []
    if '--all' in argv:
        recs = log('--branches', '--tags')
    else:
        event = os.environ.get('GITHUB_EVENT_NAME', '')
        path = os.environ.get('GITHUB_EVENT_PATH', '')
        payload = json.load(open(path)) if path and os.path.exists(path) else {}
        if event == 'pull_request':
            pr = payload['pull_request']
            for where, text in (('PR title', pr.get('title') or ''), ('PR body', pr.get('body') or '')):
                problems += ['%s: %s' % (where, p) for p in ac.message_problems(text)]
            p = ac.ref_problem(pr['head']['ref'])
            if p:
                problems.append('PR head branch: ' + p)
            recs = log(pr['base']['sha'] + '..' + pr['head']['sha'])
        elif event == 'push':
            ref = payload.get('ref') or os.environ.get('GITHUB_REF', '')
            p = ac.ref_problem(ref)
            if p:
                problems.append('pushed ' + p)
            before, after = payload.get('before', ZERO), payload.get('after') or 'HEAD'
            branch = ref[len('refs/heads/'):] if ref.startswith('refs/heads/') else None
            if payload.get('deleted'):
                recs = []
            elif before == ZERO or not commit_exists(before):    # new branch, or a force-push that dropped `before`
                recs = new_commits(after, branch)
            else:
                recs = log(before + '..' + after)
        else:
            print('no pull_request or push event: nothing to check (use --all for an audit)')
            return 0
    for sha, probs in ac.commit_problems(recs):
        problems += ['commit %s: %s' % (sha[:10], p) for p in probs]
    for p in problems:
        print('::error::' + p)
    if problems:
        print('%d problem(s). Rule: no agent attribution, no agent-named branches (see docs/conventions/attribution-guard.md in meta-knoedg).' % len(problems))
        return 1
    print('no agent attribution found in %d commit(s)' % len(recs))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
