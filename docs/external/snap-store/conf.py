import datetime
import ast
import logging
import os
from os import environ
import yaml
import sys

sys.path.append(os.path.abspath("./_ext"))
logger = logging.getLogger()

# Configuration for the Sphinx documentation builder.
# All configuration specific to your project should be done in this file.
#
# If you're new to Sphinx and don't want any advanced or custom features,
# just go through the items marked 'TODO'.
#
# A complete list of built-in Sphinx configuration values:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# Our starter pack uses the custom Canonical Sphinx extension
# to keep all documentation based on it consistent and on brand:
# https://github.com/canonical/canonical-sphinx


#######################
# Project information #
#######################

# Project name
#
# TODO: Update with the official name of your project or product

html_title = full_title = project = 'Dedicated Snap Store'
author = "Canonical Ltd."

# Sidebar documentation title; best kept reasonably short
#
# TODO: To include a version number, add it here (hardcoded or automated).
#
# TODO: To disable the title, set to an empty string.


# Copyright string; shown at the bottom of the page
#
# Now, the starter pack uses CC-BY-SA as the license
# and the current year as the copyright year.
#
# TODO: If your docs need another license, specify it instead of 'CC-BY-SA'.
#
# TODO: If your documentation is a part of the code repository of your project,
#       it inherits the code license instead; specify it instead of 'CC-BY-SA'.
#
# NOTE: For static works, it is common to provide the first publication year.
#       Another option is to provide both the first year of publication
#       and the current year, especially for docs that frequently change,
#       e.g. 2022–2023 (note the en-dash).
#
#       A way to check a repo's creation date is to get a classic GitHub token
#       with 'repo' permissions; see https://github.com/settings/tokens
#       Next, use 'curl' and 'jq' to extract the date from the API's output:
#
#       curl -H 'Authorization: token <TOKEN>' \
#         -H 'Accept: application/vnd.github.v3.raw' \
#         https://api.github.com/repos/canonical/<REPO> | jq '.created_at'

copyright = "%s CC-BY-SA, %s" % (datetime.date.today().year, author)


# Documentation website URL
#
# TODO: Update with the official URL of your docs or leave empty if unsure.
#
# NOTE: The Open Graph Protocol (OGP) enhances page display in a social graph
#       and is used by social media platforms; see https://ogp.me/

ogp_site_url = "https://canonical-canonical-brand-store.readthedocs-hosted.com/"


# Preview name of the documentation website
#
# TODO: To use a different name for the project in previews, update as needed.

ogp_site_name = project


# Preview image URL
#
# TODO: To customise the preview image, update as needed.

ogp_image = "https://assets.ubuntu.com/v1/253da317-image-document-ubuntudocs.svg"


# Product favicon; shown in bookmarks, browser tabs, etc.

# TODO: To customise the favicon, uncomment and update as needed.

#html_favicon = '.sphinx/_static/favicon.png'


# Dictionary of values to pass into the Sphinx context for all pages:
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_context

html_context = {
    # Product page URL; can be different from product docs URL
    #
    # TODO: Change to your product website URL,
    #       dropping the 'https://' prefix, e.g. 'ubuntu.com/lxd'.
    #
    # TODO: If there's no such website,
    #       remove the {{ product_page }} link from the page header template
    #       (usually .sphinx/_templates/header.html; also, see README.rst).
    "product_page": "documentation.ubuntu.com",
    # Product tag image; the orange part of your logo, shown in the page header
    #
    # TODO: To add a tag image, uncomment and update as needed.
    # 'product_tag': '_static/tag.png',
    # Your Discourse instance URL
    #
    # TODO: Change to your Discourse instance URL or leave empty.
    #
    # NOTE: If set, adding ':discourse: 123' to an .rst file
    #       will add a link to Discourse topic 123 at the bottom of the page.
    "discourse": "https://discourse.ubuntu.com",
    # Your Mattermost channel URL
    #
    # TODO: Change to your Mattermost channel URL or leave empty.
    "mattermost": "https://chat.canonical.com/canonical/channels/documentation",
    # Your Matrix channel URL
    #
    # TODO: Change to your Matrix channel URL or leave empty.
    "matrix": "https://matrix.to/#/#documentation:ubuntu.com",
    # Your documentation GitHub repository URL
    #
    # TODO: Change to your documentation GitHub repository URL or leave empty.
    #
    # NOTE: If set, links for viewing the documentation source files
    #       and creating GitHub issues are added at the bottom of each page.
    'github_url': 'https://github.com/canonical/brand-store-documentation',
    # Docs branch in the repo; used in links for viewing the source files
    #
    # TODO: To customise the branch, uncomment and update as needed.
    'repo_default_branch': 'main',
    # Docs location in the repo; used in links for viewing the source files
    #


    # TODO: To customise the directory, uncomment and update as needed.
    "repo_folder": "/docs/",
    # TODO: To enable or disable the Previous / Next buttons at the bottom of pages
    # Valid options: none, prev, next, both
    # "sequential_nav": "both",
    # TODO: To enable listing contributors on individual pages, set to True
    "display_contributors": False,

    # Required for feedback button    
    'github_issues': 'enabled',
}

# Project slug; see https://meta.discourse.org/t/what-is-category-slug/87897
#
# TODO: If your documentation is hosted on https://docs.ubuntu.com/,
#       uncomment and update as needed.

slug = 'dedicated-snap-store'


# Template and asset locations

html_static_path = [".sphinx/_static"]
templates_path = [".sphinx/_templates"]


#############
# Redirects #
#############

# To set up redirects: https://documatt.gitlab.io/sphinx-reredirects/usage.html
# For example: 'explanation/old-name.html': '../how-to/prettify.html',

# To set up redirects in the Read the Docs project dashboard:
# https://docs.readthedocs.io/en/stable/guides/redirects.html

# NOTE: If undefined, set to None, or empty,
#       the sphinx_reredirects extension will be disabled.

redirects = {}


###########################
# Link checker exceptions #
###########################

# A regex list of URLs that are ignored by 'make linkcheck'
#
# TODO: Remove or adjust the ACME entry after you update the contributing guide

linkcheck_ignore = [
    'http://127.0.0.1:8000',
    'https://dashboard.snapcraft.io/reviewer/{{CUSTOMER_STORE_ID}}/',
    'https://readthedocs.com/projects/*',
    'https://canonical-canonical-brand-store.readthedocs-hosted.com/*',
    'https://canonical-brand-store-acme-alpha.readthedocs-hosted.com/*',
    'https://canonical-canonical-alliances-demo-brand-store.readthedocs-hosted.com/*',
    'https://ubuntu.com/core/docs/gadget-snaps#heading--gadget',
    'https://ubuntu.com/core/services/guide/signing-keys#heading--key-roles',
    'https://portal.support.canonical.com',
    'https://dashboard.snapcraft.io/snaps/{{CUSTOMER_STORE_PREFIX}}-pc/',
    'https://dashboard.snapcraft.io/dev/store/{{CUSTOMER_STORE_ID}}/permissions/',
    'https://github.com/canonical/hsm-assertion-signing-reference',
    'http://support.canonical.com/',
    'https://snapcraft.io/docs/channels',
    
]


# A regex list of URLs where anchors are ignored by 'make linkcheck'

linkcheck_anchors_ignore_for_url = [
    r"https://canonical-serial-vault.readthedocs-hosted.com/serial-vault/signing-keys",
    r"https://documentation.ubuntu.com/dedicated-snap-store/how-to/setting-up-account-roles/"
]

# give linkcheck multiple tries on failure
# linkcheck_timeout = 30
linkcheck_retries = 3

########################
# Configuration extras #
########################

# Custom MyST syntax extensions; see
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
#
# NOTE: By default, the following MyST extensions are enabled:
#       substitution, deflist, linkify

myst_enable_extensions = {
    "attrs_inline",
}


# Custom Sphinx extensions; see
# https://www.sphinx-doc.org/en/master/usage/extensions/index.html

# NOTE: The canonical_sphinx extension is required for the starter pack.
#       It automatically enables the following extensions:
#       - custom-rst-roles
#       - myst_parser
#       - notfound.extension
#       - related-links
#       - sphinx_copybutton
#       - sphinx_design
#       - sphinx_reredirects
#       - sphinx_tabs.tabs
#       - sphinxcontrib.jquery
#       - sphinxext.opengraph
#       - terminal-output
#       - youtube-links

extensions = [
    "canonical_sphinx",
    "sphinxcontrib.cairosvgconverter",
    "sphinx_last_updated_by_git",
    "rstjinja",
    "better-term",
]

# Excludes files or directories from processing

exclude_patterns = []

# Adds custom CSS files, located under 'html_static_path'

# html_css_files = [
#     "css/pdf.css",
# ]


# Adds custom JavaScript files, located under 'html_static_path'

# html_js_files = []


# Specifies a reST snippet to be appended to each .rst file

rst_epilog = """
.. include:: /reuse/links.txt
"""

# Feedback button at the top; enabled by default
#
# TODO: To disable the button, uncomment this.

# disable_feedback_button = True


# Your manpage URL
#
# TODO: To enable manpage links, uncomment and update as needed.
#
# NOTE: If set, adding ':manpage:' to an .rst file
#       adds a link to the corresponding man section at the bottom of the page.

# manpages_url = f'https://manpages.ubuntu.com/manpages/{codename}/en/' + \
#     f'man{section}/{page}.{section}.html'


# Specifies a reST snippet to be prepended to each .rst file
# This defines a :center: role that centers table cell content.
# This defines a :h2: role that styles content for use with PDF generation.

rst_prolog = """
.. role:: center
   :class: align-center
.. role:: h2
    :class: hclass2
.. role:: woke-ignore
    :class: woke-ignore
.. role:: vale-ignore
    :class: vale-ignore
"""

# Workaround for https://github.com/canonical/canonical-sphinx/issues/34

if "discourse_prefix" not in html_context and "discourse" in html_context:
    html_context["discourse_prefix"] = html_context["discourse"] + "/t/"


# Templating

with open("templates/TEMPLATE.yaml") as template_file:
    template_values = yaml.safe_load(template_file)

template_path = os.environ.get("TEMPLATE_FILENAME", "NONE")

try:
    if environ['TEMPLATE'] != "NONE":
        template_path = environ['TEMPLATE']
except LookupError:
    print("No template variable set. Assuming RTD build.")
    pass

try:
    with open(template_path) as template_file:
        template_values = yaml.safe_load(template_file)
except FileNotFoundError:
    logger.error(f"Template {template_path} not found")
    # Then fall back to the defaults

html_context = {**html_context, **template_values}

# PDF generation

latex_documents = [  ('pdf-index', 'UC24_Onboarding_Guide.tex', u'UC24 Onboarding Guide', u'Canonical', 'manual'),]

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'fncychap': '',
    'preamble': r'''
%\usepackage{charter}
%\usepackage[defaultsans]{lato}
%\usepackage{inconsolata}
\setmainfont[UprightFont = *-R, BoldFont = *-B, ItalicFont=*-RI, Extension = .ttf]{Ubuntu}
\setmonofont[UprightFont = *-R, BoldFont = *-B, ItalicFont=*-RI, Extension = .ttf]{UbuntuMono}
\usepackage[most]{tcolorbox}
\tcbuselibrary{breakable}
\usepackage{lastpage}
\usepackage{tabto}
\usepackage{ifthen}
\usepackage{etoolbox}
\usepackage{fancyhdr}
\usepackage{graphicx}
\usepackage{titlesec}
\usepackage{fontspec}
\usepackage{tikz}
\usepackage{changepage}
\usepackage{array}
\usepackage{tabularx}
\graphicspath{ {../../.sphinx/images/} }
\definecolor{yellowgreen}{RGB}{154, 205, 50}
\definecolor{title}{RGB}{76, 17, 48}
\definecolor{subtitle}{RGB}{116, 27, 71}
\definecolor{label}{RGB}{119, 41, 100}
\definecolor{copyright}{RGB}{174, 167, 159}
\makeatletter
\def\tcb@finalize@environment{%
  \color{.}% hack for xelatex
  \tcb@layer@dec%
}
\makeatother
\newenvironment{sphinxclassprompt}{\color{yellowgreen}\setmonofont[Color = 9ACD32, UprightFont = *-R, Extension = .ttf]{UbuntuMono}}{}
\tcbset{enhanced jigsaw, colback=black, fontupper=\color{white}}
\newtcolorbox{termbox}{use color stack, breakable, colupper=white, halign=flush left}
\newenvironment{sphinxclassterminal}{\setmonofont[Color = white, UprightFont = *-R, Extension = .ttf]{UbuntuMono}\sphinxsetup{VerbatimColor={black}}\begin{termbox}}{\end{termbox}}
\newcommand{\dimtorightedge}{%
  \dimexpr\paperwidth-1in-\hoffset-\oddsidemargin\relax}
\newcommand{\dimtotop}{%
  \dimexpr\height-1in-\voffset-\topmargin-\headheight-\headsep\relax}
\newtoggle{tpage}
\AtBeginEnvironment{titlepage}{\global\toggletrue{tpage}}
\fancypagestyle{plain}{
    \fancyhf{}
    \fancyfoot[R]{\thepage\ of \pageref*{LastPage}}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
}
\fancypagestyle{normal}{
    \fancyhf{}
    \fancyfoot[R]{\thepage\ of \pageref*{LastPage}}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
}
\fancypagestyle{titlepage}{%
    \fancyhf{}
    \fancyfoot[L]{\footnotesize \textcolor{copyright}{© 2024 Canonical Ltd. All rights reserved. Confidential and proprietary, do not share without permission.}}
}
\newcommand\sphinxbackoftitlepage{\thispagestyle{titlepage}}
\titleformat{\chapter}[block]{\Huge \color{title} \bfseries\filright}{\thechapter}{1.5ex}{}
\titlespacing{\chapter}{0pt}{0pt}{0pt}
\titleformat{\section}[block]{\huge \bfseries\filright}{\thesection}{1.5ex}{} 
\titlespacing{\section}{0pt}{0pt}{0pt}
\titleformat{\subsection}[block]{\Large \bfseries\filright}{\thesubsection}{1.5ex}{} 
\titlespacing{\subsection}{0pt}{0pt}{0pt}
\setcounter{tocdepth}{1}
\renewcommand\pagenumbering[1]{}
''',
    'sphinxsetup': 'verbatimwithframe=false, pre_border-radius=0pt, verbatimvisiblespace=\\phantom{}, verbatimcontinued=\\phantom{}',
    'extraclassoptions': 'openany,oneside',
    'maketitle': r'''
\begin{titlepage}
\begin{flushleft}
    \begin{tikzpicture}[remember picture,overlay]
    \node[anchor=south east, inner sep=0] at (current page.south east) {
    \includegraphics[width=\paperwidth, height=\paperheight]{front-page-light}
    };
    \end{tikzpicture}
\end{flushleft}

\vspace*{3cm}

\Huge \textcolor{title}{''' + template_values['CUSTOMER_NAME'] + r''' Onboarding Guide}

\Large \textcolor{subtitle}{\textit{Dedicated Snap Store and Image Build Quick-Start Guide}}

\vfill

\textcolor{label}{Prepared by:} \tabto{8em} ''' + template_values['PREPARED_BY'] + r'''

\textcolor{label}{Prepared on:} \tabto{8em} ''' + template_values['PREPARED_ON'] + r'''

\vfill

\begin{adjustwidth}{8cm}{0pt}
\begin{tabularx}{0.5\textwidth}{ l l }
    \hspace{3cm}  & \small\textcolor{lightgray}{© 2024 Canonical Ltd.}            \\
    \hspace{3cm}  & \small\textcolor{lightgray}{All rights reserved.}             \\
    \hspace{3cm}  & \small\textcolor{lightgray}{Confidential and proprietary,}    \\
    \hspace{3cm}  & \small\textcolor{lightgray}{do not share without permission.} \\

\end{tabularx}
\end{adjustwidth}

\end{titlepage}
\RemoveFromHook{shipout/background}
\AddToHook{shipout/background}{
      \begin{tikzpicture}[remember picture,overlay]
      \node[anchor=south west, align=left, inner sep=0] at (current page.south west) {
        \includegraphics[width=\paperwidth]{normal-page-footer}
      };
      \end{tikzpicture}
      \begin{tikzpicture}[remember picture,overlay]
      \node[anchor=north east, opacity=0.5, inner sep=35] at (current page.north east) {
        \includegraphics[width=4cm]{Canonical-logo-4x}
      };
      \end{tikzpicture}
    }
''',
}