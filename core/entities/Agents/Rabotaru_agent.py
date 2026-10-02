"""
Agent for Rabota.ru site with vacancies
"""

from core.entities.Agents.IAgent import IAgent


class Page_objects:
    class _Login_page:
        telephone_field: str
        sign_in_btn: str

        def __init__(self, page):
            pass

    class _Vacancy_page:
        def __init__(self, page):
            pass


class Rabotaru_agent(IAgent):

    def login(self) -> None:
        pass

    def search(self) -> None:
        pass

    def add_to_later(self) -> None:
        pass

    def add_to_possible(self) -> None:
        pass

    def apply_to_vacancy(self) -> None:
        pass

    @staticmethod
    def current_time():
        return super().current_time()