{% for cat, msg in get_flashed_messages(True) %}
<div class="flash {{cat}}">{{msg}}</div>
{% endfor %}