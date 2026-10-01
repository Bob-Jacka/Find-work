import signal

from core.data.Config import Config
from core.entities.App import App

try:
    from common_py_lib.logger.CommonLogger import CommonLogger
    from common_py_lib.entities.Formatter import TextAnsiFormatter
except ModuleNotFoundError:
    print('Import private local module common py lib first')


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
    app.close_app()
    TextAnsiFormatter.prYellow("Out program")


logger: CommonLogger = CommonLogger()  # global instance of logger
config: Config = Config()
app: App

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)  # if program goes wrong

    app = App(config_ptr=config, logger_ptr=logger)
    app.init_agents()

    app.start_app()
    app.show_search_results()
    app.save_search_results()
    app.close_app()
