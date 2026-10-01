"""
Search agent base class.
"""
import datetime
from abc import abstractmethod, ABC

from common_py_lib.entities.Formatter import TextAnsiFormatter
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
        Login on agent (vendor) site, using playwright library
        """
        pass

    @abstractmethod
    def search(self) -> None:
        """
        Search stage for vacancies on the site
        """
        pass

    @abstractmethod
    def add_to_later(self) -> None:
        """
        Add vacancy to favourites, maybe you are not acceptable, but in future want to be
        """
        pass

    @abstractmethod
    def add_to_possible(self) -> None:
        pass

    @abstractmethod
    def apply_to_vacancy(self) -> None:
        """
        Send application to company you like
        """
        pass

    @staticmethod
    def current_time():
        return datetime.datetime.now()

    @staticmethod
    def open_browser(start_link: str) -> tuple[Browser, Page] | None:
        """
        Open browser and return pointers to it with page
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
            TextAnsiFormatter.prRed(f'Exception during initializing web browser: {e}')
