import logging
from executer.commandbase import CommandBase


class Command(CommandBase):
    _logger = logging.getLogger(__name__)

    def __init__(self):
        super(Command, self).__init__()

    def init_options(self):
        CommandBase.init_options(self)

    def process_command(self):
        #here comes the magic
        pass

    def end_process_command(self):
        pass
