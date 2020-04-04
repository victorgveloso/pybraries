from requests import HTTPError

from pybraries.utils import clear_params, fix_pages, sess


class BaseController:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kind = "get"

    def make_request(self, url: str) -> str:
        """ call api server

            Args:
                url (str): base url to call
                kind (str): get, post, put, or delete
            Returns:
                json encoded response from libraries.io
        """

        try:
            params = {"include_prerelease": "False"} if self.kind == "post" else {}
            fix_pages()  # Must be called before any request for page validation
            r = getattr(sess, self.kind)(url, params=params)
            r.raise_for_status()
            return r.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        finally:
            clear_params()
