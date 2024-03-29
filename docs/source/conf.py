# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Aucbot'
copyright = '2024'
author = 'Khawer'

release = '0.1'
version = '2.6'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']
html_static_path = ["_static"]
templates_path = ['_templates']


# -- Options for HTML output
html_css_files = [
    'docs/source/_static/rtd_dark.css',
]
default_dark_mode = True
html_theme = 'sphinx_rtd_theme'
# -- Options for EPUB output
epub_show_urls = 'footnote'
