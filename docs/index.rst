muxdoc
======

``muxdoc`` is a Sphinx extension for simplifying Sphinx configuration for
the `mux-org <https://github.com/mux-org>`_ documentation.

Install
-------
Install ``muxdoc`` with ``pip``:

.. code:: bash

   pip install muxdoc

The source code is available on `Github <https://github.com/mux-org/muxdoc>`_.

Use
---
``muxdoc`` provides a full Sphinx configuration so a minimally compliant
Sphinx ``conf.py`` file looks like this:

.. code:: python

   project = 'project name'
   author = 'author name'
   copyright = 'copyright message'
   extensions = ['muxdoc']


Default configuration
---------------------

``app.config``
~~~~~~~~~~~~~~

``templates_path``
   ``['_templates']``
``exclude_patterns``
   ``['_build', 'Thumbs.db', '.DS_Store']``
``html_static_path``
   ``assets/``
``html_css_files``
   ``['css/mux.css']``
``html_theme``
   ``'pydata_sphinx_theme'``
``html_show_sphinx``
   ``False``
``html_show_sourcelink``
   ``False``
``html_scaled_image_link``
   ``False``
``extensions``
   ``sphinx.ext.autodoc``, ``sphinx.ext.todo``, ``sphinx_design``,
   ``sphinx_copybutton``, ``sphinxcontrib.openapi``
``suppress_warnings``
   ``[toc.not_included]``


``app.config.html_theme_options``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   ``html_theme_options`` is a dict

``show_prev_next``
   ``False``
``github_url``
   ``'https://github.com/mux-org'``
``logo``
   the mux light/dark logos, linked to ``index``
``pygments_light_style``
   ``'friendly'``
``pygments_dark_style``
   ``'material'``
``secondary_sidebar_items``
   ``{'**': ['page-toc'], 'docs/index': []}``


Overriding default configuration
--------------------------------
To override a ``muxdoc`` default value, define a ``setup()`` function in your local
``conf.py``. Sphinx calls it *after* all extensions have been set up, so any
value assigned there takes precedence:

.. code:: python

   project = 'project name'
   author = 'author name'
   copyright = 'copyright message'
   extensions = ['muxdoc']

   def setup(app):
       # override a value set by muxdoc
       app.config.html_show_sourcelink = True

       # add to a list/dict without discarding muxdoc's entries
       app.config.html_css_files.append('css/custom.css')
       app.config.html_theme_options['show_prev_next'] = True


