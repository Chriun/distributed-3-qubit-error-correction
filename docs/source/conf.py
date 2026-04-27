# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DQC'
copyright = '2026, DQC'
author = 'Christopher Poon'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.mathjax",
]

master_doc = "index"

exclude_patterns = []

numfig = True
math_numfig = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "sphinx_rtd_theme"

html_static_path = ['_static']

html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "Chriun", # Username
    "github_repo": "distributed-3-qubit-error-correction", # Repo name
    "github_version": "main", # Version
    "conf_py_path": "/docs/source/", # Path in the checkout to the docs root
}

latex_elements = {
    'preamble': r'''
    \usepackage{amsmath}
    \usepackage{braket}
    \usepackage{algorithm}
    \usepackage{algorithmic}
    '''
}
