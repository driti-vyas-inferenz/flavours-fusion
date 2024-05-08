try:
    # Loads production configurations for production server.
    from .production import *
except:
    # Loads local server configurations.
    from .local import *