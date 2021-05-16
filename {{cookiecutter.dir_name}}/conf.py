#  {{ cookiecutter.project_name }} documentation created by {{ cookiecutter.author_name }} on {% now 'utc', '%d.%m.%Y' %}
#  using ThetaDev's cookiecutter sphinx template V1
#
#  This configuration file holds the settings for your Sphinx documentation
#  For further information, see here:
#  https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- PROJECT INFO -------------------------------------------------------------

project = '{{ cookiecutter.project_name }}'
copyright = '{% now 'utc', '%Y' %}, {{ cookiecutter.author_name }}'
author = '{{ cookiecutter.author_name }}'

# Document language ('en' / 'de')
# used for certain text components like Contents/Inhalt
language = '{{ cookiecutter.language }}'


# -- MAIN CONFIGURATION -------------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autosectionlabel",
    # "sphinx.ext.autodoc"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['*/*', 'Thumbs.db', '.DS_Store']

# Pygments-Styling used for code syntax highlighting.
# See this page for an overview of all styles including live demo:
# https://pygments.org/demo/
pygments_style = "vs"

autodoc_default_options = {
    'member-order': 'bysource',
    'undoc-members': True,
}

autosectionlabel_prefix_document = True


# -- IMPORT DIRECTORIES -------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
'''
import os
import sys
sys.path.append(os.path.abspath('../'))
'''

# -- OUTPUT: HTML -------------------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_title = project

html_theme = "furo"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# furo theming
html_theme_options = {
    "navigation_with_keys": True,
}
