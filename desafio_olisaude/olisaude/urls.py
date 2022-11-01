"""olisaude URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from saude_app.views import list_costumers, get_costumer, calculate_score, create_costumer, add_problems

urlpatterns = [
    path("costumers/", list_costumers, name='costumer'),
    path("costumers/<int:code>", get_costumer, name='get_costumer'),
    path("create_costumer/", create_costumer, name='create'),
    path("add_problem/", add_problems, name='add_problems'),
    path("score/", calculate_score, name='score'),
    path("my_admin/", admin.site.urls),
]
