#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# https://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------
import glob
import os
import shutil

from packaging.version import parse

import arch

##########################################################
# Copy Examples
##########################################################
root = os.path.split(os.path.abspath(__file__))[0]
example_path = os.path.join(root, "..", "..", "examples")
examples = glob.glob(os.path.join(example_path, "*.ipynb"))
for example in examples:
    _, filename = os.path.split(example)
    mod = filename.split("_")[0]
    target = os.path.join(root, mod, filename)
    shutil.copyfile(example, target)

# -- Project information -----------------------------------------------------

project = "arch"
copyright = "2021, Kevin Sheppard"
author = "Kevin Sheppard"

# More warnings
nitpicky = True

# The short X.Y version
full_version = parse(arch.__version__)
short_version = version = arch.__version__
if full_version.is_devrelease:
    release = f"v{full_version.base_version} (+{full_version.dev})"
else:
    release = short_version

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = "1.0"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
    # One of the next two only
    "sphinx.ext.napoleon",
    # "numpydoc",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.extlinks",
    "sphinx.ext.todo",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.coverage",
    "sphinx.ext.ifconfig",
    "sphinx.ext.githubpages",
    "IPython.sphinxext.ipython_console_highlighting",
    "IPython.sphinxext.ipython_directive",
    "nbsphinx",
    "sphinx_immaterial",
]

try:
    import sphinxcontrib.spelling  # noqa: F401
except ImportError as err:  # noqa: F841
    pass
else:
    extensions.append("sphinxcontrib.spelling")

spelling_word_list_filename = ["spelling_wordlist.txt", "names_wordlist.txt"]
spelling_ignore_pypi_package_names = True

suppress_warnings = ["ref.citation"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = [".rst", ".md"]
source_suffix = {".rst": "restructuredtext"}

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns: list[str] = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "colorful"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# Adds an HTML table visitor to apply Bootstrap table classes
html_theme = "sphinx_immaterial"
html_title = f"{project} {release}"
# sphinx_immaterial theme options
html_theme_options = {
    "icon": {"repo": "fontawesome/brands/github"},
    "site_url": "https://bashtage.github.io/arch/",
    "repo_url": "https://github.com/bashtage/arch/",
    "repo_name": "arch",
    "palette": {"primary": "blue", "accent": "indigo"},
    "globaltoc_collapse": True,
    "toc_title": "Contents",
    "version_dropdown": True,
    "version_info": [
        {
            "version": "https://bashtage.github.io/arch/",
            "title": "Release",
            "aliases": [],
        },
        {
            "version": "https://bashtage.github.io/arch/devel/",
            "title": "Development",
            "aliases": [],
        },
        {
            "title": "RTD (Release)",
            "version": "https://arch.readthedocs.io/",
            "aliases": [],
        },
    ],
    "toc_title_is_page_title": True,
    "social": [
        {
            "icon": "fontawesome/brands/github",
            "link": "https://github.com/bashtage/arch",
            "name": "Source on github.com",
        },
        {
            "icon": "fontawesome/brands/python",
            "link": "https://pypi.org/project/arch/",
        },
        {
            "icon": "fontawesome/solid/quote-left",
            "link": "https://doi.org/10.5281/zenodo.593254",
        },
    ],
}

html_favicon = "images/favicon.ico"
html_logo = "images/bw-logo.svg"
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["css/small_fixes.css"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don"t match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``["localtoc.html", "relations.html", "sourcelink.html",
# "searchbox.html"]``.
#
# html_sidebars = {}
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "searchbox.html", "localtoc.html"]
}

# If false, no module index is generated.
html_domain_indices = True

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "arch"

# -- Options for LaTeX output ------------------------------------------------
# latex_elements: dict[str, str] = {
# The paper size ("letterpaper" or "a4paper").
#
# "papersize": "letterpaper",
# The font size ("10pt", "11pt" or "12pt").
#
# "pointsize": "10pt",
# Additional stuff for the LaTeX preamble.
#
# "preamble": '',
# Latex figure (float) alignment
#
# "figure_align": "htbp",
# }

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "arch.tex", "arch Documentation", "Kevin Sheppard", "manual"),
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "arch", "arch Documentation", [author], 1)]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "arch",
        "arch Documentation",
        author,
        "arch",
        "ARCH models in Python",
        "Finance/Econometrics",
    ),
]

# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]

# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "statsmodels": ("https://www.statsmodels.org/dev", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy", None),
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
}

extlinks = {"issue": ("https://github.com/bashtage/arch/issues/%s", "GH%s")}


napoleon_google_docstring = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_attr_annotations = True
napoleon_preprocess_types = True
napoleon_use_param = True
napoleon_type_aliases = {
    "array-like": ":term:`array-like <array_like>`",
    "array_like": ":term:`array_like`",
    "Figure": "matplotlib.figure.Figure",
    "Axes": "matplotlib.axes.Axes",
    "AxesSubplot": "matplotlib.axes.Axes",
    "DataFrame": "pandas.DataFrame",
    "Series": "pandas.Series",
    "ndarray": "numpy.ndarray",
    "np.ndarray": "numpy.array",
    "pd.Series": "pandas.Series",
    "RandomState": "numpy.random.RandomState",
    "Generator": "numpy.random.Generator",
    "float64": "numpy.double",
    "numpy.float64": "numpy.double",
    "OptimizeResult": "scipy.optimize.OptimizeResult",
    "VarianceForecast": "arch.univariate.volatility.VarianceForecast",
    "CovarianceEstimator": "arch.covariance.kernel.CovarianceEstimator",
    "CovarianceEstimate": "arch.covariance.kernel.CovarianceEstimate",
    "VolatilityUpdater": "arch.univariate.recursions.VolatilityUpdater",
    "ARCHModel": "arch.univariate.base.ARCHModel",
    "ARCHModelResult": "arch.univariate.base.ARCHModelResult",
    "ARCHModelFixedResult": "arch.univariate.base.ARCHModelFixedResult",
}

numpydoc_use_autodoc_signature = True
numpydoc_xref_param_type = True
numpydoc_class_members_toctree = False
numpydoc_xref_aliases = {
    "array-like": ":term:`array-like <array_like>`",
    "array_like": ":term:`array_like`",
    "Figure": "matplotlib.figure.Figure",
    "Axes": "matplotlib.axes.Axes",
    "AxesSubplot": "matplotlib.axes.Axes",
    "DataFrame": "pandas.DataFrame",
    "Series": "pandas.Series",
    "ndarray": "numpy.ndarray",
    "np.ndarray": "numpy.array",
    "pd.Series": "pandas.Series",
    "RandomState": "numpy.random.RandomState",
    "Generator": "numpy.random.Generator",
    "float64": "numpy.double",
    "numpy.float64": "numpy.double",
    "OptimizeResult": "scipy.optimize.OptimizeResult",
    "VarianceForecast": "arch.univariate.volatility.VarianceForecast",
    "CovarianceEstimator": "arch.covariance.kernel.CovarianceEstimator",
    "CovarianceEstimate": "arch.covariance.kernel.CovarianceEstimate",
    "VolatilityUpdater": "arch.univariate.recursions.VolatilityUpdater",
    "ARCHModel": "arch.univariate.base.ARCHModel",
    "ARCHModelResult": "arch.univariate.base.ARCHModelResult",
    "ARCHModelFixedResult": "arch.univariate.base.ARCHModelFixedResult",
}
numpydoc_xref_ignore = {"type", "optional", "default"}

autosummary_generate = True
autoclass_content = "class"
