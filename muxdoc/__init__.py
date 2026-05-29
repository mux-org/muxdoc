__version__ = '1.0.1'


def setup(app, *args, **kwargs):
    from .muxdoc import setup

    return setup(app, *args, **kwargs)
