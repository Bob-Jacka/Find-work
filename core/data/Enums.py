from enum import Enum


class Work_status(str, Enum):
    WORKING = 'working'
    SEARCH = 'search'
    NOT_SEARCH = 'not searching'
    VERY_VERY_ACTIVELY_SEARCHING = 'very very searching'


class Agent_vendor(str, Enum):
    HH = 'hh'
    HABR = 'habr'
