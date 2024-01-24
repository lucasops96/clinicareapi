from django.urls import path,include

from clinicareapi import views
from rest_framework.routers import SimpleRouter

app_name = 'clinicareapi'

router = SimpleRouter()
router.register('clinicareapi/paciente',views.PacienteViewSet,basename='paciente')
router.register('clinicareapi/profissional',views.ProfissionalSaudeViewSet,basename='profissional')
router.register('clinicareapi/custom/user',views.CustomUserViewSet,basename='custom_user')
router.register('clinicareapi/user',views.UserViewSet,basename='user')
router.register('clinicareapi/endereco',views.EnderecoViewSet,basename='endereco')

urlpatterns = [
    path('',include(router.urls))
]
