from core.entities.Agents.Agent import Agent
from core.entities.Agents.HH_agent import HH_agent
from core.entities.Agents.Habr_agent import Habr_agent
from core.entities.MyProfile import MyProfile
from core.entities.Vacancy import Vacancy


from core.utils.LW_process import LW_process
from core.utils.Utilities import Format

try:
    import common_py_lib
except ModuleNotFoundError:
    print('Import private library first')


def agent_create(vendor_name, config):
    match vendor_name:
        case 'hh':
            return HH_agent(config=config)
        case 'habr':
            return Habr_agent(config=config)
        case _:
            raise NotImplementedError('Implement type first')


class App:
    """
    Main class for application
    """
    agents: list[Agent]  # who will search
    profiles: list[MyProfile]  # it is not a secret that many peoples has many profiles

    favourites: list[Vacancy]  # favourite vacancies to apply on

    processes: list[LW_process]

    def __init__(self, config):
        self.agents = list()
        self.profiles = list()
        self.favourites = list()
        self.processes = list()

        self.config_ptr = config

    def init_agents(self):
        Format.prYellow('Initializing agents:')
        for vendor_name in self.config_ptr.vacancy_sites.keys():
            self.agents.append(agent_create(vendor_name, self.config_ptr))

    def start_app(self):
        Format.prYellow('App starting')
        for agent in self.agents:
            self.processes.append(LW_process(agent.agent_name, target=agent.search()))

        while True:
            pass

    def close_app(self):
        for browser in self.config_ptr.browsers:
            browser.close()

        for vacancy in self.favourites:
            pass
        Format.prYellow('App closing')
