from typing import List, Iterable

from . import Project
from .internal.base import Base


class Platform(Base):
    def __init__(self, name: str = "", default_language: str = "", homepage: str = "", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.default_language = default_language
        self.homepage = homepage
        self._projects = []

    @property
    def projects(self) -> List[Project]:
        return self._projects

    @projects.setter
    def projects(self, value: Iterable[Project]):
        self._projects.extend(value)

    def add_project(self, project: Project):
        self._projects.append(project)
