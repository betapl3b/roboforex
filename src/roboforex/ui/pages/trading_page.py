from playwright.sync_api import Page, Locator

from src.roboforex.ui.pages.base_page import BasePage


class TradingPage(BasePage):
    """Roboforex trading page."""
    URL = "https://stockstrader.roboforex.com/trading"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.demo_account = self.page.locator("//div[contains(@class, 'app__header_stats_block_account-number')]")
