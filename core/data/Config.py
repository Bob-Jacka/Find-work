from playwright.sync_api import BrowserType  # TODO maybe delete browser type

from core.data.Enums import Agent_vendor

vacancy_sites_dict: dict[str, str] = {
    'hh': 'https://izhevsk.hh.ru/?ysclid=mup5yzegb5277727803',
    'habr': '',
}


class Config:
    """
    Config object with data to use in app
    """
    vacancy_sites: dict[Agent_vendor, str]  # key is vendor and value is url
    browsers: list[BrowserType]

    def __init__(self):
        self.vacancy_sites = dict()
        self.browsers = list()

        # add another vacancy site to config file:
        self.vacancy_sites[Agent_vendor.HH] = vacancy_sites_dict['hh']
        self.vacancy_sites[Agent_vendor.HABR] = vacancy_sites_dict['habr']

    def get_browser_ptr_by_name(self, browser_name: str):
        return self.browsers

    def get_all_browsers(self):
        return self.browsers

    def get_vacancy_site_by_name(self, site_name):
        return self.vacancy_sites[site_name]

    def get_all_vacany_sites(self):
        return self.vacancy_sites
