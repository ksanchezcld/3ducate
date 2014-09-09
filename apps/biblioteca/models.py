from django.db import models

class Libro(models.Model):
	GENERO           = (('IG', 'Informatica General'), ('P','Programacion'), ('R','Redes y Protocolos'), ('I', 'Internet'), ('B', 'Base de Datos'), ('V', 'Virtualizacion'), ('S', 'Sistemas Operativos'), ('B', 'Bibliografia'), ('O', 'Otros'),)
	titulo			 = models.CharField(max_length=50)
	autor 			 = models.CharField(max_length=45, verbose_name='Nombre Autor')
	isbn			 = models.CharField(max_length=45, unique=True)	
	f_public		 = models.DateField(null=True, verbose_name='Fecha Publicacion')
	editorial        = models.CharField(max_length=25)
	num_pag			 = models.CharField(max_length=4)
	genero			 = models.CharField(max_length=50, choices=GENERO)
	website			 = models.URLField(null=True)
	port_f		     = models.ImageField(upload_to='media/images/portadas/libro/front', null=True, blank=True, verbose_name='Portada frontal')
	port_t 			 = models.ImageField(upload_to='media/images/portadas/back', null=True, blank=True, verbose_name='Portada trasera')

	def __unicode__(self):
		return self.autor

	def portadas(self,filename):
		path = 'media/images/libros/portada/'
		return path
