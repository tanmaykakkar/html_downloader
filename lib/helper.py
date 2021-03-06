def config_logging(filehandler=False):
    """Configure basic logging as per setting"""
    import logging
    import settings

    handlers = [logging.StreamHandler()]
    if filehandler:
        handlers += [logging.FileHandler(settings.LOG_FILE)]

    logging.basicConfig(
            level=settings.LOG_LEVEL,
            format=settings.LOG_FORMAT,
            handlers=handlers
    )
