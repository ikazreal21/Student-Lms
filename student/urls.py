from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    # path("profile/", views.profile, name="profile"),
    # path("subject/", views.subject, name="subject"),
    # path("groups/", views.groups, name="groups"),
    # path("calendar/", views.calendar, name="calendar"),
    # path("grades/", views.grades, name="grades"),
    # path("settings/", views.settings, name="settings"),

    # Prof Urls 
    # path("", views.dashboard, name="dashboard"),
    # path("profile/", views.profile, name="profile"),
    # path("subject/", views.subject, name="subject"),
    # path("groups/", views.groups, name="groups"),
    # path("calendar/", views.calendar, name="calendar"),
    # path("grades/", views.grades, name="grades"),
    # path("settings/", views.settings, name="settings"),
    
]
