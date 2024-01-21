from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

User = get_user_model()

class CustomUser(models.Model):
    user_custom = models.OneToOneField(User,on_delete=models.PROTECT ,related_name='user_custom',null=True)
    cpf = models.CharField(max_length=14,default='000.000.000-00',unique=True)
    telefone = models.CharField(max_length=15,blank=True,null=True)
    is_profissional_saude = models.BooleanField(default=False)

class Endereco(models.Model):
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=255,blank=True,null=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=50,blank=True,null=True)
    pais = models.CharField(max_length=100)

class Conselho(models.Model):
    nome = models.CharField(max_length=100)

class ProfissionalSaude(models.Model):
    user_profissional = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    especialidade = models.CharField(max_length=100)
    enderecos_atendimento = models.ManyToManyField(Endereco,related_name='profissionais_atendimento',blank=True)

    conselho = models.ForeignKey(Conselho,on_delete=models.SET_NULL, null=True, blank=True)
    numero_conselho = models.CharField(max_length=50,blank=True,null=True)

class Paciente(models.Model):
    user_paciente = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    idade = models.IntegerField(validators=[MinValueValidator(0)])
    peso = models.DecimalField(max_digits=5,decimal_places=2, validators=[MinValueValidator(0)])
    sexo = models.CharField(max_length=20)
    endereco = models.ForeignKey(Endereco,on_delete=models.SET_NULL,null=True,blank=True)

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE, related_name='consultas')
    profissional_saude = models.ForeignKey(ProfissionalSaude, on_delete=models.CASCADE, related_name='consultas')
    data_hora = models.DateField()
    descricao = models.TextField()
    local_atendimento = models.ForeignKey(Endereco,on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Consulta para {self.paciente.user.username} com {self.profissional_saude.user.username} em {self.data_hora.strftime('%d/%m/%Y %H:%M')}"
    
    class Meta:
        ordering = ['-data_hora']

