from playwright.sync_api import BrowserType  # TODO maybe delete browser type

from core.data.Enums import Agent_vendor

try:
    from core.data.CurrentInfo import hh_site_link, habr_site_link
except Exception as e:
    print('No file with current Data for agents in app data directory')
    exit(1)


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
        self.vacancy_sites[Agent_vendor.HH] = hh_site_link
        self.vacancy_sites[Agent_vendor.HABR] = habr_site_link
