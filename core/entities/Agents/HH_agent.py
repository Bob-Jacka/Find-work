from core.entities.Agents.Agent import Agent


class _Login_page:
    telephone_field: str
    sign_in_btn: str

    def __init__(self, page):
        pass


class _Vacancy_page:
    def __init__(self, page):
        pass


class HH_agent(Agent):

    def __init__(self, config):
        self.agent_name = 'HH agent'
        self.config_ptr = config

    def login(self) -> None:
        browser, page = self.open_browser(self.config_ptr.vacancy_sites['hh'])
        self.config_ptr.browsers.append(browser)

        login_page = _Login_page(page)

    def search(self) -> None:
        print(f'{self.agent_name} started working')

    def add_to_favourite(self) -> None:
        pass

    def add_to_interesting(self) -> None:
        pass

    def apply_to_vacancy(self) -> None:
        pass
