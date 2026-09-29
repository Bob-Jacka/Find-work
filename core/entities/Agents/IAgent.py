"""
Search agent base class.
"""

from abc import abstractmethod, ABC

from playwright.sync_api import sync_playwright, Browser, Page

from core.entities.Vacancy import Vacancy


class IAgent(ABC):
    """
    Search agent base class.
    """

    start_link: str
    agent_name: str
    later_see: list[Vacancy]
    favourite: list[Vacancy]

    @abstractmethod
    def login(self) -> None:
        """
        Login on agent (vendor) site
        """
        pass

    @abstractmethod
    def search(self) -> None:
        """
        Search for vacancies on the site
        """
        pass

    @abstractmethod
    def add_to_later(self) -> None:
        """
        Add vacancy to favourites, maybe you are not acceptable, but in future want to be
        """
        pass

    @abstractmethod
    def add_to_interesting(self) -> None:
        pass

    @abstractmethod
    def apply_to_vacancy(self) -> None:
        """
        Send application to company you like
        """
        pass

    @staticmethod
    def open_browser(start_link: str) -> tuple[Browser, Page] | None:
        """
        Open browser
        """
        print('Open browser')
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=False)
                page = browser.new_page()
                page.goto(start_link)

                page.wait_for_load_state("networkidle")

                return browser, page

        except Exception as e:
            print(f'Exception during initializing web browser: {e}')
