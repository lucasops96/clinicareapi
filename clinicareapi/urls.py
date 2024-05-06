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
    path('register/healthcare/professional/',
         site.ProfissionalSaudeCreateView.as_view(),
         name='profissional_create_view'),
    path('detail/profissional/<int:pk>',
         site.ProfissionalSaudeDetailView.as_view(),
         name='profissional_detail_view'),
    path('update/profissional/<int:pk>',
        site.ProfissionalSaudeUpdateView.as_view(),
        name='profissional_update_view'),

    #paciente
    path('register/paciente',
         site.PacienteCreateView.as_view(),
         name='paciente_create_view'),
    
    #endereco
    path('endereco/list/',
        site.EnderecoListView.as_view(),
        name='endereco_list'),
    path('endereco/create/',
        site.EnderecoCreateView.as_view(),
        name='endereco_create'),
    path('endereco/update/<int:pk>',
        site.EnderecoUpdateView.as_view(),
        name='endereco_update'),
    path('endereco/delete/<int:pk>',
        site.EnderecoDeleteView.as_view(),
        name='endereco_delete'),

    path('login/',site.login_view,name='login'),
    path('login/create/',site.login_create,name='login_create'),
    path('logout/',site.logout_view,name='logout'),
    path('dashboard/',site.dashboard,name='dashboard'),
    path('senha/<int:pk>',site.alterar_senha,name='senha'),
    path('senha/alterada/<int:pk>',site.senha_alterada,name='senha_alterada'),

    # urls api
    path('clinicare/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('clinicare/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('clinicare/api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('',include(router.urls))
]
