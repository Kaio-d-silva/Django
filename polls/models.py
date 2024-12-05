from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
 
   
class endereco(models.Model):
#     id = models.AutoField()
    rua = models.CharField(max_length=30)
#     bairro = models.CharField(max_length=20)
#     cidade = models.CharField(max_length=20)
#     numero = models.IntegerField()
    
# class paciente(models.Model):
#     id = models.AutoField()
#     endereco_id = models.ForeignKey(endereco)
#     nome = models.CharField(max_length=40)
#     data_nascimento = models.DateTimeField()
#     cpf = models.IntegerField()
#     telefone = models.IntegerField()
    

# class clinica(models.Model):
#     id = models.AutoField()
#     endereco_id = models.ForeignKey(endereco)
#     nome = models.CharField(default=30)
#     cnpj = models.IntegerField()
    
    
# class profissional_clinica(models.Model):
#     id = models.AutoField()
#     tipo = 0
#     nome = 0
#     registro_profissional = 0
#     tipo_registro = 0
    

    