from django.core.mail     import EmailMessage, send_mail
from django.shortcuts 	  import render_to_response
from django.http      	  import HttpResponseRedirect
from django.db.models     import Count, Avg
from django.template  	  import RequestContext
from django.views.generic import CreateView, ListView

import datetime

from django.core.urlresolvers import reverse_lazy
from django.core.paginator    import Paginator, EmptyPage, InvalidPage

'''Librerias de Authentication '''
from django.contrib.auth 			 import login,logout,authenticate
#from django.contrib.auth.models      import User
from django.contrib.auth.forms 		 import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators	 import login_required

'''Librerias App'''

from registro_estudiantes_oym.apps.home.forms      import LoginForm, sugerencias
from registro_estudiantes_oym.apps.registro.models import Estudiante, Correo, Materia, Capitulo, Subcapitulo, Seccion, TextoPrincipal, Profesor, Periodo, Calificacion, Grupo, Aviso, PreguntasRespuestas, LinkInteresante

def index_view(request):
    materia 	= Materia.objects.filter(id=2)    # Select * from materias
    capitulo    = Capitulo.objects.all()
    texto   	= TextoPrincipal.objects.all()	 # Despliega el texto de la pagina principal
    seccion    	= Seccion.objects.all()
    nom_prof    = Profesor.objects.all()
    periodo     = Periodo.objects.all()
    aviso       = Aviso.objects.all()
    hora        = datetime.datetime.now()
    ctx         = {'materia':materia, 'capitulo':capitulo, 'texto':texto, 'seccion':seccion, 'nom_prof':nom_prof, 'aviso':aviso, 'hora':hora}

    return render_to_response('home/index.html',ctx,context_instance=RequestContext(request))

def login_view(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/materia/')
	if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario  = authenticate(username=username, password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/materia/')

				else:
					return HttpResponseRedirect('/login/')
			else:
				return render_to_response('home/login.html',{'form':form},context_instance=RequestContext(request))
	else:
		form = LoginForm()
		ctx  = {'form':form}

		return render_to_response('home/login.html', ctx, context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')


#@login_required(login_url = '/login/')
class RegistrarEstudiante(CreateView):
    template_name = 'home/registro_estudiantes.html'
    model = Estudiante
    success_url = reverse_lazy('vista_reg_estudiante')

    
class LinkInteresante(ListView):
	model         = LinkInteresante
	queryset      = LinkInteresante.objects.all()

class ListadoView(ListView):
	'''Vista Listado Oficial Estudiante'''
	template = 'home/estudiante.html'
	model    = Estudiante
	context_object = 'estudiante'


class ListadoFAQ(ListView):
	'''Vista para Q&A'''
	template = 'home/pregunta_respuesta.html'
	model = PreguntasRespuestas
	queryset = PreguntasRespuestas.objects.all() #[:5] Escoger ultimas 5 
	#context_object = 'preguntasrespuestas'
	
'''
	def get_queryset(self):
		tags = [ pregunta.tag.all() for pregunta in self.queryset]
		return zip(self.queryset, tags)
'''

@login_required(login_url='/login/')
def registrados_view(request,pagina):
	mensaje   = 'Listado estudiantes registrados'
	lista_est = Estudiante.objects.all()
	correo    = Correo.objects.all()
	grupo     = Grupo.objects.all()
	paginator = Paginator(lista_est,3)
	try:
		page = int(pagina) #Convierte la cadena de caracteres tomadas en el url a entero /1/ o /2/.
	except:
		page = 1
	try:
		estudiante = paginator.page(page)
	except (EmptyPage,InvalidPage):
		estudiante = paginator.page(paginator.num_pages)

	ctx = {'msg':mensaje, 'correo':correo, 'grupo':grupo, 'estudiante':estudiante}

	return render_to_response('home/estudiantes_registrados.html',ctx,context_instance=RequestContext(request))


@login_required(login_url = '/login/')
def sugerencias_view(request):
	enviarInfo = False
	titulo = ""
	sugerencia = ""
	if request.method == "POST":
		formulario = sugerencias(request.POST)
		if formulario.is_valid():
			enviarInfo = True
			titulo = formulario.clean_data['titulo']
			sugerencia = formulario.clean_data['sugerencia']
	else:
		formulario = buzonSugerencias()
		ctx = {'form':formulario, 'titulo':titulo, 'sugerencia':sugerencia}

		return render_to_response('home/buzon_sugerencias.html',ctx,context_instance=RequestContext(request))

@login_required(login_url = '/login/')
def cert_gallery_view(request):
	return render_to_response('home/galeria_certificados.html',context_instance=RequestContext(request))


@login_required(login_url = '/login/')
def materia_view(request):
	materia_red = Materia.objects.filter(id=1)
	materia_nos = Materia.objects.filter(id=2)
	materia_vm  = Materia.objects.filter(id=3)
	nom_prof = Profesor.objects.all()
	ctx = {'materia_red':materia_red, 'materia_nos':materia_nos, 'materia_vm':materia_vm, 'nom_prof':nom_prof }
	return render_to_response('home/seleccionar_materia.html',ctx,context_instance=RequestContext(request))


@login_required(login_url = '/login/')
def capitulos_temas_view(request):
	mensaje    = 'PROGRAMA DE ASIGNATURA'
	materia    = Materia.objects.filter(id=2)
	capitulo   = Capitulo.objects.values('id','titulo', 'num_capitulo', 'contenido')
	#cap        = Capitulo.objects.values('num_capitulo')[0]
	#cap        = int(cap['num_capitulo'])
	subcapitulo= Subcapitulo.objects.values('subtitulo', 'num_subcapitulo', 'contenido') 
	ctx       = {'materia':materia, 'capitulo':capitulo, 'subcapitulo':subcapitulo, 'mensaje':mensaje}

	return render_to_response('home/indice_temas_SOII.html',ctx,context_instance=RequestContext(request))


@login_required(login_url = '/login/')
def tema_net_view(request):
	mensaje   = 'PROGRAMA DE ASIGNATURA'
	ctx       = {'mensaje':mensaje}

	return render_to_response('home/indice_tema_networking.html',ctx,context_instance=RequestContext(request))


@login_required(login_url = '/login/')
def tema_vm_view(request):
	mensaje   = 'PROGRAMA DE ASIGNATURA'
	ctx       = {'mensaje':mensaje}

	return render_to_response('home/indice_tema_virtualizacion.html',ctx,context_instance=RequestContext(request))


@login_required(login_url = '/login/')
def audiovisuales_view(request):
	return render_to_response('home/audiovisuales.html',context_instance=RequestContext(request))


@login_required(login_url = '/login/')
def rep_calificaciones_view(request):
	calificacion  = Calificacion.objects.all()
	conteo_std    = Estudiante.objects.count()
	prom_asis     = Calificacion.objects.all().aggregate(Avg('asistencia'))
	prom_prct     = Calificacion.objects.all().aggregate(Avg('pract_ind_1'))
	prom_prcl     = Calificacion.objects.all().aggregate(Avg('parcial'))
	prom_fnl      = Calificacion.objects.all().aggregate(Avg('final'))
	ctx           = {'conteo_std':conteo_std, 'prom_asis':prom_asis, 'prom_prcl':prom_prcl, 'prom_fnl':prom_fnl, 'calificacion':calificacion} 
	return render_to_response('home/reporte_calificaciones.html',ctx,context_instance=RequestContext(request))


@login_required(login_url = '/login/')
def reglamento_view(request):
	mensaje = 'Reporte Informativo'
	ctx = {'mensaje':mensaje}

	return render_to_response('home/reglamento.html',ctx,context_instance=RequestContext(request))

def about_view(request):
	mensaje = 'Aplicacion de control de estudiantes...creada por Kennedy Sanchez para uso personal'
	ctx = {'msg':mensaje}

	return render_to_response('home/about.html',ctx,context_instance=RequestContext(request))

def current_datetime(request):
	hr_actual = datetime.datetime.now()
	ctx       = {'hr_actual':hr_actual}

	return render_to_response('home/index.html',ctx,context_instance=RequestContext(request))

def send_email(request):
	msg = EmailMessage(subject='Bienvenida',
						from_email= 'Sistema O&M <ing-ksanchez@hotmail.com',
						to = ['ing-ksanchez'])
	msg.template_name = 'aviso_cuenta_oym'
	msg.template_content = {

		'std_content00' : '<h1>Hola %s Ha sido registrado en el sistema.</h1>' % request.user
	}

	msg.send()

