import os
from datetime import datetime


class TextFormat:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Prefix:
    LOG = "LOG"
    DEBUG = "DEBUG"
    WARNING = "WARNING"
    ERROR = "ERROR"
    SEPERATOR = ":"


class Logger:

    def __init__(self, debug=False, timestamp_format=None, log_dir=None,
                 log_file_name=None):
        self._debug = debug
        self._timestamp_format = timestamp_format
        self._log_dir = log_dir
        self._log_file_name = log_file_name

    def _format_log(self, msg, prefix):
        timestamp = self.get_timestamp()
        return f"{timestamp}---{prefix:8}{Prefix.SEPERATOR:3}{msg}"

    def _write_to_file(self, msg):
        if self._log_dir is None:
            return
        if self._log_file_name is None:
            self._log_file_name = self.get_timestamp().replace(":", "_")\
                .replace(" ", "_")
        full_path = os.path.join(self._log_dir, self._log_file_name)
        try:
            with open(full_path, "a") as f:
                f.write(msg + "\n")
                f.close()
        except Exception as e:
            print(str(e))

    def get_timestamp(self):
        if self._timestamp_format is not None:
            timestamp = datetime.now().strftime(self._timestamp_format)
        else:
            timestamp = str(datetime.now())
        return timestamp

    def log(self, msg):
        out_msg = self._format_log(msg, Prefix.LOG)
        print(out_msg)
        self._write_to_file(out_msg)

    def debug(self, msg):
        out_msg = self._format_log(msg, Prefix.DEBUG)
        if self._debug:
            print(TextFormat.OKBLUE + out_msg + TextFormat.ENDC)
        self._write_to_file(out_msg)

    def warning(self, msg):
        out_msg = self._format_log(msg, Prefix.WARNING)
        print(TextFormat.WARNING + out_msg + TextFormat.ENDC)
        self._write_to_file(out_msg)

    def error(self, msg):
        out_msg = self._format_log(msg, Prefix.ERROR)
        print(TextFormat.FAIL + out_msg + TextFormat.ENDC)
        self._write_to_file(out_msg)



