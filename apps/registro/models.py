from django.db import models

class Profesor(models.Model):
	nombre           = models.CharField(max_length=45, null=False)
	apellido 		 = models.CharField(max_length=45, null=False)
	
	
	def __unicode__(self):
		nombre_profesor = "%s %s" % (self.nombre, self.apellido)
		return "%s" % (nombre_profesor)


class Titulacion(models.Model):
	profesor         = models.ForeignKey(Profesor)
	certificaciones	 = models.CharField(max_length=255)
	profesion		 = models.CharField(max_length=45)
	

class Grupo(models.Model):
	num_grp    		 = models.CharField(max_length=2, verbose_name='Numero de grupo')

	def __unicode__(self):
		num_grp      = "%s" % (self.num_grp)
		return "%s" 		% (num_grp)


class Estudiante(models.Model):
	grupo            = models.ForeignKey(Grupo)
	SEXO 			 = (('M', 'Masculino'),('F', 'Femenino'),)	
	matricula    	 = models.CharField(max_length=20, unique=True) 
	nombre       	 = models.CharField(max_length=45)
	apellido     	 = models.CharField(max_length=45) 
	genero       	 = models.CharField(max_length=1, choices=SEXO)
	telefono     	 = models.CharField(max_length=11, null=True, blank=True)
	fechareg         = models.DateTimeField(auto_now=True)
	status           = models.BooleanField(default=True)
	foto        	 = models.ImageField(upload_to='images/usuarios', null=True, blank=True, verbose_name="Foto")
	
	
	def __unicode__(self):
		nombre_completo = "%s %s" % (self.nombre, self.apellido)
		matricula 	= "%s"    % (self.matricula)
	        fecha_registro  = "%s"% (self.fechareg)
		return "%s, %s, %s"         % (nombre_completo, matricula, fecha_registro)
    
# Este campo es necesario para registrar mas de un correo de estudiantes

class Correo(models.Model):
	estudiante      = models.ForeignKey(Estudiante, null=True, blank=True)
	profesor        = models.ForeignKey(Profesor, null=True, blank=True)
	correo          = models.EmailField(max_length=75, unique=True, null=True)

	def __unicode__(self):
		correo = "%s" % (self.correo)
		return "%s"   % (correo)


class Calificacion(models.Model):
	estudiante       = models.ForeignKey(Estudiante)
	asistencia  	 = models.CharField(max_length=3, null=True, blank=True)
	pract_ind_1      = models.CharField(max_length=3, null=True, blank=True)
	pract_ind_2      = models.CharField(max_length=3, null=True, blank=True)
	pract_grp_1      = models.CharField(max_length=3, null=True, blank=True)
	parcial		     = models.CharField(max_length=3, null=True, blank=True)
	participacion    = models.CharField(max_length=1, null=True, blank=True)
	final            = models.CharField(max_length=3, null=True, blank=True)
		
	
	
	def __unicode__(self):
		asistencia   = "%s" % (self.asistencia)
		pract_ind_1  = "%s" % (self.pract_ind_1)
		pract_ind_2  = "%s" % (self.pract_ind_2)
		pract_grp_1  = "%s" % (self.pract_grp_1)
		parcial      = "%s" % (self.parcial)
		final        = "%s" % (self.final)
		#total        = int(asistencia) + int(pract_ind_1) + int(pract_ind_2) + int(pract_grp_1) + int(parcial) + int(final)
		return "%s %s %s %s %s %s" % (asistencia, pract_ind_1, pract_ind_2, pract_grp_1, parcial, final)

	def __NotaFinal__(self):
		return self.asistencia + self.pract_ind_1 + self.pract_ind_2 + self.pract_grp_1 + parcial + final
		nota_final  = property(__NotaFinal__)


class Seccion(models.Model):
	prof             = models.ForeignKey(Profesor)
	num_seccion      = models.CharField(max_length=3)

	def __unicode__(self):
		num_seccion  = "%s" % (self.num_seccion)
		return "%s"         % (num_seccion)


class Materia(models.Model):
	prof    = models.ForeignKey(Profesor, verbose_name='Nombre Profesor')
	secc    = models.ForeignKey(Seccion, verbose_name='Seccion')
	name    = models.CharField(max_length=100, verbose_name='Nombre Materia')
	detail  = models.TextField(verbose_name='Descripcion')
    

	def __unicode__(self):
		materia 	 = "%s" % (self.name)
		return "%s" 		% (materia)


class Capitulo(models.Model):
	materia          = models.ForeignKey(Materia)
	num_capitulo     = models.CharField(max_length="3",  null=True, blank=True)
	titulo           = models.CharField(max_length="255", null=True, blank=True)
	contenido        = models.CharField(max_length="255", null=True, blank=True)


	def __unicode__(self):
		num_capitulo = "%s" % (self.num_capitulo)
		titulo       = "%s" % (self.titulo)
		contenido    = "%s" % (self.contenido)
		return "%s %s %s"   % (num_capitulo, titulo, contenido)


class Subcapitulo(models.Model):
	capitulo         = models.ForeignKey(Capitulo)
	num_subcapitulo  = models.CharField(max_length="3",  null=True, blank=True)
	subtitulo        = models.CharField(max_length="255", null=True, blank=True)
	contenido        = models.CharField(max_length="255", null=True, blank=True)

	def __unicode__(self):
		num_subcapitulo = "%s" % (self.num_subcapitulo)
		subtitulo       = "%s" % (self.subtitulo)
		contenido    = "%s" % (self.contenido)
		return "%s %s %s"   % (num_subcapitulo, subtitulo, contenido)


class Periodo(models.Model):
	fdesde			 = models.DATE_FORMAT = 'N j, Y'
	fhasta			 = models.DATE_FORMAT = 'N j, Y'

	def __unicode__(self):
	    fdesde       = "%s" % (self.fdesde)	
	    fhasta       = "%s" % (self.fhasta)	

	    return "%s %s" % (fdesde, fhasta)

class Sugerencia(models.Model):
	titulo           = models.CharField(max_length=45)
	sugerencia       = models.CharField(max_length=255)
	fechareg         = models.DateTimeField(auto_now=True)
	
	estudiante		 = models.ForeignKey(Estudiante)

	def __unicode__(self):
		titulo       = "%s" % (self.titulo)
		sugerencia   = "%s" % (self.sugerencia)

		return "%s %s" (titulo, sugerencia)


class PreguntasRespuestas(models.Model):
	'''Cuestionario realizado por los estudiantes'''
	estudiante  = models.ForeignKey(Estudiante)
	pregunta    = models.CharField(max_length=255, unique=True)
	respuesta   = models.TextField()
	fechareg    = models.DateTimeField(auto_now=True)
	status      = models.BooleanField(default=True)

	def __unicode__(self):
		pregunta     = "%s" % (self.pregunta)
		respuesta    = "%s" % (self.respuesta)

		return "%s %s" %(pregunta, respuesta)


class ReglaPuntuacion(models.Model):
    asistencia   = models.CharField(max_length=2)
    pts_trb_ind1 = models.CharField(max_length=2)
    pts_trb_ind2 = models.CharField(max_length=2)
    pts_trb_grp1 = models.CharField(max_length=2)
    parcial  = models.CharField(max_length=2)
    exam_fnl = models.CharField(max_length=2)
    trab_prn = models.CharField(max_length=7)
    trab_dig = models.CharField(max_length=7)
    cant_pag_ind   = models.CharField(max_length=2)
    cant_pag_grp   = models.CharField(max_length=2)
    cant_preg_ind  = models.CharField(max_length=2)
    cant_preg_grp  = models.CharField(max_length=2)
    tipo_letra   = models.CharField(max_length=30)
    tamano_letra = models.CharField(max_length=6)
    diapositiva  = models.CharField(max_length=2)
    tiempo_estimado = models.CharField(max_length=20)


class TextoPrincipal(models.Model):
	descripcion_txt = models.TextField()
	status          = models.BooleanField(default=True)

	def __unicode__(self):
		return self.descripcion_txt


class Aviso(models.Model):
	detalle  = models.CharField(max_length=100, null=True, blank=True, unique=True)
	status   = models.BooleanField(default=True)

	def __unicode__(self):
		return self.detalle


class LinkInteresante(models.Model):
    titulo_nos = models.CharField(max_length=100, null=True, blank=True)
    nos = models.URLField(null=True, blank=True)
    titulo_virtualizacion = models.CharField(max_length=100, null=True, blank=True)
    virtualizacion = models.URLField(null=True, blank=True)
    titulo_redes   = models.CharField(max_length=100, null=True, blank=True)
    redes          = models.URLField(null=True, blank=True)

    def __unicode__(self):
    	link = "%s %s %s" % (self.titulo_nos, self.titulo_virtualizacion, self.titulo_redes)
    	return link
