try:
    import ai_lib
except ModuleNotFoundError:
    print('Import private local ai lib first')

class AI:
    """
    AI functionality to help find work
    """

    def __init__(self):
        pass

    def check_vacancy(self) -> bool:
        """
        Check if vacancy is suitable for profile
        """
        pass

    def generate_covering_letter(self) -> str:
        """
        Generate text (covering later) to support your application and resume
        """
        pass

    def check_resume(self):
        """
        Check your résumé and give advices to you
        """
        pass
