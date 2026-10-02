import signal
from typing import Final

from core.data.Config import Config
from core.entities.Finder_runner import Finder_runner

try:
    from common_py_lib.logger.CommonLogger import CommonLogger
    from common_py_lib.entities.Formatter import TextAnsiFormatter
except ModuleNotFoundError:
    print('Import private local module common py lib first')


class App:
    runner: Final[Finder_runner]
    logger: Final[CommonLogger]  # global instance of logger
    config: Final[Config]

    def __init__(self):
        self.config = Config()
        self.logger = CommonLogger()
        self.runner = Finder_runner(config_ptr=self.config, logger_ptr=self.logger)

    def run(self):
        self.runner.init_agents()

        self.runner.start_runner()
        self.runner.show_search_results()
        self.runner.save_search_results()
        self.runner.close_runner()


def signal_handler(sig, frame):
    """
    Handle sig int command
    :param sig: signal that handled
    :param frame: function to execute in case of signal
    :return: None
    """
    print('\n')  # just new line
    graceful_exit_from_app()
    exit(0)


def graceful_exit_from_app():
    app.runner.close_runner()
    TextAnsiFormatter.prYellow("Out program")


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)  # if program goes wrong

    app: Final[App] = App()
    app.run()
    graceful_exit_from_app()
