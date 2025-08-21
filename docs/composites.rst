.. _system_composites:

==========
Composites
==========

:ref:`dimod composites <concept_samplers_composites>` that provide layers of pre- and
post-processing (e.g., :term:`minor-embedding`) when using the D-Wave system:

.. currentmodule:: dwave.system.composites

Other Ocean packages provide additional composites; for example,
:ref:`dimod <index_dimod>` provides composites that operate
on the problem (e.g., scaling values), track inputs and outputs for debugging,
and other useful functionality relevant to generic samplers.

CutOffs
=======

Prunes the binary quadratic model (BQM) submitted to the child sampler by retaining
only interactions with values commensurate with the sampler’s precision.

The following composites are supported:

*   :class:`.CutOffComposite`
*   :class:`.PolyCutOffComposite`

.. autoclass:: CutOffComposite
    :show-inheritance:
    :members:
    :inherited-members:

.. autoclass:: PolyCutOffComposite
    :show-inheritance:
    :members:
    :inherited-members:

Embedding
=========

:term:`Minor-embed` a problem :term:`BQM` into a D-Wave system.

.. automodule:: dwave.system.composites.embedding

.. currentmodule:: dwave.system.composites

The following composites are supported:

*   :class:`.AutoEmbeddingComposite`
*   :class:`.EmbeddingComposite`
*   :class:`.FixedEmbeddingComposite`
*   :class:`.LazyFixedEmbeddingComposite`
*   :class:`.ParallelEmbeddingComposite`
*   :class:`.VirtualGraphComposite`

.. autoclass:: AutoEmbeddingComposite
    :show-inheritance:
    :members:
    :inherited-members:

.. autoclass:: EmbeddingComposite
    :show-inheritance:
    :members:
    :inherited-members:

.. autoclass:: FixedEmbeddingComposite
    :show-inheritance:
    :members:
    :inherited-members:

.. autoclass:: LazyFixedEmbeddingComposite
    :show-inheritance:
    :members:
    :inherited-members:

.. autoclass:: ParallelEmbeddingComposite
    :show-inheritance:
    :members:
    :inherited-members:

.. autoclass:: VirtualGraphComposite
    :show-inheritance:
    :members:
    :inherited-members:

Linear Bias
===========

Composite for using auxiliary qubits to bias problem qubits.

The following composites are supported:

*   :class:`.LinearAncillaComposite`

.. autoclass:: LinearAncillaComposite
    :show-inheritance:
    :members:
    :inherited-members:


Reverse Anneal
==============

Composites that do batch operations for reverse annealing based on sets of initial
states or anneal schedules.

The following composites are supported:

*   :class:`.ReverseBatchStatesComposite`
*   :class:`.ReverseAdvanceComposite`

.. autoclass:: ReverseBatchStatesComposite
    :show-inheritance:
    :members:
    :inherited-members:

.. autoclass:: ReverseAdvanceComposite
    :show-inheritance:
    :members:
    :inherited-members:
