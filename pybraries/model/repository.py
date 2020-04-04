import datetime
from typing import List, Iterable

from jsonpickle.handlers import DatetimeHandler

from .dependent_repo import DependentRepository
from .project import Project
from .user import User


@DatetimeHandler.handles
class Repository(DependentRepository):
    def __init__(self, full_name: str = "", description: str = "",
                 created_at: datetime.datetime = datetime.datetime.now(),
                 updated_at: datetime.datetime = datetime.datetime.now(),
                 host_type: str = "github", scm: str = "git", language: str = "",
                 homepage: str = "", subscribers_count: int = 0, contributions_count: int = 0,
                 forks: int = 0, stars: int = 0, size: int = 0, projects: List[Project] = None,
                 owner: User = None, subscribers: List[User] = None,
                 contributors: List[User] = None, **kwargs):
        super().__init__(
            full_name=full_name,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            host_type=host_type,
            scm=scm,
            language=language,
            homepage=homepage,
            subscribers_count=subscribers_count,
            contributions_count=contributions_count,
            forks=forks,
            stars=stars,
            size=size,
            **kwargs)
        self._owner = owner
        self._subscribers = [] if subscribers is None else subscribers
        self._contributors = [] if contributors is None else contributors
        self._projects = [] if projects is None else projects

    @property
    def projects(self) -> List[Project]:
        return self._projects

    @projects.setter
    def projects(self, value: Iterable[Project]):
        self._projects.extend(value)

    def add_project(self, project: Project):
        self._projects.append(project)

    @property
    def owner(self) -> User:
        return self._owner

    @owner.setter
    def owner(self, value: User):
        self._owner = value

    @property
    def subscribers(self) -> List[User]:
        return self._subscribers

    @subscribers.setter
    def subscribers(self, value: Iterable[User]):
        self._subscribers.extend(value)

    def add_subscriber(self, value: User):
        self._subscribers.append(value)

    @property
    def contributors(self) -> List[User]:
        return self._contributors

    @contributors.setter
    def contributors(self, value: Iterable[User]):
        self._contributors.extend(value)

    def add_contributor(self, value: User):
        self._contributors.append(value)
