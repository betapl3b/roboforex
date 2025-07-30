from dataclasses import dataclass
from time import sleep, time

import pytest
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then, parsers

from src.roboforex.ui.pages.login_page import LoginPage
from src.roboforex.ui.pages.trading_page import TradingPage


@pytest.fixture()
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture()
def trading_page(page: Page) -> TradingPage:
    return TradingPage(page)

@dataclass
class User:
    email: str
    password: str
    name: str
    surname: str
    account: str

@given("the user is on the login page")
def user_on_login_page(login_page: LoginPage) -> None:
    login_page.goto()
    login_page.check_current_url()
    expect(login_page.email_field).to_be_visible()


@when(parsers.parse("the user logs in with valid credentials of the existing account"))
def login_attempt_with_valid_credentials(login_page: LoginPage, existing_user: User):
    login_page.email_field.fill(existing_user.email)
    login_page.password_field.fill(existing_user.password)
    login_page.submit()

@then("correct user account number is shown on trading page")
def check_successful_login(trading_page: TradingPage, existing_user: User) -> None:
    expect(trading_page.demo_account, "Wrong user account number").to_have_text(existing_user.account)


@given("existing user account", target_fixture="existing_user")
def existing_user() -> User:
    return User(
        email="usmn7yukca@ibolinva.com",
        password="983870A(X$h",
        name="Test",
        surname="Task",
        account="92169495-demo",
    )
