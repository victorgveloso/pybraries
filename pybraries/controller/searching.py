# searching.py
from typing import List

from pybraries.controller.internal.base import BaseController
from pybraries.utils import sess, extract


class SearchingController(BaseController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def search_api(self, action, *args, filters=None, sort=None, **kwargs):
        """
        build and call for search

        Args:
            action (str): function action name
            filters (dict): filters passed to requests Session
            sort (str): to sort by. Options
            *args (str): positional arguments
            **kwargs (str): keyword arguments
        Returns:
            (list): list of dicts response from libraries.io.
                according to page and per page
            Many are dicts or list of dicts.
        """
        url_end_list = self._handle_path_params(action, *args, **kwargs)
        sess.params = self._handle_query_params(sort, filters, **sess.params, **kwargs)
        url_combined = "/".join(url_end_list)
        return self.make_request(url_combined)

    @staticmethod
    def _handle_query_params(sort=None, filters=None, **kwargs):
        if "project" in kwargs:
            kwargs['q'] = kwargs.pop("project")
        if sort is not None:
            kwargs["sort"] = sort
        if filters is not None:
            kwargs.update(filters)
        return kwargs

    @staticmethod
    def _handle_path_params(action, *args, **kwargs):
        def from_kwargs(*keys):
            return extract(*keys).of(kwargs).then([].append)

        url_end_list: List[str] = ["https://libraries.io/api"]  # start of list to build url
        if action == "special_project_search":
            url_end_list.append("search?")
        elif action == "platforms":
            url_end_list.append("platforms")

        elif action.startswith("project"):
            action = action[7:]  # remove action prefix
            url_end_list += [*from_kwargs("platforms", "project"), *args]
            if action.startswith("_"):
                action = action[1:]  # remove remaining underscore from operation name
                if action == "dependencies":
                    version = kwargs.pop("version") or "latest"  # defaults to latest
                    url_end_list.append(version)
                url_end_list.append(action)
        elif action.startswith("repository"):
            action = action[len("repository"):]
            url_end_list += [*from_kwargs("host", "owner", "repo"), *args]
            if action.startswith("_"):
                url_end_list.append(action[1:])
        elif "user" in action:
            url_end_list += [*from_kwargs("host", "user"), *args]
            if action == "user_repositories":
                url_end_list.append("repositories")

            if action == "user_projects":
                url_end_list.append("projects")

            if action == "user_projects_contributions":
                url_end_list.append("project-contributions")

            if action == "user_repositories_contributions":
                url_end_list.append("repository-contributions")

            if action == "user_dependencies":
                url_end_list.append("dependencies")
        return url_end_list
