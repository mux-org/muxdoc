import ast
import glob
import os
from pathlib import Path

from .util import dump_openapi


MUXDOC_DIR = Path(__file__).expanduser().absolute().parent
MUXDOC_ASSETS_DIR = str(MUXDOC_DIR / 'assets')

print(MUXDOC_ASSETS_DIR)


def _read_muxdoc_openapi(conf_path):
    """Return the ``muxdoc_openapi`` dict literal from a conf.py, or None.

    The file is parsed with ast (never executed), so reading a container's
    declaration during the aggregate build has no import side effects and does
    not require the container's deps to merely discover it.
    """
    tree = ast.parse(Path(conf_path).read_text())
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == 'muxdoc_openapi'
            for t in node.targets
        ):
            return ast.literal_eval(node.value)
    return None


def _generate_openapi(app):
    """Generate openapi.yaml for every container that declares one in conf.py.

    A container opts in by setting ``muxdoc_openapi = {"app": ..., "app_dir":
    ...}`` in its docs ``conf.py``. We discover conf.py files anywhere under the
    source tree, so this works both for a standalone container build (srcdir is
    the container's ``docs/``) and for the aggregate build (srcdir is the repo
    root, with each container's conf.py at ``containers/*/docs/conf.py``).
    """
    # glob (unlike pathlib.rglob) follows symlinked directories, which the
    # containers/ entries are during local builds (see the docs Makefile).
    pattern = os.path.join(app.srcdir, '**', 'conf.py')
    for match in glob.glob(pattern, recursive=True):
        cfg = _read_muxdoc_openapi(match)
        if not cfg:
            continue
        confdir = Path(match).parent
        app_dir = (confdir / cfg.get('app_dir', '.')).resolve()
        out = (confdir / cfg.get('out', 'openapi.yaml')).resolve()
        dump_openapi(app=cfg['app'], app_dir=str(app_dir), out=str(out))


def setup(app):
    app.connect('builder-inited', _generate_openapi)

    config = app.config

    # REMINDER
    # these values override whatever is set in conf!
    # to define, add a setup() function in your conf.py
    config.extensions.append('sphinx.ext.autodoc')
    config.extensions.append('sphinx.ext.todo')
    config.extensions.append('sphinx_design')
    config.extensions.append('sphinx_copybutton')
    config.extensions.append('sphinxcontrib.openapi')

    config.templates_path = ['_templates']
    config.exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

    config.suppress_warnings.append('toc.not_included')

    config.html_static_path = [MUXDOC_ASSETS_DIR]
    config.html_css_files = ['css/mux.css']

    config.html_theme = 'pydata_sphinx_theme'
    config.html_theme_options = {}
    config.html_theme_options['show_prev_next'] = False
    config.html_theme_options['github_url'] = 'https://github.com/mux-org'
    config.html_theme_options['logo'] = {
        'link': 'index',
        'image_light': os.path.join(MUXDOC_ASSETS_DIR, 'logo/mux_light.svg'),
        'image_dark': os.path.join(MUXDOC_ASSETS_DIR, 'logo/mux_dark.svg'),
    }
    config.html_theme_options['pygments_light_style'] = 'friendly'
    config.html_theme_options['pygments_dark_style'] = 'material'
    config.html_theme_options['secondary_sidebar_items'] = {
        '**': ['page-toc'],
        'docs/index': []
    }

    config.html_show_sphinx = False
    config.html_show_sourcelink = False
    config.html_scaled_image_link = False

    
