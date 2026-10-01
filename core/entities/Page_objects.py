from abc import abstractproperty


class Page_objects:
    """
    Class for page objects in agents
    """

    @abstractproperty
    class Login_page:
        pass

    @abstractproperty
    class Vacancy_page:
        pass
