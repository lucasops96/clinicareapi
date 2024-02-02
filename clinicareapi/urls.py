from django.urls import path,include
from clinicareapi import views
from clinicareapi.views import site
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name = 'clinicareapi'

router = SimpleRouter()
router.register('clinicareapi/paciente',views.PacienteViewSet,basename='paciente')
router.register('clinicareapi/profissional',views.ProfissionalSaudeViewSet,basename='profissional')
router.register('clinicareapi/custom/user',views.CustomUserViewSet,basename='custom_user')
router.register('clinicareapi/user',views.UserViewSet,basename='user')
router.register('clinicareapi/endereco',views.EnderecoViewSet,basename='endereco')

urlpatterns = [
    # urls site
    path('',site.ProfissionalSaudeListView.as_view(),name='profissional_list_view'),
    path('register/healthcare/professional/',site.ProfissionalSaudeCreateView.as_view(),name='profissional_create_view'),

    path('login/',site.login_view,name='login'),
    path('login/create/',site.login_create,name='login_create'),
    path('logout/',site.logout_view,name='logout'),
    path('dashboard/',site.dashboard,name='dashboard'),

    # urls api
    path('clinicare/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('clinicare/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('clinicare/api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('',include(router.urls))
]
