# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.ifconfig'
]

autosummary_generate = True

# The suffix(es) of source filenames.
source_suffix = '.rst'

master_doc = 'index'

# General information about the project.
project = u'dwave-system'
copyright = u'2018, D-Wave Systems Inc'
author = u'D-Wave Systems Inc'

import dwave.system.package_info
version = dwave.system.package_info.__version__
release = dwave.system.package_info.__version__

language = "en"

add_module_names = False

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'sdk_index.rst']

linkcheck_retries = 2
linkcheck_anchors = False
linkcheck_ignore = [r'https://cloud.dwavesys.com/leap',  # redirects, many checks
                    r'https://www.jstor.org/stable',
                    r'https://doi.org/']

pygments_style = 'sphinx'

todo_include_todos = True

modindex_common_prefix = ['dwave-system.']

doctest_global_setup = """
import dimod
from dwave.embedding import *

from unittest.mock import Mock
from dwave.system.testing import MockDWaveSampler
import dwave.system
dwave.system.DWaveSampler = Mock()
dwave.system.DWaveSampler.side_effect = MockDWaveSampler
from dwave.system import *
"""

# -- Options for HTML output ----------------------------------------------
html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    "collapse_navigation": True,
    "show_prev_next": False,
}
html_sidebars = {"**": ["search-field", "sidebar-nav-bs"]}  # remove ads

intersphinx_mapping = {'python': ('https://docs.python.org/3', None),
    'networkx': ('https://networkx.github.io/documentation/stable/', None),
    'dwave': ('https://docs.dwavequantum.com/en/latest/', None),
    }
    


rst_epilog = """
.. |copy| unicode:: U+000A9 .. COPYRIGHT SIGN
.. |deg| unicode:: U+00B0
.. |nbsp| unicode:: 0xA0    .. non-breaking space
.. |nb-| unicode:: U+2011  .. Non-breaking hyphen (e.g., "D |nb-| Wave")
    :trim:
.. |reg| unicode:: U+000AE .. REGISTERED SIGN
.. |tm| unicode::  U+2122
.. |Darr| unicode:: U+02193 .. DOWNWARDS ARROW from docutils/parsers/rst/include/isonum.txt
.. |Uarr| unicode:: U+02191 .. UPWARDS ARROW from docutils/parsers/rst/include/isonum.txt

.. |array-like| replace:: array-like    .. used in dwave-optimization
.. _array-like: https://numpy.org/devdocs/glossary.html#term-array_like

.. |adv2| unicode:: Advantage2
.. |adv2_tm| unicode:: Advantage2 U+2122
.. |cloud| unicode:: Leap
.. _cloud: https://cloud.dwavesys.com/leap
.. |cloud_tm| unicode:: Leap U+2122
.. _cloud_tm: https://cloud.dwavesys.com/leap
.. |dwave_2kq| unicode:: D-Wave U+00A0 2000Q
.. |dwave_5kq| unicode:: Advantage
.. |dwave_5kq_tm| unicode:: Advantage U+2122
.. |dwave_short| unicode:: D-Wave
.. _dwave_short: https://dwavequantum.com
.. |dwave_short_tm| unicode:: D-Wave U+2122 U+0020
.. |dwave_system| unicode:: D-Wave U+00A0 System
.. |ocean_tm| unicode:: Ocean U+2122
.. |ocean_sdk| replace:: Ocean software
.. _ocean_sdk: https://github.com/dwavesystems/dwave-ocean-sdk

.. |dwave_launch_tm| unicode:: D U+2011 Wave U+00A0 Launch U+2122
.. _dwave_launch_tm: https://www.dwavesys.com/solutions-and-products/professional-services
.. |dwave_launch| unicode:: D U+2011 Wave U+00A0 Launch
.. _dwave_launch: https://www.dwavesys.com/solutions-and-products/professional-services
.. |dwave_learn_tm| unicode:: D U+2011 Wave U+00A0 Learn U+2122
.. _dwave_learn_tm: https://training.dwavequantum.com
.. |dwave_learn| unicode:: D U+2011 Wave U+00A0 Learn
.. _dwave_learn: https://training.dwavequantum.com

.. |support_email| replace:: D-Wave Customer Support
.. _support_email: support@dwavesys.com

.. |doc_operations| replace:: *D-Wave Quantum Computer Operations*
"""
