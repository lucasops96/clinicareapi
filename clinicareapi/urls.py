from django.urls import path,include

from clinicareapi import views
from rest_framework.routers import SimpleRouter

app_name = 'clinicareapi'

router = SimpleRouter()
router.register('clinicareapi/paciente',views.PacienteViewSet,basename='paciente')

urlpatterns = [
    path('',include(router.urls))
]
