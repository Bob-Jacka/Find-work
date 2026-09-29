import signal

from core.data.Config import Config
from core.entities.App import App
from core.utils.BotLogger import BotLogger
from core.utils.Utilities import Format


def signal_handler(sig, frame):
    """
    Handle sig int command
    :param sig: signal
    :param frame: function to execute in case of signal
    :return: None
    """
    print('\n')
    app.close_app()
    Format.prYellow("Out program")
    exit(0)


logger: BotLogger = BotLogger()  # global instance of logger
config: Config = Config()
app: App

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)  # if program goes wrong

    app = App(config)
    app.init_agents()

    app.start_app()
    app.close_app()
