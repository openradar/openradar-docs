# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'openradar'
copyright = '2022, Open Radar Community'
author = 'Open Radar Community'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx_design']

templates_path = ['_templates']
exclude_patterns = []

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_context = {
    "default_mode": "dark"
}
html_logo = "_static/openradar_logo.svg"

# Add some more theme Options
html_theme_options = {
    "header_links_before_dropdown": 4,
    "show_toc_level": 1,
    'github_url': 'https://github.com/openradar/openradar-docs',
    'search_bar_text': 'Search this site... ',
    "navbar_align": "left",
    #'google_analytics_id': 'UA-196809533-1',
    "navbar_end": ["theme-switcher", "icon-links.html"],
    "favicons": [
        {
            "rel": "icon",
            "href": "openradar_micro.svg",
        },
    ],
    "logo": {
        "link": "https://openradarscience.org",
    },
    "icon_links": [
        {
            "type": "local",
            "name": "OpenRadarScience",
            "url": "https://openradarscience.org",
            "icon": "_static/openradar_mini.svg",
        },
    ],
}
