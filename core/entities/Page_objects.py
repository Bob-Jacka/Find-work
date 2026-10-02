from abc import ABC
from typing import Callable

from playwright.sync_api import Page


class IExtendable(ABC):
    """
    Interface for extending
    """

    def add_element(self, element_name, locator: str):
        """
        Add element to page in dynamic style
        """
        setattr(self, element_name, locator)

    def add_behaviour(self, behaviour_name, behaviour: Callable):
        """
        Add some behavior to page with lambda function
        """
        if isinstance(behaviour, Callable):
            setattr(self, behaviour_name, behaviour)
        else:
            raise Exception('Wrong behaviour type to add in page object')


class Page_objects:
    """
    Class for page objects in agents
    """

    class Home_page(IExtendable):
        pass

    class Login_page(IExtendable):
        """
        Page for writing login and password
        """
        pass

    class Vacancies_page(IExtendable):
        """
        Page where stored vacancies
        """
        pass

    class Vacancy_page(IExtendable):
        """
        Page for vacancy
        """
        pass

    class Settings_page(IExtendable):
        pass

    @staticmethod
    def add_attribute_2_page(page_to_change, name, locator: str):
        """
        Add elements to page object object
        :param page_to_change: page that need to change
        :param name: name of the element to add to page
        :param locator: given value to that element (i.e. locator on the page)
        """
        if isinstance(locator, str):
            setattr(page_to_change, name, locator)
        else:
            raise Exception('Wrong value type to add in page object')

    @staticmethod
    def proceed_to_page(page: Page, to: str):
        if page is not None:
            page.goto(to, timeout=5)
