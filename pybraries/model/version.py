import datetime

from jsonpickle.handlers import DatetimeHandler

from .internal.base import Base
from .project import Project


@DatetimeHandler.handles
class Version(Base):
    def __init__(self, number: str = "", usage: int = 0, project: Project = None,
                 published_at: datetime.datetime = datetime.datetime.now(), **kwargs):
        super().__init__(**kwargs)
        self.number = number
        self.usage = usage
        self.published_at = published_at
        self._project = project

    @property
    def project(self) -> Project:
        return self._projects

    @project.setter
    def project(self, value: Project):
        self._project = value
