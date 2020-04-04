from typing import Union

from pybraries.controller.internal.base import BaseController
from pybraries.utils import extract


class SubscriptionController(BaseController):
    def sub_api(self, action, manager="", package="", *args, **kwargs) -> Union[bool, str]:
        url_end_list = [
            "https://libraries.io/api/subscriptions"
        ]  # start of list to build url

        if action == "list_subscribed":
            self.kind = "get"
            url_combined = "/".join(url_end_list)
            resp = self.make_request(url_combined)
            return resp

        assert manager and package, "this operation requires manager and package definition"

        url_end_list += [manager, package]
        url_combined = "/".join(url_end_list)

        if action == "check_subscribed":
            self.kind = "get"
            resp = self.make_request(url_combined)
            return resp is not None
        if action == "subscribe":
            extract("include_prerelease").of(kwargs).then(url_end_list.append)
            self.kind = "post"
            self.make_request(url_combined)
            return "Successfully Subscribed"

        if action == "update_subscribe":
            self.kind = "put"
            # not implemented - seems libraries.io api has bug
            # if implemented in future, adjust modules in readme
            self.make_request(url_combined)
            return "include_prerelease is always set to true"

        if action == "delete_subscribe":
            # first check if subscribed. Must be done before build url.
            is_subscribed = self.sub_api(
                "check_subscribed", manager=manager, package=package
            )
            self.kind = "delete"
            if is_subscribed:
                self.make_request(url_combined)
                msg = "Successfully Unsubscribed"
            else:
                msg = f"Unsubscribe unnecessary. You are not subscribed to {package}."
            return msg

    # prerelease option currently not changeable for subscribe or update
    # (perhaps due to libraries.io api glitch)
    @staticmethod
    def __check_prerelease(*args, **kwargs):
        prerelease = kwargs.pop("include_prerelease", "")
        return prerelease
