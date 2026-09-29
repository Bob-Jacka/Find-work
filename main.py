import signal

from core.data.Config import Config
from core.entities.App import App
from core.utils.BotLogger import BotLogger
from core.utils.Utilities import Format

try:
    import common_py_lib
except ModuleNotFoundError:
    print('Import private local module common py lib first')


def signal_handler(sig, frame):
    """
    Handle sig int command
    :param sig: signal
    :param frame: function to execute in case of signal
    :return: None
    """
    print('\n')  # just new line
    graceful_exit_from_app()
    exit(0)


def graceful_exit_from_app():
    app.close_app()
    Format.prYellow("Out program")


logger: BotLogger = BotLogger()  # global instance of logger
config: Config = Config()
app: App

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)  # if program goes wrong

    app = App(config, logger)
    app.init_agents()

    app.start_app()
    app.show_search_results()
    app.save_search_results()
    app.close_app()
