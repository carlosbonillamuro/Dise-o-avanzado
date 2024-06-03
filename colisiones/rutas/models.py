from django.db import models

CARGO=[
    ('1','Maquinista'),
    ('2','Ayudante de Maquinista'),
    ('3','Garrotero')
]

RUTAS=[
    ('1','AGUASCALIENTES'),
    ('2','AJUNO'),
    ('3','CD FRONTERA'),
    ('4','CDMX'),
    ('5','CELAYA'),
    ('6','CHIHUAHUA'),
    ('7','COATZACOALCOS'),
    ('8','CULIACAN'),
    ('9','EL PASO'),
    ('10','GUADALAJARA'),
    ('11','GUAYMAS'),
    ('12','HERMOSILLO'),
    ('13','IRAPUATO'),
    ('14','LOS MOCHIS'),
    ('15','MANZANILLO'),
    ('16','MAZATLAN'),
    ('17','MEXICALI'),
    ('18','MONTERREY'),
    ('19','NACOZARI'),
    ('20','NOGALES'),
    ('21','OJINAGA'),
    ('22','PIEDRAS NEGRAS'),
    ('23','PUEBLA'),
    ('24','RAMOS ARISPE'),
    ('25','SALINA CRUZ'),
    ('26','SALTILLO'),
    ('27','SILAO'),
    ('28','TAMPICO'),
    ('29','TEPIC'),
    ('30','TOPOLOBAMBO'),
    ('31','TORREON'),
    ('32','VERACRUZ'),
    ('33','VERECRUZ'),
    ('34','ZACATECAS')

]

class rutas(models.Model):
    viajes = models.CharField("No de viaje",max_length=20,null=True,blank=True)
    maquina = models.ForeignKey("rutas.Trenes",verbose_name="No de Maquina",on_delete=models.DO_NOTHING)
    maquinista=models.ForeignKey("rutas.Personal",verbose_name="Capitan de viaje",on_delete=models.DO_NOTHING)
    origen=models.CharField('Origen',max_length=2,choices=RUTAS)
    destino=models.CharField('Destino',max_length=2,choices=RUTAS)
    salida=models.DateField('Fecha de Salida',null=True,blank=True)
    llegada=models.DateField('Fecha de Llegada',null=True,blank=True)
    
        
    def __str__(self):
        return self.viajes
    

class Trenes(models.Model):
    idmaquina = models.CharField('No de la Maquina',max_length=10)
    idgps = models.CharField('ID del GPS',max_length=10)
    ubicacion = models.CharField('Ubicación',max_length=22)
    marca=models.CharField('Marca',max_length=15)
    modelo=models.CharField('Modelo',max_length=15)
    serie=models.CharField('No de serie',max_length=20)
    
    def __str__(self):
        return self.idmaquina
        

class Personal(models.Model):
    nombre=models.CharField('Nombre del trabajador',max_length=40)
    cargo=models.CharField('Puesto',max_length=1,choices=CARGO)
    empleado=models.CharField('No de empleado',max_length=20)
    licencia=models.CharField('No de licencia',max_length=20)
    ingreso=models.DateField('Fecha de ingreso',null=True,blank=True)
    segurosocial=models.CharField('No de Seguro Social',max_length=11)
    
    def __str__(self):
        return self.nombre
        