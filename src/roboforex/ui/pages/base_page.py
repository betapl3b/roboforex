from abc import ABC
from typing import ClassVar, Optional

from playwright.sync_api import Page, Locator


class BasePage(ABC):
    # Inherited pages must have URL for goto() and check_current_url()
    URL: ClassVar[Optional[str]] = None

    def __init__(self, page: Page) -> None:
        self.page = page
        self.page.set_default_timeout(10000)
        # These elements are accessible from any page
        self.allow_cookies_button = self.page.locator("//ion-button[@translate='cookies.allow']")
        self.disallow_cookies_button = self.page.locator("//ion-button[@translate='cookies.disallow']")

    def goto(self) -> None:
        """Go to defined page URL."""
        # "commit" prevents waiting for "endless" loading and allows to navigate page as soon as it starts loading
        self.page.goto(self.URL, wait_until="commit")

    def check_current_url(self) -> None:
        """Assert that browser tab has correct URL."""
        assert self.URL in self.page.url, f"Wrong URL!"
