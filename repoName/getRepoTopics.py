from github import Github
from github.Repository import Repository

g = Github("Suba122", "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")

repo: Repository = g.get_repo("PyGithub/PyGithub")
contents = repo.get_contents("apiKey.txt", ref="test")
repo.update_file(contents.path, "more tests", "more tests", contents.sha, branch="test")
