from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.getDoctors),
    path('doctors/create', views.addDoctor),
    path('doctors/read/<str:pk>', views.getDoctor),
    path('doctors/update/<str:pk>', views.updateDoctor),
    path('doctors/delete/<str:pk>', views.deleteDoctor),
]
