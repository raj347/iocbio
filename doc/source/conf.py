# -*- coding: utf-8 -*-
#
# Iocbio documentation build configuration file, created by
# sphinx-quickstart on Wed Jan 13 15:17:37 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.pngmath', 'numpydoc',
              'sphinx.ext.intersphinx', 'sphinx.ext.coverage',
              'sphinx.ext.extlinks']
extensions.append('sphinx.ext.autosummary')

#import sphinx
#if sphinx.__version__ >= "0.7":
#    extensions.append('sphinx.ext.autosummary')
#else:
#    extensions.append('numpydoc.autosummary')
#    extensions.append('numpydoc.only_directives')


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'IOCBio'
copyright = u'2009-2010, Pearu Peterson'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# The full version, including alpha/beta/rc tags.
from iocbio.version import version as release
# The short X.Y version.
version = '.'.join(release.split ('.')[:2])

print version, release


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'
today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
default_role = 'autolink'

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = False

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

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

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_use_modindex = False

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'Iocbiodoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = 'a4'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'Iocbio.tex', u'IOCBio Documentation',
   u'Pearu Peterson', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

intersphinx_mapping = {'http://docs.python.org/dev': None}

extlinks = {'numpy': ('http://docs.scipy.org/doc/numpy/reference/generated/numpy.%s.html',
                      'numpy.'),
            'pythonlib': ('http://docs.python.org/library/%s.html',
                          '')}



import glob
autosummary_generate = glob.glob ('index.rst')# + glob.glob ('generated/*.rst')

os.makedirs('generated')

import types

def scan_for_autodoc(obj, prefix, cache=set([])):
    if not hasattr(obj, '__name__'):
        # objects with no name have no members
        return
    if isinstance(obj, types.ModuleType) and not obj.__name__.startswith(prefix):
        # skip external modules/packages
        print 'skipping',obj.__name__
        return
    if isinstance(obj, types.ModuleType):
        n = obj.__name__
    else:
        n = prefix + '.' + obj.__name__
        if not obj.__module__.startswith('iocbio'):
            # skip external classes
            return
    if n not in cache:
        yield n
        cache.add(n)
    prefix = n
    autodoc_names = getattr(obj, '__autodoc__',None)
    if autodoc_names is None:
        if isinstance(obj, (types.TypeType, types.ClassType)):
            autodoc_names = [name for name in dir(obj) if (not name.startswith ('_') or name in ['__init__'])]
        elif isinstance(obj, types.ModuleType):
            autodoc_names = getattr(obj, '__all__', [])
    if autodoc_names is None:
        return
    for name in autodoc_names:
        if not hasattr(obj, name):
            if isinstance(obj, types.ModuleType):
                exec 'import %s.%s' % (obj.__name__, name)
        member = getattr(obj, name)
        for n in scan_for_autodoc(member, prefix):
            if n not in cache:
                yield n
                cache.add(n)

import iocbio
f = open('generated/stubs.rst', 'w')
print>>f,'.. autosummary::'
print>>f,'  :toctree: .'
print>>f

for n in scan_for_autodoc(iocbio, 'iocbio'):
    sys.stdout.flush ()
    print>>f, '  ' + n
f.close ()
autosummary_generate.append('generated/stubs.rst')

from iocbio.optparse_gui import OptionParser
from iocbio.script_options import set_formatter
parent_path = os.path.abspath(os.path.dirname(iocbio.__file__))

scripts_info = {}

for root, dirs, files in os.walk(parent_path):
    if '.svn' in dirs: dirs.remove('.svn')
    if os.path.basename(root)=='scripts':
        for script in files:
            script_name = os.path.splitext(script)[0]
            package_name = '.'.join(root[len(os.path.dirname(parent_path))+1:].split(os.sep)[:-1])
            try:
                exec 'import %s.script_options as script_options' % (package_name)
            except ImportError, msg:
                print msg
                continue
            try:
                set_options = getattr (script_options, 'set_%s_options' % (script_name))
            except AttributeError, msg:
                print msg
                continue
            parser = OptionParser()
            set_formatter (parser)
            parser.add_option('--no-gui', action='store_false', default=True, help='Run script without opening GUI.')
            set_options (parser)
            parser.prog = 'iocbio.%s' % (script_name)
            if parser.description is None:
                print 'Warning: %s does not have a description (use parser.set_description in %s.script_options.%s)' % (parser.prog, package_name,set_options.__name__)
                parser.description = 'PFI'

            descr = parser.get_description()
            descr_title = descr.lstrip().split('\n')[0]
            help = parser.format_help()
            help += '''
See also
========
:mod:`%s`
''' % (package_name)
            scripts_info[parser.prog] = dict(
                name = script_name,
                descr_title = descr_title,
                help = help)


name_len = 0
descr_len = 0
for script_name in sorted(scripts_info):
    info = scripts_info[script_name]
    f = open('generated/%s.rst' % (script_name.replace('.','-')), 'w')
    f.write('.. _%s:\n\n' % (script_name.replace('.','-')))
    f.write('%s\n%s\n%s\n' % ('-'*len (script_name), script_name, '-'*len (script_name)))
    f.write ('%s\n' % (info['help']))
    f.close()
    name_len = max (name_len, len(script_name))
    descr_len = max (descr_len, len(info['descr_title']))


f = open('generated/scripts.rst', 'w')
f.write('''
GUI scripts
===========
''')

name_len += 7
row_fmt = '| %%%ss | %%%ss |\n' % (name_len, descr_len)
name_len += 2
descr_len += 2
for script_name in sorted(scripts_info):
    info = scripts_info[script_name]
    script_ref = ':ref:`%s`' % (script_name.replace('.','-'))
    f.write('+%s+%s+\n' % ('-'*name_len, '-'*descr_len))
    f.write (row_fmt % (script_ref, info['descr_title']))
f.write('+%s+%s+\n' % ('-'*name_len, '-'*descr_len))
f.close()

#sys.exit(0)
