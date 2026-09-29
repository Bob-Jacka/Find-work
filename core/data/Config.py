from playwright.sync_api import BrowserType  # TODO maybe delete browser type

from core.data.Enums import Agent_vendor

try:
    from core.data.CurrentInfo import hh_site_link, habr_site_link
except Exception as e:
    print('No file with current Data in data directory')
    exit(1)


class Config:
    vacancy_sites: dict[Agent_vendor, str]  # key is vendor and value is url
    browsers: list[BrowserType]

    def __init__(self):
        self.vacancy_sites = dict()
        self.browsers = list()

        # add another vacancy site
        self.vacancy_sites[Agent_vendor.HH] = hh_site_link
        self.vacancy_sites[Agent_vendor.HABR] = habr_site_link
