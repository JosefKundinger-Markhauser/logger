import os
from datetime import datetime

"""
%a: Returns the first three characters of the weekday, e.g. Wed.
%A: Returns the full name of the weekday, e.g. Wednesday.
%B: Returns the full name of the month, e.g. September.
%w: Returns the weekday as a number, from 0 to 6, with Sunday being 0.
%m: Returns the month as a number, from 01 to 12.
%p: Returns AM/PM for time.
%y: Returns the year in two-digit format, that is, without the century. For example, "18" instead of "2018".
%f: Returns microsecond from 000000 to 999999.
%Z: Returns the timezone.
%z: Returns UTC offset.
%j: Returns the number of the day in the year, from 001 to 366.
%W: Returns the week number of the year, from 00 to 53, with Monday being counted as the first day of the week.
%U: Returns the week number of the year, from 00 to 53, with Sunday counted as the first day of each week.
%c: Returns the local date and time version.
%x: Returns the local version of date.
%X: Returns the local version of time.
"""


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
        self.frame_width = 80

    def _format_log(self, msg, prefix):
        timestamp = self.get_timestamp()
        return f"{timestamp}---{prefix:8}{Prefix.SEPERATOR:3}{msg}"

    def _write_to_file(self, msg):
        if self._log_dir is None:
            return
        if self._log_file_name is None:
            self._log_file_name = self.get_timestamp().replace(":", "_")\
                .replace(" ", "_").replace("/", "_")
        full_path = os.path.join(self._log_dir, self._log_file_name)
        try:
            with open(full_path, "a") as f:
                f.write(msg + "\n")
                f.close()
        except Exception as e:
            print(str(e))

    def _get_line(self):
        return "|" + ("-" * self.frame_width) + "|"

    def get_timestamp(self):
        if self._timestamp_format is not None:
            timestamp = datetime.now().strftime(self._timestamp_format)
        else:
            timestamp = str(datetime.now())
        return timestamp
    
    def log_header(self, msg):
        outputs = msg.split('\n')
        header = self._get_line() + "\n"
        for out in outputs:
            header += f"|{TextFormat.BOLD}{out.center(self.frame_width)}{TextFormat.ENDC}|\n"
        header += self._get_line() + "\n"
        print(header)
        self._write_to_file(header)

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



