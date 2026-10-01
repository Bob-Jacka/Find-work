from core.entities.Agents.IAgent import IAgent
from core.entities.Agents.HH_agent import HH_agent
from core.entities.Agents.Habr_agent import Habr_agent
from core.entities.MyProfile import MyProfile
from core.entities.Vacancy import Vacancy

try:
    from common_py_lib.entities import LW_process
except ModuleNotFoundError:
    print('Import private common py library first')


def agent_create(vendor_name: str, config_ptr):
    """
    Fabric method, create search agent and return it
    param vendor_name: name of the company that hosts the site
    param config_ptr: pointer to config
    """
    match vendor_name:
        case 'hh':
            return HH_agent(config=config_ptr)
        case 'habr':
            return Habr_agent(config=config_ptr)

        case _:
            raise NotImplementedError('Implement type first')


class App:
    """
    Main class for application
    """
    agents: list[IAgent]  # who will search
    profiles: list[MyProfile]  # it is not a secret that many peoples has many profiles
    favourites: list[Vacancy]  # favourite vacancies to apply on
    later_to_see: list[Vacancy]  # maybe in future apply

    processes: list[LW_process.LW_process]

    def __init__(self, config_ptr, logger_ptr):
        self.agents = list()
        self.profiles = list()
        self.favourites = list()
        self.processes = list()

        self.config_ptr = config_ptr
        self.logger_ptr = logger_ptr

    def init_agents(self):
        """
        Initialize agents in application with vendor names
        """
        self.logger_ptr.log('Initializing agents:')
        for vendor_name in self.config_ptr.vacancy_sites.keys():
            self.logger_ptr.log(f'Init agent: with vendor name {vendor_name.value()}')
            self.agents.append(agent_create(vendor_name, self.config_ptr))

    def start_app(self):
        """
        Start app execution loop
        """
        self.logger_ptr.log('App starting')
        for agent in self.agents:
            self.processes.append(LW_process.LW_process(agent.agent_name, target=agent.search()))

    def show_search_results(self):
        """
        Simple show search results to console
        """
        for num, vacancy in enumerate(self.favourites):
            print(f'Vacancy: №{num}')
            print('\tName' + vacancy.name)
            print('\tCity' + vacancy.city if vacancy.city is not None else 'No data')
            print('\tPayment' + vacancy.payment if vacancy.payment is not None else 'No data')
            print('\tWorkhours' + vacancy.workhours if vacancy.workhours is not None else 'No data')
            print('\tWorkplace' + vacancy.workplace if vacancy.workplace is not None else 'No data')
            print('\tNeeded skills' + vacancy.skills)

    def save_search_results(self, local: bool = True, remote: bool = False):
        """
        Save search results in remote or local devices
        """
        if local:
            pass

        if remote:
            pass

    def close_app(self):
        for browser in self.config_ptr.browsers:
            browser.close()
        self.logger_ptr.log('App closing')
