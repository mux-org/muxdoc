muxdoc
======

``muxdoc`` is a Sphinx extension for standardizing the look and feel of all of
the `mux-org <https://github.com/mux-org>`_ documentation.

Install
-------
You can install ``muxdoc`` with ``pip``:

.. code:: bash

   pip install muxdoc

The source code is available on `Github <https://github.com/mux-org/muxdoc>`_.

Use
---
``muxdoc`` provides a full Sphinx configuration so only the project name and
extensions need to be specified in the Sphinx ``conf.py`` file:

.. code:: python

   project = 'project name'
   extensions = ['muxdoc']


``muxdoc`` overrides the following values in ``conf.py``:

* ``copyright`` :octicon:`arrow-right` ``'%Y, California Institute of Technology'``

``muxdoc`` adds entries to the following lists in ``conf.py``:

* ``extensions`` :octicon:`arrow-right` ``spinx.ext.todo``, ``sphinx_design``, 
  ``sphinx_copybutton``


Overriding default configuration values
---------------------------------------

.. todo::

   I think this is possible by defining a setup() function in the local conf.py?
