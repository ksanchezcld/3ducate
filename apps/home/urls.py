from django.conf.urls import patterns,url
from registro_estudiantes_oym.apps.home.views import RegistrarEstudiante, registrados_view, ListadoView, ListadoFAQ, LinkInteresante

# Class base View de paginacion, RegistradoView

urlpatterns = patterns('registro_estudiantes_oym.apps.home.views',
	url(r'^$','index_view',name='vista_principal'),
	url(r'^login/$','login_view'),
	url(r'^logout/$','logout_view'),
	url(r'^reg_estudiantes/$',RegistrarEstudiante.as_view(),name='vista_reg_estudiante'),
	#url(r'^registrados/$',RegistradoView.as_view(),name='vista_registrados'),
	url(r'^registrados/pagina/(?P<pagina>.*)/$','registrados_view',name='vista_registrados'), # El parentesis captura los datos del texto que coincide
	url(r'^certificados/$','cert_gallery_view',name='vista_certificados'),
	url(r'^audiovisuales/$','audiovisuales_view',name='vista_audiovisuales'),
	url(r'^materia/$','materia_view',name='vista_materia'),
	url(r'^temas/$','capitulos_temas_view',name='vista_temas'),
	url(r'^tema-networking/$','tema_net_view',name='vista_temas_net'),
	url(r'^tema-virtualizacion/$','tema_vm_view',name='vista_temas_vm'),
	url(r'^links-interesantes/$',LinkInteresante.as_view(),name='vista_link_interesante'),
	url(r'^reporte/$','rep_calificaciones_view',name='vista_reporte'),
	url(r'^listado/$', ListadoView.as_view(context_object_name="listado_estudiante"), name='Listado Estudiantes'),
	url(r'^reglamento/$','reglamento_view',name='vista_reglamento'),
	#url(r'^biblioteca/$','biblioteca_view',name='vista_biblioteca'),
	url(r'^sugerencias/$','sugerencias_view',name='vista_sugerencias'),
	url(r'^faq/$', ListadoFAQ.as_view(context_object_name="preguntasresp"), name='vista_faq'),
	url(r'^about/$','about_view',name='vista_about'),
	)
