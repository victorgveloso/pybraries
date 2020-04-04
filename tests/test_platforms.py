import random

import pytest
from pyexpect import expect

from pybraries.api.searching import SearchingAPI


@pytest.fixture
def search():
    from pybraries.controller import SearchingController
    ctrl = SearchingController()
    return SearchingAPI(ctrl)


@pytest.fixture
def platforms(search):
    return search.platform()


@pytest.fixture
def any_platform(platforms):
    return random.choice(platforms)


def test_platforms_typing(platforms):
    expect(platforms).to_be_a_list_of(dict)


def test_platform_attributes(any_platform):
    expect(any_platform).to_include("name", "project_count", "homepage", "color", "default_language")
