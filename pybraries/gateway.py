from pybraries import SubscriptionAPI, SearchingAPI
from pybraries.model import Project, Platform


class Gateway:
    def __init__(self, subscription_api: SubscriptionAPI, search_api: SearchingAPI, **kwargs):
        super().__init__(**kwargs)
        self.subscription_api = subscription_api
        self.search_api = search_api

    def project(self, platform: Platform, name: str) -> Project:
        data = self.search_api.project(platform.name, name)
        project = Project.from_dict(data)
        platform.add_project(project)
        return project
