"""Tests for `pybraries Subscribe` package."""
from time import sleep

import pytest

from pybraries.api import SubscriptionAPI

mgr = "pypi"  # package manager name
repo2 = "pandas"  # repository name
repo3 = "scikit-learn"  # repo name


@pytest.fixture
def ctrl():
    from pybraries.controller import SubscriptionController
    return SubscriptionController()


# fixture to avoid hitting rate limit
@pytest.fixture(autouse=True, scope="function")
def wait_a_sec():
    yield
    sleep(1)


@pytest.fixture
def subs(ctrl):
    return SubscriptionAPI(ctrl)  # instantiate subscribe api object


# subscribe to pandas
@pytest.fixture
def pre_unsub(subs):
    subs.unsubscribe("pypi", "pandas")


# unsubscribe from pandas
@pytest.fixture
def pre_sub(subs):
    subs.subscribe("pypi", "pandas")


# variables for testing


# first need to subscribe the user to package updates
# my search key is subscribed, so will work for travis tests
# won't pass locally for development if user search_key isn't subscribed to any packages
@pytest.mark.xfail(raises=IndexError)
def test_list_subscribed(subs):
    """for subscriber- returns a list item subscription with a project rank >= 0"""
    sub = subs.list_subscribed()
    assert sub[0]["project"]["rank"] >= 0


def test_check_subscribed(subs):
    """for subscriber - check if user is subscribed to a project with a rank >= 0"""
    check_sub = subs.check_subscribed(mgr, repo3)
    assert type(check_sub) is bool


def test_subscribe(subs, pre_unsub):
    """for subscribe key sent- use args to check if subscribed"""
    sub = subs.subscribe(mgr, repo2)
    assert type(sub) is str


def test_subscribe_kwargs(subs, pre_unsub):
    """for api key sent- use kwargs to check if subscribed"""
    sub = subs.subscribe(manager=mgr, package=repo2)
    assert type(sub) is str


@pytest.mark.skip()
def test_update_subscribe(subs):
    """for api key sent- doesn't error"""
    update = subs.update_subscribe(mgr, repo2)
    pass


@pytest.mark.skip()
def test_update_subscribe_updates(subs):
    """for api key sent- change subscription for prerelease to false"""
    update = subs.update_subscribe(mgr, repo2, False)
    assert update["include_prerelease"] is False


def test_unsubscribe_kwargs(subs, pre_sub):
    """subscribed person gets unsubscribed message"""
    del_sub = subs.unsubscribe(manager=mgr, package=repo2)
    assert del_sub == "Successfully Unsubscribed"


def test_unsubscribe_intercept(subs, pre_unsub):
    """returns no unsubscribe needed if not subscribed"""
    del_sub = subs.unsubscribe(manager=mgr, package=repo2)
    assert "Unsubscribe unnecessary" in del_sub


# slow
def test_unsubscribe_args(subs, pre_sub):
    """for api key sent- doesn't error if not already subscribed"""
    del_sub = subs.unsubscribe(mgr, repo2)
    assert del_sub == "Successfully Unsubscribed"


def test_unsubscribe_works(subs):
    """unsubscribes and verifies"""
    del_sub = subs.unsubscribe(mgr, repo2)
    bsub = subs.check_subscribed(mgr, repo2)
    assert bsub is False
