from playwright.sync_api import Page, Locator

from src.roboforex.ui.pages.base_page import BasePage


class LoginPage(BasePage):
    """Roboforex login page."""
    URL = "https://stockstrader.roboforex.com/login"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        # Login page specific elements
        self.language_selector_dropdown = self.page.locator("//div[@id='language-selector']")
        self.email_field = self.page.locator("//input[@type='email']")
        self.password_field = self.page.locator("//input[@type='password']")
        self.forgot_password_button = self.page.locator("//ion-label[@translate='login.ForgotPassword']")
        self.submit_button = self.page.locator("//ion-button[ion-label[@translate='login.Continue']]")


    def submit(self) -> None:
        """Click submit button. If cookies popup is visible, disallow it."""
        if self.submit_button.is_disabled() and self.disallow_cookies_button.is_visible():
            self.disallow_cookies_button.click()
        self.submit_button.click()


    def language_selector_option(self, language: str) -> Locator:
        """Get the language selector option element."""
        return self.page.locator(f"//div[contains(@class, 'modal-item__text')][text()='{language}']")
