# -*- coding: utf-8 -*-

import os
import sys
import sphinx_bootstrap_theme

# only needed for Autobahn|Python
sys.path.insert(0, os.path.abspath('./_extensions'))
sys.path.insert(0, os.path.abspath('..'))

extensions = [
   'sphinx.ext.autodoc',
   'sphinx.ext.doctest',
   'sphinx.ext.intersphinx',
   'sphinx.ext.viewcode',
   'sphinx.ext.ifconfig',
   'sphinx.ext.todo',
   'sphinxcontrib.spelling',
   'txsphinx' # only needed for Autobahn|Python
]

spelling_lang = 'en_US'
spelling_show_suggestions = False
spelling_word_list_filename = 'spelling_wordlist.txt'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'AutobahnPython'
copyright = u'Tavendo GmbH'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
init = {}
with open(os.path.join(base_dir, "autobahn", "__init__.py")) as f:
   exec(f.read(), init)

version = release = init["__version__"]


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'work']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

## Sphinx-Bootstrap Theme
##
## http://sphinx-bootstrap-theme.readthedocs.org/en/latest/README.html
##
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

html_theme_options = {
    # Navigation bar title. (Default: ``project`` value)
    'navbar_title': " ",

    # Tab name for entire site. (Default: "Site")
    'navbar_site_name': "Site",

    # A list of tuples containing pages or urls to link to.
    # Valid tuples should be in the following forms:
    #    (name, page)                 # a link to a page
    #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
    #    (name, "http://example.com", True) # arbitrary absolute url
    # Note the "1" or "True" value above as the third argument to indicate
    # an arbitrary url.
    'navbar_links': [
        #("Examples", "examples"),
        #("Link", "http://example.com", True),
    ],

    # Render the next and previous page links in navbar. (Default: true)
    'navbar_sidebarrel': True,

    # Render the current pages TOC in the navbar. (Default: true)
    'navbar_pagenav': True,

    # Tab name for the current pages TOC. (Default: "Page")
    #'navbar_pagenav_name': "Page",

    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    'globaltoc_depth': 1,

    # Include hidden TOCs in Site navbar?
    #
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    #
    # Values: "true" (default) or "false"
    'globaltoc_includehidden': "true",

    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    #'navbar_class': "navbar navbar-inverse",
    'navbar_class': "navbar",

    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "true",

    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    'source_link_position': "nav",

    # Bootswatch (http://bootswatch.com/) theme.
    #
    # Options are nothing with "" (default) or the name of a valid theme
    # such as "amelia" or "cosmo".
    'bootswatch_theme': "",

    # Choose Bootstrap version.
    # Values: "3" (default) or "2" (in quotes)
    'bootstrap_version': "3",
}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


## additional variables which become accessible in RST (e.g. .. ifconfig:: not no_network)
##
def setup(app):
   app.add_config_value('no_network', False, True)

no_network = None

## additional variables which become accessible in the template engine's
## context for all pages
##
html_context = {
   #'widgeturl': 'https://demo.crossbar.io/clandeckwidget'
   #'widgeturl': 'http://127.0.0.1:8090/widget'
   'widgeturl': None,
   'no_network': False,
   #'cstatic': 'http://127.0.0.1:8888',
   'cstatic': '//tavendo-common-static.s3-eu-west-1.amazonaws.com',
}

# (Optional) Logo. Should be small enough to fit the navbar (ideally 24x24).
# Path should be relative to the ``_static`` files directory.
html_logo = None


# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
   '**': [
      'side-primary.html'
   ]
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'AutobahnPython'


# http://sphinx-doc.org/ext/intersphinx.html
intersphinx_mapping = {
   'py2': ('http://docs.python.org/2', None),
   'py3': ('http://docs.python.org/3', None),
   'six': ('https://pythonhosted.org/six/', None),
}

rst_epilog = """
.. |ab| replace:: Autobahn
.. |Ab| replace:: **Autobahn**
.. |abL| replace:: Autobahn|Python
.. |AbL| replace:: **Autobahn**\|Python
.. _Autobahn: http://autobahn.ws
.. _AutobahnJS: http://autobahn.ws/js
.. _AutobahnPython: **Autobahn**\|Python
.. _WebSocket: http://tools.ietf.org/html/rfc6455
.. _RFC6455: http://tools.ietf.org/html/rfc6455
.. _WAMP: http://wamp.ws/
.. _Twisted: http://twistedmatrix.com/
.. _asyncio: http://docs.python.org/3.4/library/asyncio.html
.. _CPython: http://python.org/
.. _PyPy: http://pypy.org/
.. _Jython: http://jython.org/
.. _WAMP: http://wamp.ws/
.. _WAMPv1: http://wamp.ws/spec/wamp1/
.. _WAMPv2: https://github.com/wamp-proto/wamp-proto/blob/master/spec/README.md
.. _AutobahnTestsuite: http://autobahn.ws/testsuite
.. _trollius: https://pypi.python.org/pypi/trollius/
.. _tulip: https://pypi.python.org/pypi/asyncio/
"""

rst_prolog = """
"""

# http://stackoverflow.com/questions/5599254/how-to-use-sphinxs-autodoc-to-document-a-classs-init-self-method
autoclass_content = 'both'

autodoc_member_order = 'bysource'
