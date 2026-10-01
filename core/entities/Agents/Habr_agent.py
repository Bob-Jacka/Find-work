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

class Habr_agent(IAgent):

    def __init__(self, config):
        self.agent_name = 'Habr agent'
        self.config_ptr = config
        self.favourite = list()
        self.later_see = list()


    def login(self) -> None:
        pass

    def search(self) -> None:
        print(f'{self.agent_name} started working')
        print(f'{self.agent_name} ended working')

    def add_to_later(self) -> None:
        pass

    def add_to_possible(self) -> None:
        pass

    def apply_to_vacancy(self) -> None:
        pass
