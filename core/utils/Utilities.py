class Format:
    """
    Utility class for text formater
    Includes print functions in different colors and underline technology.
    """

    @staticmethod
    def prRed(string: str):
        print("\033[91m {}\033[00m".format(string))

    @staticmethod
    def prGreen(string: str):
        print("\033[92m {}\033[00m".format(string))

    @staticmethod
    def prYellow(string: str):
        print("\033[93m {}\033[00m".format(string))

    @staticmethod
    def prCyan(string: str):
        print("\033[96m {}\033[00m".format(string))

    @staticmethod
    def prUnderline(string: str):
        print("\033[4m {}\033[0m".format(string))


def handle_critical_error(msg: str):
    Format.prRed(msg)
    exit(1)
