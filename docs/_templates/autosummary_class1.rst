{{ objname | underline}}

.. currentmodule:: {{ module }}

.. autoclass:: {{ objname }}
    :no-index:
    :show-inheritance:

{% block attributes %}
{% if attributes %}
{{ 'Properties' }}
{{ '----------' }}

.. autosummary::
{% for item in attributes %}
   ~{{ name }}.{{ item }}
{%- endfor %}
{% endif %}
{% endblock %}

{% block methods %}
{% if methods %}
{{ 'Methods' }}
{{ '-------' }}

.. autosummary::
    :signatures: none
{% for item in methods %}
    {%- if not item.startswith('_') %}
    ~{{ name }}.{{ item }}
    {%- endif -%}
{%- endfor %}
{% endif %}
{% endblock %}

.. autoclass:: {{ objname }}
    :class-doc-from: init
    :member-order: groupwise
    :members:
    :inherited-members: