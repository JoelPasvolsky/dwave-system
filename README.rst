.. image:: https://img.shields.io/pypi/v/dwave-system.svg
   :target: https://pypi.org/project/dwave-system

.. image:: https://img.shields.io/pypi/pyversions/dwave-system.svg?style=flat
    :target: https://pypi.org/project/dwave-system
    :alt: PyPI - Python Version

.. image:: https://codecov.io/gh/dwavesystems/dwave-system/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/dwavesystems/dwave-system

.. image:: https://circleci.com/gh/dwavesystems/dwave-system.svg?style=shield
   :target: https://circleci.com/gh/dwavesystems/dwave-system

.. |tm| unicode::  U+2122

============
dwave-system
============

.. index-start-marker

``dwave-system`` is documented here: Ocean\ |tm|
`SDK documentation <https://docs.ocean.dwavesys.com/en/stable/index.html>`_. 

``dwave-system`` enables easy incorporation of the D-Wave quantum computer as a
sampler in either a hybrid quantum-classical solution or directly. It includes 
``DWaveSampler``, a dimod sampler that accepts and passes system parameters 
such as system identification and authentication down the stack, 
``LeapHybridNLSampler``, for hybrid solvers in the Leap\ |tm| service, and others. 
It also includes several useful composites---layers of pre- and 
post-processing---that can be used with ``DWaveSampler`` to handle 
minor-embedding, optimize chain strength, etc.

.. index-end-marker

Example
=======

This example solves a small example of a known graph problem, minimum
`vertex cover <https://en.wikipedia.org/wiki/Vertex_cover>`_\ . It uses the 
NetworkX graphic package to create the problem, Ocean SDK's 
:std:doc:`dwave_networkx <oceandocs:docs_dnx/sdk_index>`
to formulate the graph problem as a :term:`BQM`, and dwave-system's
:class:`~dwave.system.samplers.DWaveSampler()` to use a D-Wave system as the sampler.
dwave-system's :class:`~dwave.system.composites.EmbeddingComposite()` handles mapping
between the problem graph to the D-Wave system's numerically indexed qubits,
a mapping known as :term:`minor-embedding`.

>>> import networkx as nx
>>> import dwave_networkx as dnx
>>> from dwave.system import DWaveSampler, EmbeddingComposite
...
>>> s5 = nx.star_graph(4)  # a star graph where node 0 is hub to four other nodes
>>> sampler = EmbeddingComposite(DWaveSampler())
>>> print(dnx.min_vertex_cover(s5, sampler))
[0]

Installation
============

.. installation-start-marker

Installation from PyPI
----------------------

.. code-block:: bash

    pip install dwave-system

Installation from PyPI with Drivers
-----------------------------------

.. note::
    Prior to v0.3.0, running ``pip install dwave-system`` installed a driver dependency called ``dwave-drivers``
    (previously also called ``dwave-system-tuning``). This dependency has a restricted license and has been made optional
    as of v0.3.0, but is highly recommended. To view the license details:

    .. code-block:: python

        from dwave.drivers import __license__
        print(__license__)

To install with optional dependencies:

.. code-block:: bash

    pip install dwave-system[drivers] --extra-index-url https://pypi.dwavesys.com/simple

Installation from Source
------------------------

.. code-block:: bash

    pip install -r requirements.txt
    python setup.py install

Note that installing from source installs ``dwave-drivers``. To uninstall the proprietary components:

.. code-block:: bash

    pip uninstall dwave-drivers

.. installation-end-marker


License
=======

Released under the Apache License 2.0. See `<LICENSE>`_ file.

Contributing
============

Ocean SDK's 
`contributing guide <https://docs.ocean.dwavesys.com/en/stable/contributing.html>`_
has guidelines for contributing to Ocean software packages.
