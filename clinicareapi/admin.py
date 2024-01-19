from django.contrib import admin

# Register your models here.
from .models import CustomUser,Endereco, Conselho, ProfissionalSaude, Paciente, Consulta

admin.site.register(CustomUser)
admin.site.register(Endereco)
admin.site.register(Conselho)
admin.site.register(ProfissionalSaude)
admin.site.register(Paciente)
admin.site.register(Consulta)