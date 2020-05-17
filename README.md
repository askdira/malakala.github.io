
{% extends "base.html" %}
{% load static %}
{% block page_content %}
<h1>Coretan</h1>
<div class="row">
    {% for projek in projek1 %}
    <div class="col-md-4">
        <div class="card mb-2">
            <img class="card-img-top" src="{% static projek.gambar %}" />
            <div class="card-body">
                <h5 class="card-title">{{ projek.judul }}</h5>
                <p class="card-text">{{ projek.desk | slice:":50" }}...</p>
                <a href="{% url 'detail' projek.pk %}" class="btn btn-primary">Baca</a>
            </div>
        </div>
    </div>
    {% endfor %}
</div>
{% endblock %}
