.. DashboardUtilsDataScience documentation master file, created by
   sphinx-quickstart on Thu Jan 11 13:16:19 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. jinja:: first_ctx

    {% for k, v in topics.items() %}

    {{k}}
    ~~~~~
    {{v}}
    {% endfor %}
