import time
import logger
logger(time.time(), logger.INFO)

# last commit would make it easy to understand

try:
    import pip.req.internal
except ImportError:
    import pip._internal

logger.info("pip version will set to latest")
