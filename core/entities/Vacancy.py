import dataclasses


@dataclasses.dataclass(init=True, frozen=True)
class Vacancy:
    """
    Dataclass for vacancy in vacancy sites
    """
    name: str  # vacancy title
    skills: list[str]  # skills that need on vacancy
    city: str | None  # vacancy city
    workplace: str | None  # at employer office, remotely or hybrid
    workhours: int | None  # how many to work

    payment: float | None  # they pay money or not


def vacancy_sorter(vacancies: list[Vacancy]) -> list[Vacancy]:
    """
    Sort vacancies in likely order
    :param vacancies: list with vacancy objects
    :return: sorted list
    """
    pass
