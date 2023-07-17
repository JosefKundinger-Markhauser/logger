
from Logger.Logger import Logger

logger = Logger(debug=True)

logger.log_header("Test Header\nHeader second line")
logger.log("Test Log")
logger.debug("Test Debug")
logger.warning("Test Warning")
logger.error("Test Error")

