{%- extends 'basic.tpl' -%}

{% block output_group %}
<div class="output_wrapper output_hidden">
  <div class="output">
    {{ super() }}
  </div>
</div>
{% endblock output_group %}

{% block input %}
<div class="inner_cell">
  <div class="input_area">
    {{ cell.source | highlight_code(metadata=cell.metadata) }}
    <i class="icon-hand-up icon-large" style="float:right; margin-bottom:8px; margin-right:10px">
    &nbsp;&nbsp;Click me to hide the output</i>
  </div>
</div>
{%- endblock input %}