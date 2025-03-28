import datetime
import ast
from pathlib import Path
import sys
import warnings


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

# Allow local extensions.
sys.path.append(str((Path.cwd() / __file__).with_name(".sphinx") / "exts"))

###########################
### Project information ###
###########################

# Project name

project = "Workshop"
author = "Canonical Ltd"


# Sidebar documentation title; best kept reasonably short

html_title = ""


# Copyright string; shown at the bottom of the page
#
# Now, the starter pack uses CC-BY-SA as the license
# and the current year as the copyright year.
#
# NOTE: For static works, it is common to provide the year of first publication.
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
# NOTE: The Open Graph Protocol (OGP) enhances page display in a social graph
#       and is used by social media platforms; see https://ogp.me/

ogp_site_url = "https://canonical-workshop.readthedocs-hosted.com/"


# Preview name of the documentation website

ogp_site_name = project


# Preview image URL

ogp_image = "https://assets.ubuntu.com/v1/253da317-image-document-ubuntudocs.svg"


# Product favicon; shown in bookmarks, browser tabs, etc.

html_favicon = ".sphinx/_static/favicon.png"


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
    "product_tag": "_static/tag.png",
    # Your Discourse instance URL
    #
    # NOTE: If set, adding ':discourse: 123' to an .rst file
    #       will add a link to Discourse topic 123 at the bottom of the page.
    "discourse": "https://discourse.canonical.com/",
    "category": "engineering/workshops",
    # Your Mattermost channel URL
    "mattermost": "https://chat.canonical.com/canonical/channels/SDK",
    # Your Matrix channel URL
    "matrix": "https://matrix.to/#/#documentation:ubuntu.com",
    # Your documentation GitHub repository URL
    #
    # NOTE: If set, links for viewing the documentation source files
    #       and creating GitHub issues are added at the bottom of each page.
    "github_url": "https://github.com/canonical/workshop",
    # Docs branch in the repo; used in links for viewing the source files
    "repo_default_branch": "main",
    # Docs location in the repo; used in links for viewing the source files
    #
    "repo_folder": "/docs/",
    "github_issues": "enabled",
    # "sequential_nav": "none",
    # "display_contributors": True,
    # "display_contributors_since": "",
}

# Project slug; see https://meta.discourse.org/t/what-is-category-slug/87897

slug = ""


# Template and asset locations

html_static_path = [".sphinx/_static", ".sphinx/images"]
templates_path = [".sphinx/_templates"]


#################
### Redirects ###
#################

# To set up redirects: https://documatt.gitlab.io/sphinx-reredirects/usage.html
# For example: 'explanation/old-name.html': '../how-to/prettify.html',

# To set up redirects in the Read the Docs project dashboard:
# https://docs.readthedocs.io/en/stable/guides/redirects.html

# NOTE: If undefined, set to None, or empty,
#       the sphinx_reredirects extension will be disabled.

redirects = {}


###############################
### Link checker exceptions ###
###############################

# A regex list of URLs that are ignored by 'make linkcheck'

linkcheck_ignore = [
    "http://127.0.0.1:8000",
    "https://github.com/canonical/sdkcraft",
    "https://github.com/canonical/workshop",
    r"^https://.*\.readthedocs-hosted\.com/.*#\w+$",
]


# A regex list of URLs where anchors are ignored by 'make linkcheck'

linkcheck_anchors_ignore_for_url = [r"https://github\.com/.*"]


############################
### Configuration extras ###
############################

# Custom MyST syntax extensions; see
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
#
# NOTE: By default, the following MyST extensions are enabled:
#       substitution, deflist, linkify

# myst_enable_extensions = set()


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

# The insert_console_prompts extension adds prompts to console code blocks.
# This improves the appearance of HTML code blocks,
# without adding extraneous prompts to commands copied from GitHub.

extensions = [
    "canonical_sphinx",
    "sphinxcontrib.cairosvgconverter",
    "sphinxcontrib.mermaid",
    "insert_console_prompts",
]


# Excludes files or directories from processing

exclude_patterns = ["readme.rst", "reference/cli/workshop-*.rst", "coverage.md"]

# Adds custom CSS files, located under 'html_static_path'

html_css_files = [
    "css/pdf.css",
    "css/workshop.css",
]


# Adds custom JavaScript files, located under 'html_static_path'

# html_js_files = []


# Specifies a reST snippet to be appended to each .rst file

rst_epilog = """
.. include:: /reuse/links.txt
.. include:: /reuse/substitutions.txt
"""

# Feedback button at the top; enabled by default

disable_feedback_button = True


# Your manpage URL
#
# TODO: To enable manpage links, uncomment and update as needed.
#
# NOTE: If set, adding ':manpage:' to an .rst file
#       adds a link to the corresponding man section at the bottom of the page.

# manpages_url = 'https://manpages.ubuntu.com/manpages/noble/en/man{section}/{page}.{section}.html'


# Specifies a reST snippet to be prepended to each .rst file
# This defines a :center: role that centers table cell content.
# This defines a :h2: role that styles content for use with PDF generation.

rst_prolog = """
.. role:: center
   :class: align-center
.. role:: h2
    :class: hclass2

.. |project| replace:: {project}
"""

# Workaround for https://github.com/canonical/canonical-sphinx/issues/34

if "discourse_prefix" not in html_context and "discourse" in html_context:
    html_context["discourse_prefix"] = html_context["discourse"] + "/t/"


copybutton_prompt_text = "$ "
copybutton_here_doc_delimiter = "EOF"
copybutton_line_continuation_character = "\\"


# workaround for https://github.com/executablebooks/sphinx-tabs/issues/197
warnings.filterwarnings(
    "ignore",
    message="The str interface for _JavaScript objects is deprecated. Use js.filename instead.",
)

# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-smartquotes_action
smartquotes_action = "qe"

############################################################
### PDF configuration
############################################################

latex_additional_files = [
    "./.sphinx/fonts/Ubuntu-B.ttf",
    "./.sphinx/fonts/Ubuntu-R.ttf",
    "./.sphinx/fonts/Ubuntu-RI.ttf",
    "./.sphinx/fonts/UbuntuMono-R.ttf",
    "./.sphinx/fonts/UbuntuMono-RI.ttf",
    "./.sphinx/fonts/UbuntuMono-B.ttf",
    "./.sphinx/images/Canonical-logo-4x.png",
    "./.sphinx/images/front-page-light.pdf",
    "./.sphinx/images/normal-page-footer.pdf",
]

latex_engine = "xelatex"
latex_show_pagerefs = True
latex_show_urls = "footnote"

with open(".sphinx/latex_elements_template.txt", "rt") as file:
    latex_config = file.read()

latex_elements = ast.literal_eval(latex_config.replace("$PROJECT", project))
