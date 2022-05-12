#!/bin/env python3
import os
import sys

from github import Github


def run():
    token = os.environ['GITHUB_TOKEN']
    gh = Github(token)

    repository = gh.get_user().get_repo(repo)
    body = '''
    APP_NAME=HowToLiveLonger
    APP_URL=http://sucicada.cf/HowToLiveLonger/
    APP_ICON=https://user-images.githubusercontent.com/33519267/167297958-2bc084d2-e9f1-4dd5-a167-64904cab4ef9.png
    '''
    print(repository)

    match sys.argv[1]:
        case "create":
            res = repository.create_issue(
                title="test_app",
                body=body,
                labels=['build']
            )
            print(res)
        case "close":
            issues = repository.get_issues(
                state='open',
                labels=['build']
            )
            for issue in issues:
                print("close", issue)
                issue.edit(state='close')


# repo = "Auto-Convert-Website-to-Android-With-GitHub-Action"
repo = "test-github-action"

if len(sys.argv) > 1:
    run()
else:
    print("create / close")
