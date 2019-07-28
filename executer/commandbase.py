from abc import ABCMeta, abstractmethod

from django.core.management.base import BaseCommand


class CommandBase(BaseCommand):
    ERROR_CODE = 1
    NORMAL_EXIT_CODE = 0

    __metaclass__ = ABCMeta

    _logger = None
    options = None
    required_options = None

    def __init__(self):
        super(CommandBase, self).__init__()
        self.required_options = []

    def execute(self, *args, **options):
        options['no_color'] = options.get('no_color', False)
        super(CommandBase, self).execute(self, *args, **options)

    def handle(self, *args, **options):
        try:
            self.options = options
            self.log_options()
            self.init_options()
            self.process_command()
        except Exception, exception:
            self._logger.error(str(exception))
            self.exit_command()
        finally:
            self.end_process_command()
            self.log_summary()

    # init command methods

    def init_options(self):
        self.check_options_are_provided()

    def check_options_are_provided(self):
        if self.required_options:
            missing_options = [value for value in self.required_options if not self.options.get(value)]
            if missing_options:
                self.log_missing_options(missing_options)
                self.exit_command()

    # main command methods

    @abstractmethod
    def process_command(self):
        pass

    @abstractmethod
    def end_process_command(self):
        pass

    # log methods

    def log_options(self):
        self._logger.info('OPTIONS:')
        self._logger.info(self.options)

    def log_missing_options(self, options):
        options_text = ', '.join(options)
        self._logger.error('The options {list} are required to execute the command. '
                           'Use -h to see all the options.'.format(list=options_text))

    def log_errors_list(self, errors):
        for error in errors:
            self._logger.error(error)

    @abstractmethod
    def log_summary(self):
        pass

    def exit_command_after_log_warning(self, message):
        self._logger.error(message)
        self.exit_command(self.NORMAL_EXIT_CODE)

    def exit_command_after_log_error(self, message):
        self._logger.error(message)
        self.exit_command()

    def exit_command(self, exit_code=ERROR_CODE):
        exit(exit_code)
