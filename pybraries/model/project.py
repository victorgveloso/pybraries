from typing import List, Iterable

from .dependent import Dependent
from .internal.base import Base
from .platform import Platform
from .user import User
from .version import Version


class Project(Base):
    def __init__(self, name: str = "", language: str = "", homepage: str = "", rank: int = 0, forks: int = 0,
                 stars: int = 0, description: str = "", deprecation_reason: str = "", platform: Platform = None,
                 versions: List[Version] = None, owner: User = None, subscribers: List[User] = None,
                 contributors: List[User] = None, dependents: List[Dependent] = None, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self.language = language
        self.homepage = homepage
        self.forks = forks
        self.stars = stars
        self.rank = rank
        self.deprecation_reason = deprecation_reason
        self._platform = platform
        self._owner = owner
        self._dependents = [] if dependents is None else dependents
        self._subscribers = [] if subscribers is None else subscribers
        self._contributors = [] if contributors is None else contributors
        self._versions = [] if versions is None else versions

    @property
    def platform(self) -> Platform:
        return self._platform

    @platform.setter
    def platform(self, value: Platform):
        self.platform = value

    @property
    def versions(self) -> List[Version]:
        return self._versions

    @versions.setter
    def versions(self, value: Iterable[Version]):
        self._versions.extend(value)

    def add_version(self, value: Version):
        self._versions.append(value)

    @property
    def owner(self) -> User:
        return self._owner

    @owner.setter
    def owner(self, value: User):
        self._owner = value

    @property
    def dependents(self) -> List[Dependent]:
        return self._dependents

    @dependents.setter
    def dependents(self, value: Iterable[Dependent]):
        self._dependents.extend(value)

    def add_dependent(self, value: Dependent):
        self._dependents.append(value)

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
