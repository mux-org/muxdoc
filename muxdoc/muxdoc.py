import os
from pathlib import Path


MUXDOC_DIR = Path(__file__).expanduser().absolute().parent
MUXDOC_ASSETS_DIR = str(MUXDOC_DIR / 'assets')

print(MUXDOC_ASSETS_DIR)


def setup(app):

    # REMINDER
    # these values override whatever is set in conf!

    config = app.config

    config.project = 'mux'
    config.copyright = '%Y, California Institute of Technology'
    config.author = 'Andy Kee'

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

    
