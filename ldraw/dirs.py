""" data and config directories """

from platformdirs import user_data_dir, user_config_dir, user_cache_dir

from ldraw.utils import ensure_exists

PYLDRAW = 'pyldraw'

def get_data_dir():
    """ get the directory where to put some data """
    return ensure_exists(user_data_dir(PYLDRAW))


def get_config_dir():
    """ get the directory where the config is """
    return ensure_exists(user_config_dir(PYLDRAW))


def get_cache_dir():
    return ensure_exists(user_cache_dir(PYLDRAW))
