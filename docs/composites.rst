.. _system_composites:

==========
Composites
==========

:ref:`dimod composites <concept_samplers_composites>` that provide layers of
pre- and post-processing (e.g., :term:`minor-embedding`) when using D-Wave
quantum computers.

.. currentmodule:: dwave.system.composites

Other Ocean packages provide additional composites; for example:

*   :ref:`dimod <index_dimod>` provides :ref:`composites <dimod_composites>`
    that operate on the problem (e.g., scaling values), track inputs and outputs
    for debugging, and other useful functionality relevant to generic samplers.
*   :ref:`index_preprocessing` provides composites that clip, fix, and scale
    variables and apply spin-reversal transforms.


CutOffs
=======

.. automodule:: dwave.system.composites.cutoffcomposite


CutOffComposite
---------------

.. autoclass:: CutOffComposite
   :show-inheritance:

Properties
~~~~~~~~~~

.. autosummary::
   :toctree: generated/

   CutOffComposite.children
   CutOffComposite.parameters
   CutOffComposite.properties

See also inherited properties of the
:class:`~dwave.system.composites.cutoffcomposite` class.

Methods
~~~~~~~

.. autosummary::
   :toctree: generated/

   CutOffComposite.sample

See also inherited methods of the
:class:`~dwave.system.composites.cutoffcomposite` class.

PolyCutOffComposite
-------------------

.. autoclass:: PolyCutOffComposite
   :show-inheritance:

Properties
~~~~~~~~~~

.. autosummary::
   :toctree: generated/

   PolyCutOffComposite.children
   PolyCutOffComposite.parameters
   PolyCutOffComposite.properties

See also inherited properties of the
:class:`~dwave.system.composites.PolyCutOffComposite` class.

Methods
~~~~~~~

.. autosummary::
   :toctree: generated/

   PolyCutOffComposite.sample_poly

See also inherited methods of the
:class:`~dwave.system.composites.PolyCutOffComposite` class.

Embedding
=========

:term:`Minor-embed` a problem :term:`BQM` into a D-Wave system.

.. automodule:: dwave.system.composites.embedding

.. currentmodule:: dwave.system.composites


AutoEmbeddingComposite
----------------------

.. autoclass:: AutoEmbeddingComposite
   :show-inheritance:

Methods
~~~~~~~

.. autosummary::
   :toctree: generated/

   AutoEmbeddingComposite.sample

See also inherited properties and methods of the
:class:`~dwave.system.composites.embedding.AutoEmbeddingComposite` class.

EmbeddingComposite
------------------

.. autoclass:: EmbeddingComposite
   :show-inheritance:

Properties
~~~~~~~~~~

.. autosummary::
   :toctree: generated/

   EmbeddingComposite.children
   EmbeddingComposite.parameters
   EmbeddingComposite.properties
   EmbeddingComposite.return_embedding_default
   EmbeddingComposite.warnings_default

See also inherited properties of the
:class:`~dwave.system.composites.embedding.EmbeddingComposite` class.

Methods
~~~~~~~

.. autosummary::
   :toctree: generated/

   EmbeddingComposite.sample

See also inherited methods of the
:class:`~dwave.system.composites.embedding.EmbeddingComposite` class.

FixedEmbeddingComposite
-----------------------

.. autoclass:: FixedEmbeddingComposite
   :show-inheritance:

See also inherited properties and methods of the
:class:`~dwave.system.composites.embedding.FixedEmbeddingComposite` class.

LazyFixedEmbeddingComposite
---------------------------

.. autoclass:: LazyFixedEmbeddingComposite
   :show-inheritance:

Properties
~~~~~~~~~~

.. autosummary::
   :toctree: generated/


   LazyFixedEmbeddingComposite.adjacency
   LazyFixedEmbeddingComposite.edgelist
   LazyFixedEmbeddingComposite.embedding
   LazyFixedEmbeddingComposite.nodelist

See also inherited properties of the
:class:`~dwave.system.composites.embedding.LazyFixedEmbeddingComposite` class.

Methods
~~~~~~~

.. autosummary::
   :toctree: generated/

   LazyFixedEmbeddingComposite.sample

See also inherited methods of the
:class:`~dwave.system.composites.embedding.LazyFixedEmbeddingComposite` class.

ParallelEmbeddingComposite
--------------------------

.. autoclass:: ParallelEmbeddingComposite
   :show-inheritance:

Properties
~~~~~~~~~~

.. autosummary::
   :toctree: generated/


   ParallelEmbeddingComposite.children
   ParallelEmbeddingComposite.edgelist
   ParallelEmbeddingComposite.embeddings
   ParallelEmbeddingComposite.nodelist
   ParallelEmbeddingComposite.num_embeddings
   ParallelEmbeddingComposite.parameters
   ParallelEmbeddingComposite.properties

See also inherited properties of the
:class:`~dwave.system.composites.ParallelEmbeddingComposite` class.

Methods
~~~~~~~

.. autosummary::
   :toctree: generated/

   ParallelEmbeddingComposite.sample
   ParallelEmbeddingComposite.sample_multiple

See also inherited methods of the
:class:`~dwave.system.composites.ParallelEmbeddingComposite` class.

TilingComposite
---------------

.. autoclass:: TilingComposite
   :show-inheritance:

Properties
~~~~~~~~~~

.. autosummary::
   :toctree: generated/

   TilingComposite.children
   TilingComposite.edgelist
   TilingComposite.embeddings
   TilingComposite.nodelist
   TilingComposite.num_tiles
   TilingComposite.parameters
   TilingComposite.properties

Methods
~~~~~~~

.. autosummary::
   :toctree: generated/

   TilingComposite.sample


VirtualGraphComposite
---------------------

.. autoclass:: VirtualGraphComposite
   :show-inheritance:

Methods
~~~~~~~

.. autosummary::
   :toctree: generated/

   VirtualGraphComposite.sample


Linear Bias
===========

.. automodule:: dwave.system.composites.linear_ancilla

.. currentmodule:: dwave.system.composites

LinearAncillaComposite
-----------------------

.. autoclass:: LinearAncillaComposite
   :show-inheritance:

Properties
~~~~~~~~~~

.. autosummary::
   :toctree: generated/

   LinearAncillaComposite.children
   LinearAncillaComposite.parameters
   LinearAncillaComposite.properties

Methods
~~~~~~~

.. autosummary::
   :toctree: generated/

   LinearAncillaComposite.sample


Reverse Anneal
==============

.. automodule:: dwave.system.composites.reversecomposite

.. currentmodule:: dwave.system.composites

ReverseBatchStatesComposite
---------------------------

.. autoclass:: ReverseBatchStatesComposite
   :show-inheritance:

Properties
~~~~~~~~~~

.. autosummary::
   :toctree: generated/

   ReverseBatchStatesComposite.children
   ReverseBatchStatesComposite.parameters
   ReverseBatchStatesComposite.properties

Methods
~~~~~~~

.. autosummary::
   :toctree: generated/

   ReverseBatchStatesComposite.sample


ReverseAdvanceComposite
-----------------------

.. autoclass:: ReverseAdvanceComposite
   :show-inheritance:

Properties
~~~~~~~~~~

.. autosummary::
   :toctree: generated/

   ReverseAdvanceComposite.children
   ReverseAdvanceComposite.parameters
   ReverseAdvanceComposite.properties

Methods
~~~~~~~

.. autosummary::
   :toctree: generated/

   ReverseAdvanceComposite.sample


