import datetime
from typing import List, Iterable

from jsonpickle.handlers import DatetimeHandler

from .internal.base import Base
from .project import Project
from .repository import Repository


@DatetimeHandler.handles
class User(Base):
    def __init__(self, id: int = 0, uuid: str = "", login: str = "",
                 created_at: datetime.datetime = datetime.datetime.now(),
                 updated_at: datetime.datetime = datetime.datetime.now(),
                 name: str = "", subscribed_repos: List[Repository] = None,
                 subscribed_projects: List[Project] = None, owned_projects: List[Project] = None,
                 owned_repos: List[Repository] = None, contributed_projects: List[Project] = None,
                 contributed_repositories: List[Repository] = None, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.id = id
        self.uuid = uuid
        self.login = login
        self.created_at = created_at
        self.updated_at = updated_at
        self._subscribed_projects = [] if subscribed_projects is None else subscribed_projects
        self._subscribed_repos = [] if subscribed_repos is None else subscribed_repos
        self._owned_projects = [] if owned_projects is None else owned_projects
        self._owned_repos = [] if owned_repos is None else owned_repos
        self._contributed_projects = [] if contributed_projects is None else contributed_projects
        self._contributed_repositories = [] if contributed_repositories is None else contributed_repositories

    @property
    def subscribed_projects(self) -> List[Project]:
        return self._subscribed_projects

    @subscribed_projects.setter
    def subscribed_projects(self, value: Iterable[Project]):
        self._subscribed_projects.extend(value)

    def add_subscribed_project(self, value: Project):
        self._subscribed_projects.append(value)

    @property
    def subscribed_repos(self) -> List[Repository]:
        return self._subscribed_repos

    @subscribed_repos.setter
    def subscribed_repos(self, value: Iterable[Repository]):
        self._subscribed_repos.extend(value)

    def add_subscribed_repo(self, value: Repository):
        self._subscribed_repos.append(value)

    @property
    def owned_projects(self) -> List[Project]:
        return self._owned_projects

    @owned_projects.setter
    def owned_projects(self, value: Iterable[Project]):
        self._owned_projects.extend(value)

    def add_owned_project(self, value: Project):
        self._owned_projects.append(value)

    @property
    def owned_repos(self) -> List[Repository]:
        return self._owned_repos

    @owned_repos.setter
    def owned_repos(self, value: Iterable[Repository]):
        self._owned_repos.extend(value)

    def add_owned_repo(self, value: Repository):
        self._owned_repos.append(value)

    @property
    def contributed_projects(self) -> List[Project]:
        return self._contributed_projects

    @contributed_projects.setter
    def contributed_projects(self, value: Iterable[Project]):
        self._contributed_projects.extend(value)

    def add_contributed_project(self, value: Project):
        self._contributed_projects.append(value)

    @property
    def contributed_repositories(self) -> List[Repository]:
        return self._contributed_repositories

    @contributed_repositories.setter
    def contributed_repositories(self, value: Iterable[Repository]):
        self._contributed_repositories.extend(value)

    def add_contributed_repository(self, value: Repository):
        self._contributed_repositories.append(value)
