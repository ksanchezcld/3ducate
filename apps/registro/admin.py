from django.contrib import admin
from registro_estudiantes_oym.apps.registro.models import Estudiante, Correo, Calificacion, Materia, Periodo, Profesor, Capitulo, Subcapitulo, Grupo, Seccion, PreguntasRespuestas, ReglaPuntuacion, TextoPrincipal, Aviso, LinkInteresante
from registro_estudiantes_oym.apps.biblioteca.models import Libro

class EstudianteAdmin(admin.ModelAdmin):
	list_display  = ('status', 'matricula', 'nombre', 'apellido', 'grupo', 'genero', 'foto')
	list_filter   = ('matricula', 'nombre', 'apellido', 'genero', 'status')
	ordering      = ('matricula',)
	search_fields = ('matricula', 'nombre', 'apellido', 'telefono', 'genero', 'status')
	list_editable = ('nombre', 'apellido', 'grupo', 'genero', 'foto')


class CorreoAdmin(admin.ModelAdmin):
	list_display  = ('estudiante','correo')


class CalificacionAdmin(admin.ModelAdmin):
	fields  = ('estudiante', 'asistencia', 'pract_ind_1'), ('pract_ind_2', 'pract_grp_1', 'parcial'), ('participacion', 'final')
	list_display  = ('estudiante', 'asistencia', 'pract_ind_1', 'pract_ind_2', 'pract_grp_1', 'parcial', 'participacion', 'final',)
	list_editable = ('pract_ind_1', 'pract_ind_2', 'pract_grp_1', 'parcial', 'participacion', 'final',)


class ProfesorAdmin(admin.ModelAdmin):
	list_display  = ('nombre', 'apellido',)
	search_fields = ('nombre', 'apellido', 'correo',)


class MateriaAdmin(admin.ModelAdmin):
	list_display  = ('secc','prof', 'name', 'detail')
	

class CapituloAdmin(admin.ModelAdmin):
	list_display  = ('materia','num_capitulo','titulo', 'contenido',)
	ordering      = ('num_capitulo',)
	search_fields = ('materia','num_capitulo','titulo',)


class SubcapituloAdmin(admin.ModelAdmin):
	list_display  = ('capitulo','num_subcapitulo','subtitulo', 'contenido',)
	ordering      = ('num_subcapitulo',)
	search_fields = ('capitulo','num_subcapitulo','subtitulo',)


class ReglaPuntuacionAdmin(admin.ModelAdmin):
	list_display  = ('asistencia', 'pts_trb_ind1', 'pts_trb_ind2', 'pts_trb_grp1', 'parcial', 'exam_fnl', 'trab_prn', 'trab_dig', 'cant_pag_ind', 'cant_pag_grp', 'cant_preg_ind', 'cant_preg_grp', 'tipo_letra', 'tamano_letra', 'diapositiva', 'tiempo_estimado')


class TextoPrincipalAdmin(admin.ModelAdmin):
	list_display  = ('descripcion_txt','status')
	list_editable = ('status',)


class AvisoAdmin(admin.ModelAdmin):
	list_display  = ('detalle','status')
	list_editable = ('status',)


class PreguntasRespuestasAdmin(admin.ModelAdmin):
	list_display  = ('pregunta', 'respuesta', 'estudiante', 'status')
	list_editable = ('status','estudiante')
	list_filter   = ('estudiante', 'status')
	ordering      = ('id',)

class LinkInteresanteAdmin(admin.ModelAdmin):
	fields = ('titulo_nos', 'nos'), ('titulo_virtualizacion' ,'virtualizacion'), ('titulo_redes', 'redes',)
	list_display = ('nos', 'virtualizacion', 'redes')



class LibroAdmin(admin.ModelAdmin):
	list_display  = ('titulo', 'autor', 'isbn', 'f_public', 'editorial', 'genero', 'website', 'port_f')
	list_filter   = ('titulo', 'isbn', 'autor', 'f_public', 'editorial', 'genero', 'website',)
	ordering      = ('titulo', 'isbn', 'autor',)
	search_fields = ('titulo', 'isbn', 'autor', 'f_public', 'editorial', 'genero', 'website',)

admin.site.register(Estudiante, EstudianteAdmin),
admin.site.register(Correo, CorreoAdmin),
admin.site.register(Materia, MateriaAdmin),
admin.site.register(Calificacion, CalificacionAdmin),
admin.site.register(Capitulo, CapituloAdmin),
admin.site.register(Subcapitulo, SubcapituloAdmin),
admin.site.register(Periodo),
admin.site.register(Profesor, ProfesorAdmin),
admin.site.register(Grupo),
admin.site.register(Seccion),
admin.site.register(PreguntasRespuestas, PreguntasRespuestasAdmin),
admin.site.register(ReglaPuntuacion, ReglaPuntuacionAdmin),
admin.site.register(TextoPrincipal, TextoPrincipalAdmin),
admin.site.register(Aviso, AvisoAdmin),
admin.site.register(LinkInteresante, LinkInteresanteAdmin)
admin.site.register(Libro, LibroAdmin),