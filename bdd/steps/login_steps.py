from dataclasses import dataclass
from time import sleep, time

import pytest
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then, parsers

from src.roboforex.ui.pages.login_page import LoginPage


@pytest.fixture()
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@dataclass
class UserCredentials:
    email: str
    password: str

@given("the user is on the login page")
def user_on_login_page(login_page: LoginPage) -> None:
    login_page.goto()
    login_page.check_current_url()
    expect(login_page.email_field).to_be_visible()


@when(parsers.parse("the user logs in with valid credentials of the existing account"))
def login_attempt_with_valid_credentials(login_page: LoginPage, user_account: UserCredentials):
    login_page.email_field.fill(user_account.email)
    login_page.password_field.fill(user_account.password)
    login_page.submit()

@then("the user should be redirected to the profile page")
def check_successful_login() -> None:
    # TODO: successful login checks
    sleep(3)


@given("existing user account", target_fixture="user_account")
def user_account():
    unique_email = f"some_user_{int(time() * 1000)}@gmail.com"
    # TODO: user creation steps
    return UserCredentials(unique_email, "c0rrect_P@ssword")
