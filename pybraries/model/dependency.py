from pybraries.model import Platform


class Dependency:
    def __init__(self, project_name: str = "", name: str = "", platform: Platform = None, requirements: str = "",
                 latest_stable: str = "", latest: str = "", deprecated: bool = False, outdated: bool = True,
                 kind: str = "runtime", **kwargs):
        super().__init__(**kwargs)
        self.project_name = project_name
        self.name = name
        self.requirements = requirements
        self.latest_stable = latest_stable
        self.latest = latest
        self.deprecated = deprecated
        self.outdated = outdated
        self.kind = kind
        self._platform = platform

    @property
    def platform(self) -> Platform:
        return self._platform

    @platform.setter
    def platform(self, value: Platform):
        self._platform = value
