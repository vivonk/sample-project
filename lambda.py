import time
import logger
logger(time.time(), logger.INFO)

# last commit would make it easy to understand

try:
    import pip.req.internal
except ImportError:
    import pip._internal

logger.info("pip version will set to latest")
# exceptions are added to the version parsing
text = parse_requirement("/home/vivonk/aws/parsing_config.txt")
logger.warn("parsing have following requirements\n%s" % text)
