__version__ = '1.0.4'

from muxdoc.util import dump_openapi

def setup(app, *args, **kwargs):
    from .muxdoc import setup

    return setup(app, *args, **kwargs)
