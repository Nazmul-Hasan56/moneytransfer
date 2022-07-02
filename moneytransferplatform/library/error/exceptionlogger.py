def logException(logger, exception, errorMessage):
	logger.error(exception, exc_info=True)
	logger.error(errorMessage)
