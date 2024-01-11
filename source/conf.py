# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'DashboardUtilsDataScience'
copyright = '2024, Rajat Mishra'
author = 'Rajat Mishra'

# The full version, including alpha/beta/rc tags
release = '1.25'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx_jinja',"myst_parser"]

jinja_contexts = {
    'first_ctx': {'topics': {'a': 'b', 'c': 'd'}}
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []
jinja_env_kwargs = {
    'lstrip_blocks': True,
}

jinja_filters = {
    'bold': lambda value: f'**{value}**',
}

jinja_tests = {
    'instanceof': lambda value, type: isinstance(value, type),
}

jinja_globals = {
    'list': list,
}

jinja_policies = {
    'compiler.ascii_str': False,
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']