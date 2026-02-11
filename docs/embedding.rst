.. _system_embedding:

=========
Embedding
=========

Provides functions that map :term:`binary quadratic models (BQM) <BQM>` and
samples between a :term:`source` :term:`graph` and a :term:`target` graph.


Embedding
=========

For an introduction to :term:`minor-embedding`, see the
:ref:`qpu_embedding_intro` section.

Find Generic Embeddings
-----------------------

:ref:`minorminer <index_minorminer>` is a heuristic tool for minor embedding:
given a minor and target graph, it tries to find a mapping that embeds the minor
into the target.

.. autosummary::
    :toctree: generated/

    minorminer.find_embedding

Find QPU Embeddings
-------------------

Minor-embedding in target graphs with :term:`Chimera`, :term:`Pegasus`, and
:term:`Zephyr` :term:`topology`.

.. currentmodule:: dwave.embedding

.. autosummary::
    :toctree: generated/

    chimera.find_clique_embedding
    chimera.find_biclique_embedding
    chimera.find_grid_embedding
    pegasus.find_clique_embedding
    pegasus.find_biclique_embedding
    zephyr.find_clique_embedding
    zephyr.find_biclique_embedding

Embed Problems
--------------

.. autosummary::
    :toctree: generated/

    embed_bqm
    embed_ising
    embed_qubo

Analyze Embeddings
------------------

.. autosummary::
    :toctree: generated/

    diagnose_embedding
    is_valid_embedding
    verify_embedding

Chain Strength
--------------

.. automodule:: dwave.embedding.chain_strength
.. currentmodule:: dwave.embedding

.. autosummary::
    :toctree: generated/

    ~chain_strength.uniform_torque_compensation
    ~chain_strength.scaled

Helper Functions
----------------

.. autosummary::
    :toctree: generated/

    adjacency_to_edges
    chain_to_quadratic
    ~drawing.draw_chimera_bqm
    edgelist_to_adjacency

EmbeddedStructure Class
-----------------------

.. autosummary::
    :toctree: generated/

    EmbeddedStructure

For all properties and methods, see the
:class:`~dwave.embedding.EmbeddedStructure` class.

.. autosummary::
    :toctree: generated/

    EmbeddedStructure.chain_edges
    EmbeddedStructure.chain_strength
    EmbeddedStructure.embed_bqm
    EmbeddedStructure.interaction_edges
    EmbeddedStructure.max_chain_length


Unembedding
===========

.. autosummary::
    :toctree: generated/

    unembed_sampleset

Diagnose Chains
---------------

.. autosummary::
    :toctree: generated/

    broken_chains
    chain_break_frequency

Handle Broken Chains
--------------------

.. autosummary::
    :toctree: generated/

    ~chain_breaks.discard
    ~chain_breaks.majority_vote
    ~chain_breaks.MinimizeEnergy
    ~chain_breaks.weighted_random

Helper Functions
----------------

.. autosummary::
    :toctree: generated/

    target_to_source


Exceptions
==========

.. autosummary::
   :toctree: generated/

   ~exceptions.EmbeddingError
   ~exceptions.MissingChainError
   ~exceptions.ChainOverlapError
   ~exceptions.DisconnectedChainError
   ~exceptions.InvalidNodeError
   ~exceptions.MissingEdgeError