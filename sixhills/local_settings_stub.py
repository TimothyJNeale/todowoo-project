print("local_settings.py found. Apply local configurations.")

DEBUG = True
ALLOWED_HOSTS = []

# Add these lines to the bottom of the settings.py file

# try:
#     from .local_settings import *
#     print("local_settings.py found. Apply local configurations.")
# except ImportError:
#     print("local_settings.py not found. Make sure to create it for local configurations.")