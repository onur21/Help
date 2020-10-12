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

project = 'helpPage'
copyright = '2020, MagNET'
author = 'MagNET'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

language = None

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

import sphinx_rtd_theme
html_logo = 'images/logo.png'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    'logo_only' : True,
    'display_version' : False,
}
# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

locale_dirs = ['locales/']   # path is example but recommended.
gettext_compact = False     # optional.

# The master toctree document.
master_doc = 'index'

# -- Extension configuration -------------------------------------------------
 
# add sourcecode to path
import sys, os
sys.path.insert(0, os.path.abspath('../src'))


############################
# SETUP THE RTD LOWER-LEFT #
############################
try:
   html_context
except NameError:
   html_context = dict()
html_context['display_lower_left'] = True
 
if 'REPO_NAME' in os.environ:
   REPO_NAME = os.environ['REPO_NAME']
else:
   REPO_NAME = ''
 
# SET CURRENT_LANGUAGE
if 'current_language' in os.environ:
   # get the current_language env var set by buildDocs.sh
   current_language = os.environ['current_language']
else:
   # the user is probably doing `make html`
   # set this build's current language to english
   current_language = 'tr'
    
# tell the theme which language to we're currently building
html_context['current_language'] = current_language
 

# POPULATE LINKS TO OTHER LANGUAGES
html_context['languages'] = [ ('Türkçe', '/' +REPO_NAME+ '/tr/main/')]
html_context['languages'].append( ('English', '/' +REPO_NAME+ '/en/main/') )
 
#languages = [lang.name for lang in os.scandir('locales') if lang.is_dir()]
#for lang in languages:
#   html_context['languages'].append( (lang, '/' +REPO_NAME+ '/' +lang+ '/main/') )

DOCS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(DOCS_DIR)

html_context['documents'] = [('MagNET','/' +REPO_NAME + '/tr/main')]
html_context['documents'].append(('MagNET-Sub','/'+REPO_NAME+'/magnet-sub/'))


   