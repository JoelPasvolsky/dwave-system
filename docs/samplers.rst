.. _system_samplers:

========
Samplers
========

A :term:`sampler` accepts a problem in :term:`nonlinear model` or
:term:`quadratic model` (e.g., :term:`BQM`) format and returns variable
assignments. Samplers generally try to find minimizing values but can also
sample from distributions defined by the problem.

.. currentmodule:: dwave.system.samplers

These samplers are non-blocking: the returned :class:`~dimod.SampleSet` is constructed
from a :class:`~concurrent.futures.Future`-like object that is resolved on the first
read of any of its properties; for example, by printing the results. Your code can
query its status with the :meth:`~dimod.SampleSet.done` method or ensure resolution
with the :meth:`~dimod.SampleSet.resolve` method.

Other Ocean packages provide additional samplers; for example,
:ref:`dimod <index_dimod>` provides samplers for testing
your code.

QPU Samplers
============

Samplers for using the quantum processing unit (:term:`QPU`) directly.

DWaveSampler
------------

.. autoclass:: DWaveSampler
    :show-inheritance:

Properties
~~~~~~~~~~

.. autosummary::
    :toctree: generated/

    ~DWaveSampler.edgelist
    ~DWaveSampler.nodelist
    ~DWaveSampler.parameters
    ~DWaveSampler.properties
    ~DWaveSampler.warnings_default

See also inherited properties of the
:class:`~dwave.system.samplers.DWaveSampler` class.

Methods
~~~~~~~

.. autosummary::
    :toctree: generated/

    ~DWaveSampler.close
    ~DWaveSampler.sample
    ~DWaveSampler.to_networkx_graph
    ~DWaveSampler.trigger_failover
    ~DWaveSampler.validate_anneal_schedule

See also inherited methods of the
:class:`~dwave.system.samplers.DWaveSampler` class.

DWaveCliqueSampler
------------------

.. autoclass:: DWaveCliqueSampler
    :show-inheritance:

Properties
~~~~~~~~~~

.. autosummary::
    :toctree: generated/

    ~DWaveCliqueSampler.largest_clique_size
    ~DWaveCliqueSampler.parameters
    ~DWaveCliqueSampler.properties
    ~DWaveCliqueSampler.qpu_linear_range
    ~DWaveCliqueSampler.qpu_quadratic_range
    ~DWaveCliqueSampler.target_graph

See also inherited properties of the
:class:`~dwave.system.samplers.DWaveCliqueSampler` class.

Methods
~~~~~~~

.. autosummary::
    :toctree: generated/

    ~DWaveCliqueSampler.clique
    ~DWaveCliqueSampler.close
    ~DWaveCliqueSampler.largest_clique
    ~DWaveCliqueSampler.sample
    ~DWaveCliqueSampler.trigger_failover

See also inherited methods of the
:class:`~dwave.system.samplers.DWaveCliqueSampler` class.

Stride Hybrid Solver
====================

The Leap service's quantum-classical nonlinear :term:`hybrid` solver for
optimizing business problems.

StrideHybridSolver
------------------

.. autoclass:: StrideHybridSolver

Properties
~~~~~~~~~~

.. autosummary::
    :toctree: generated/

    ~StrideHybridSolver.default_solver
    ~StrideHybridSolver.parameters
    ~StrideHybridSolver.properties

Methods
~~~~~~~

.. autosummary::
    :toctree: generated/

    ~StrideHybridSolver.close
    ~StrideHybridSolver.estimated_min_time_limit
    ~StrideHybridSolver.sample

LeapHybridNLSampler
-------------------

.. autoclass:: LeapHybridNLSampler


Other Hybrid Solvers
====================

Additional :term:`hybrid` solvers in the Leap service.


LeapHybridSampler
-----------------

.. autoclass:: LeapHybridSampler
    :show-inheritance:

Properties
~~~~~~~~~~

.. autosummary::
    :toctree: generated/

    ~LeapHybridSampler.default_solver
    ~LeapHybridSampler.parameters
    ~LeapHybridSampler.properties

See also inherited properties of the
:class:`~dwave.system.samplers.LeapHybridSampler` class.

Methods
~~~~~~~

.. autosummary::
    :toctree: generated/

    ~LeapHybridSampler.close
    ~LeapHybridSampler.min_time_limit
    ~LeapHybridSampler.sample

See also inherited methods of the
:class:`~dwave.system.samplers.LeapHybridSampler` class.

LeapHybridCQMSampler
--------------------

.. autoclass:: LeapHybridCQMSampler

Properties
~~~~~~~~~~

.. autosummary::
    :toctree: generated/

    ~LeapHybridCQMSampler.default_solver
    ~LeapHybridCQMSampler.properties
    ~LeapHybridCQMSampler.parameters

Methods
~~~~~~~

.. autosummary::
    :toctree: generated/

    ~LeapHybridCQMSampler.close
    ~LeapHybridCQMSampler.min_time_limit
    ~LeapHybridCQMSampler.sample_cqm

LeapHybridDQMSampler
--------------------

.. autoclass:: LeapHybridDQMSampler

Properties
~~~~~~~~~~

.. autosummary::
    :toctree: generated/

    ~LeapHybridDQMSampler.default_solver
    ~LeapHybridDQMSampler.parameters
    ~LeapHybridDQMSampler.properties

Methods
~~~~~~~

.. autosummary::
    :toctree: generated/

    ~LeapHybridDQMSampler.min_time_limit
    ~LeapHybridDQMSampler.sample_dqm
