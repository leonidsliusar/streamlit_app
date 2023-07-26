import uuid
from typing import Optional

import requests
from github import Github, Auth
from github.Repository import Repository

gh_org = 'elenabiterman'
gh_token = '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'


class GitHubManager:
    _commit_message: str = "add page.txt"

    __slots__ = ('_html', '_repo_name', '_token', '_client', '_org', '_repo')

    def __init__(self, html_code: str):
        self._html: str = html_code
        self._repo_name: str = str(uuid.uuid4())
        self._token: str = gh_token
        self._client: Github = Github(auth=Auth.Token(self._token))
        self._org = self._client.get_organization(gh_org)
        self._repo: Optional[Repository] = None

    @property
    def get_link(self) -> str:
        self.repo = self._repo_name
        self._push_to_gh()
        link = self._enable_github_pages
        return link

    @property
    def repo(self) -> Repository:
        return self._repo

    @repo.setter
    def repo(self, repo_name) -> None:
        self._repo = self._org.create_repo(name=repo_name)

    def _push_to_gh(self) -> None:
        self.repo.create_file(path='index.html', message=self._commit_message, content=self._html)

    @property
    def _enable_github_pages(self) -> str:
        url = f'https://api.github.com/repos/{self._org.login}/{self._repo_name}/pages'
        headers = {"Authorization": f"Bearer {self._token}"}
        data = {"source": {"branch": "main", "path": "/"}}
        response = requests.post(url, headers=headers, json=data)
        page_link = response.json()
        page_link = page_link.get('html_url')
        return page_link
