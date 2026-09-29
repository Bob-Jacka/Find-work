from core.entities.Agents.Agent import Agent


class Habr_agent(Agent):

    def __init__(self, config):
        self.agent_name = 'Habr agent'
        self.config_ptr = config

    def login(self) -> None:
        pass

    def search(self) -> None:
        print(f'{self.agent_name} started working')

    def add_to_favourite(self) -> None:
        pass

    def add_to_interesting(self) -> None:
        pass

    def apply_to_vacancy(self) -> None:
        pass
