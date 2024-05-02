
from logger.logger import Logger

logger = Logger(debug=True, log_dir='log_dir', log_file_name='log_file')

logger.log_header("Test Header")
logger.log("Test Log")
logger.debug("Test Debug")
logger.warning("Test Warning")
logger.error("Test Error")

