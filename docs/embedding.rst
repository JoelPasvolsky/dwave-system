.. _embedding_system:

=========
Embedding
=========

.. automodule:: dwave.embedding.__init__

.. currentmodule:: dwave.embedding

Classes
=======

.. autoclass:: EmbeddedStructure

Chains
======

.. TODO: move module docstring into __init__

.. automodule:: dwave.embedding.chain_strength
.. automodule:: dwave.embedding.chain_breaks

.. currentmodule:: dwave.embedding

.. autosummary:: 
    :recursive:
    :template: custom-class-template.rst
    :toctree: generated/

    chain_breaks.discard
    chain_breaks.majority_vote
    chain_breaks.MinimizeEnergy
    chain_breaks.weighted_random
    chain_strength.uniform_torque_compensation
    chain_strength.scaled

Exceptions
==========

.. autosummary:: 
    :recursive:
    :template: custom-class-template.rst
    :toctree: generated/

    exceptions.EmbeddingError
    exceptions.MissingChainError
    exceptions.ChainOverlapError
    exceptions.DisconnectedChainError
    exceptions.InvalidNodeError
    exceptions.MissingEdgeError

Generators
==========

.. autosummary:: 
    :recursive:
    :template: custom-class-template.rst
    :toctree: generated/

    minorminer.find_embedding
    chimera.find_clique_embedding
    chimera.find_biclique_embedding
    chimera.find_grid_embedding
    pegasus.find_clique_embedding
    pegasus.find_biclique_embedding
    zephyr.find_clique_embedding
    zephyr.find_biclique_embedding

Utilities & Diagnostics
=======================

.. autosummary::
    :recursive:
    :template: custom-class-template.rst
    :toctree: generated/

    chain_break_frequency
    diagnose_embedding
    is_valid_embedding
    verify_embedding

.. autosummary:: 
    :recursive:
    :template: custom-class-template.rst
    :toctree: generated/

    embed_bqm
    embed_ising
    embed_qubo
    unembed_sampleset



