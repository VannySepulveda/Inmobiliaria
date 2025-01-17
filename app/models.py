from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES=[('arrendatario','Arrendatario'),
                          ('arrendador','Arrendador')]                        
    nombre = models.CharField(max_length=50, null=False, blank=False)
    rut=models.CharField(max_length=11, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    direccion = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=11, null=True, blank=True)
    correo = models.EmailField (max_length=50, null=True, blank=True)
    arrendador= models.CharField(max_length=12, choices=TIPO_USUARIO_CHOICES)
    def __str__(self):
       return f"{self.rut} : {self.nombre} {self.apellido}"
    
class Propiedad(models.Model):
    TIPO_PROPIEDAD_CHOISE=[
                          ('casa','Casa'),
                          ('departamento','Departamento'),
                          ('parcela','Parcela')
                          ]
    nombre= models.CharField(max_length=50, null=False, blank=False)
    direccion = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    imagen=models.ImageField(upload_to='',null=True,blank=True)
    m2construidos = models.DecimalField (max_digits=10, null=False, blank=False, default=0, decimal_places=0)
    m2totales = models.DecimalField (max_digits=10,null=False, blank=False, default=0, decimal_places=0)
    dormitorios = models.IntegerField (null=False, blank=False, default=1)
    estacionamientos = models.IntegerField (null=False, blank=False, default=1)
    banos = models.IntegerField (null=False, blank=False, default=1)
    comuna_id = models.CharField(max_length=50, null=False, blank=False)
    ciudad_id = models.CharField(max_length=50, null=False, blank=False)
    valor=models.IntegerField(null=False, blank=False, default=10)
    estado=models.BooleanField(default=False)
    arrendatario_id=models.OneToOneField(Usuario,on_delete=models.CASCADE)
    disponible=models.BooleanField(default=True)
    tipopropiedad=models.CharField(max_length=12, choices=TIPO_PROPIEDAD_CHOISE)
    def __str__(self):
        return f'{self.rut} : {self.nombre} {self.apellido}' 
    
class Region(models.Model):
    nombre=models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.nombre


     
    
class Solicitud_Arriendo(models.Model):
    TIPO_ESTADO_CHOISES=[('pendiente','Pendiente'),
                        ('aceptado','Aceptado'),
                        ('rechazado','Rechazado'),]
    arrendatario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    propiedad=models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    mensaje= models.TextField(null=True, blank=True)
    estado=models.CharField(choices=TIPO_ESTADO_CHOISES,default='pendiente')
    def __str__(self):
           return f"Solicitud de {self.propiedad.nombre} por {self.arrendatario.nombre} {self.arrendatario.apellido}"
    
        
class Comuna(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    region = models.ForeignKey(Region, related_name="comunas", on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre     