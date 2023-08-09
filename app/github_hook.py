import os
from typing import Optional
import requests
from github import Github, Auth
from github.Repository import Repository
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
gh_org = os.getenv("GH_ORG")
gh_token = os.getenv("GH_TOKEN")
if not gh_org:
    gh_org = st.secrets.get("gh_org")
if not gh_token:
    gh_token = st.secrets.get("gh_token")


class GitHubManager:
    _commit_message: str = "add page.txt"

    __slots__ = ('_html', '_repo_name', '_token', '_client', '_org', '_repo')

    def __init__(self, html_code: str = None, obj_num: str = None):
        self._html: Optional[str] = html_code
        self._repo_name: str = obj_num
        self._token: str = gh_token
        self._client: Github = Github(auth=Auth.Token(self._token))
        self._org = self._client.get_organization(gh_org)
        self._repo: Optional[Repository] = None

    @property
    def get_link(self) -> str:
        print(self._token)
        self.repo = self._repo_name
        self._push_to_gh()
        link = self._enable_github_pages
        return link

    def delete_repo(self, repo_name) -> None:
        self._repo_name = repo_name
        repo = self._org.get_repo(repo_name)
        repo.delete()

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
