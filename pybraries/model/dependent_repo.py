import datetime

from jsonpickle.handlers import DatetimeHandler

from .internal.base import Base


@DatetimeHandler.handles
class DependentRepository(Base):
    def __init__(self, full_name: str = "", description: str = "",
                 created_at: datetime.datetime = datetime.datetime.now(),
                 updated_at: datetime.datetime = datetime.datetime.now(),
                 host_type: str = "github", scm: str = "git", language: str = "",
                 homepage: str = "", subscribers_count: int = 0, contributions_count: int = 0,
                 forks: int = 0, stars: int = 0, size: int = 0, **kwargs):
        super().__init__(**kwargs)
        self.full_name = full_name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.host_type = host_type
        self.scm = scm
        self.language = language
        self.homepage = homepage
        self.subscribers_count = subscribers_count
        self.contributions_count = contributions_count
        self.forks = forks
        self.stars = stars
        self.size = size
