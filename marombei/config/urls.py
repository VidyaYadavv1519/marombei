"""
Marombei created by Danilo Marto de Carvalho <danilomartodecarvalho@protonmail.com>
Copyright© Webtinguetá Project licensed under the MIT Agreement.
"""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
