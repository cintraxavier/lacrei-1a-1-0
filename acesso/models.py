from django.db import models



class Profissional (models.Model):
    identificacao = models.ForeignKey('acesso.Profissional', on_delete=models.CASCADE)
    anotacao = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='media')
    telefone = models.CharField(max_length=13)

    def __uncode__(self):
        return self.identificacao

class Paciente (models.Model):
    usuario = models.OneToOneField('acesso.Paciente', on_delete=models.SET_NULL, null=True)
    telefone = models.CharField(max_length=13)
    email = models.EmailField(verbose_name="email")

# Create your models here.


