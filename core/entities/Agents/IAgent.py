"""
Search agent base class with page objects.
"""
import datetime
from abc import abstractmethod, ABC
from enum import Enum
from typing import Sequence

from playwright.sync_api import sync_playwright, Browser, Page

from core.entities.Vacancy import Vacancy

try:
    from common_py_lib.entities.Formatter import TextAnsiFormatter
except ModuleNotFoundError:
    print('Import private local common py lib first')


class Hardware_helper(str, Enum):
    """
    Enum class for helping with hardware, i.e. for monitors or other
    """
    first_monitor_param = '--window-position=1920,0'  # allowed param for fullHD monitors, x and y position of window
    second_monitor_param = '--window-position=3840,0'
    maximized = '--start-maximized'
    incognito = '--incognito'
    mute = '--mute-audio'
    without_devtools = '--disable-dev-tools'
    without_extensions = '--disable-extensions'


class IAgent(ABC):
    """
    Search agent base class.
    """
    # playwright data objects:
    browser: Browser
    page: Page

    # other data:
    start_link: str
    agent_name: str

    # vacancy containers:
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
        Main stage in agent entity to search for vacancies
        """
        pass

    @abstractmethod
    def add_to_later(self) -> None:
        """
        Add vacancy to favourites, maybe you are not acceptable (maybe not so many work years), but in future want to be
        """
        pass

    @abstractmethod
    def add_to_possible(self) -> None:
        """
        Possible vacancy to apply
        """
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
    def open_browser(start_link: str, params: Sequence[Hardware_helper]) -> tuple[Browser, Page]:
        """
        Open browser and return pointers to it with page
        """
        print('Open browser')
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=False, args=[*params])
                page = browser.new_page()
                page.goto(start_link)

                page.wait_for_load_state("networkidle")
                page.wait_for_timeout(2)

                return browser, page

        except Exception as e:
            TextAnsiFormatter.prRed(f'Exception during initializing web browser: {e}')
            raise
