import logging
# configure logging
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s -%(message)s',
    filename = 'app.log', #log to file
    filemode = 'a' # Append mode
)

# Different log levels
logging.debug("Detailed debug information")
logging.info("something happened")
logging.warning("something unexpected")
logging.error("something failed")
logging.critical("Program can not continue")