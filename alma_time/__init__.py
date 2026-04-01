from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("your_package_name")
except PackageNotFoundError:
    # package is not installed
    __version__ = "0.0.0.dev0"

from .alma_time import *
