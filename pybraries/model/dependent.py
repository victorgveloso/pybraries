from . import Dependency
from .platform import Platform


class Dependent(Dependency):
    def __init__(self, project_name: str = "", name: str = "", platform: Platform = None, requirements: str = "",
                 latest_stable: str = "", latest: str = "", deprecated: bool = False, outdated: bool = True,
                 kind: str = "runtime", **kwargs):
        super().__init__(project_name=project_name,
                         name=name,
                         requirements=requirements,
                         latest_stable=latest_stable,
                         latest=latest,
                         deprecated=deprecated,
                         outdated=outdated,
                         kind=kind,
                         platform=platform,
                         **kwargs)
