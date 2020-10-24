import datetime
from django.shortcuts import render,get_list_or_404
from django.views.generic import ListView,TemplateView, DetailView
from .models import Post,segmento_inferior,Noticias_Recientes,Most_Popular,Videos,Opinion,Post_de_Interes,vistas
from datetime import date
from django.db.models import Q
from Aplicacion_web.forms import  FormularioContacto
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


# Create your views here.

# def buscar(request):

#     print(request.GET)
#     queryset = request.GET.get("buscar")
#     posts = Post.objects.filter(publicado = True)

#     if queryset:

#         posts = Post.objects.filter(

#             Q(Titulo__icontains = queryset) |
#             Q(descripcion__icontains = queryset)


#         ).distinct()

#     return render(request,'base.html',{'posts':posts})


def contacto(request):


    if request.method=="POST":

        miformulario=FormularioContacto(request.POST)

        if miformulario.is_valid():
    
            infForm=miformulario.cleaned_data
            full_message = infForm['mensaje'] + "<br> Atte:    "+ infForm['Email']
            send_mail(infForm['asunto'],full_message,infForm.get('email',''),['wilfredofrias146@gmail.com'],html_message=full_message)

        return render(request,"gracias.html")



    else:

        miformulario=FormularioContacto()

        return render(request,"formulario_contacto.html",{"form":miformulario})





class Buscarview(TemplateView):
    def get(self, request,*args,**kwargs):
        buscar = request.GET['buscalo']
        print = (buscar)
        hoy = date.today()
        post = Post.objects.filter(Titulo__contains=buscar)
        reciente = Noticias_Recientes.objects.filter(Titulo__contains=buscar)


        context={}
        
        context['contenidos'] =  Post.objects.filter(fecha_publicacion__year=hoy.year, fecha_publicacion__month=hoy.month,
                                          fecha_publicacion__day=hoy.day).order_by('?')[:10]
        context['segmentos'] = segmento_inferior.objects.all()

        context['recientes'] = Noticias_Recientes.objects.all()

        context['populares'] = Most_Popular.objects.all()
        context['videos'] = Videos.objects.all()

        context['opiniones'] = Opinion.objects.all()
        context['contenidos'] = post

        return render(request,'base.html',context)




class Inicio(TemplateView):
    model = Post
    template_name = 'base.html'

    hoy = date.today()
    noticias_de_hoy = Post.objects.filter(fecha_publicacion__year=hoy.year, fecha_publicacion__month=hoy.month,
                                          fecha_publicacion__day=hoy.day).order_by('?')[:20]








    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = date.today()
        #context['contenidos'] = Post.objects.all()
        context['contenidos'] =  Post.objects.filter(fecha_publicacion__year=hoy.year, fecha_publicacion__month=hoy.month,
                                          fecha_publicacion__day=hoy.day).order_by('?')[:10]
        context['segmentos'] = segmento_inferior.objects.all()

        context['recientes'] = Noticias_Recientes.objects.all()

        context['populares'] = Most_Popular.objects.all()
        context['videos'] = Videos.objects.all()

        context['opiniones'] = Opinion.objects.all()

        return context






        



class detalleView(DetailView):
    model = Post
    template_name = 'detalles_noticias.html'
    def get_context_data(self, **kwargs):
        #usamos el get_context que viene por default en el DetailView
        context = super().get_context_data(**kwargs)
        #los parametros que se mandan por url se iran al dic de kargs por eso el self.kwargs['pk']
        #context['post'] =Post.objects.get(pk=self.kwargs['pk'])
        context['post'].Contador_visitas = context['post'].Contador_visitas + 1
        context['post'].save()
        context['DeInteres'] = Post_de_Interes.objects.all()
      
        return context

        def get_object(self, **kwargs):
            object = super().get_object(**kwargs)

            if self.request.user.is_authenticated:
                vistas.objects.get_or_create(user=self.request.user,post=object) 


            
            return object





class detallesegmentos(DetailView):
        model = segmento_inferior
        template_name = 'segmento_inferior.html'


class detalles_noticias(DetailView):
    model = Noticias_Recientes
    template_name = 'noticias_recientes.html'

    #matodo para conexto
    def get_context_data(self, **kwargs):
     
        context = super().get_context_data(**kwargs)

        context['Noticias_Recientes'] = Noticias_Recientes.objects.get(pk=self.kwargs['pk'])

        return context




class deportes(TemplateView):
    model = Post
    template_name = 'deportes.html'
    hoy = date.today()
    noticias_de_hoy = Post.objects.filter(fecha_publicacion__year=hoy.year, fecha_publicacion__month=hoy.month,
                                          fecha_publicacion__day=hoy.day).order_by('?')[:20]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = date.today()
        # context['contenidos'] = Post.objects.all()
        context['contenidos'] = Post.objects.filter(categoria__nombre = "Deporte")

        return context



class musica(TemplateView):

    model = Post
    template_name = 'musica.html'
    hoy = date.today()
    noticias_de_hoy = Post.objects.filter(fecha_publicacion__year=hoy.year, fecha_publicacion__month=hoy.month,
                                          fecha_publicacion__day=hoy.day).order_by('?')[:20]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = date.today()
        # context['contenidos'] = Post.objects.all()
        context['contenidos'] = Post.objects.filter(categoria__nombre = "Música")

        return context


class politica(TemplateView):

    model = Post
    template_name = 'Politica.html'
    hoy = date.today()
    noticias_de_hoy = Post.objects.filter(fecha_publicacion__year=hoy.year, fecha_publicacion__month=hoy.month,
                                          fecha_publicacion__day=hoy.day).order_by('?')[:20]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = date.today()
        # context['contenidos'] = Post.objects.all()
        context['contenidos'] = Post.objects.filter(categoria__nombre = "Politica Nacional")

        return context




class OpinionView(TemplateView):

    model = Opinion
    template_name = 'opinion.html'
    hoy = date.today()
    #noticias_de_hoy = Opinion.objects.all() y qui 
    # ? /-.-
    #dame 5 minutos tengo que atender algo... si listo si 
    noticias_de_hoy = Opinion.objects.filter(fecha_publicacion__year=hoy.year, fecha_publicacion__month=hoy.month,
                                          fecha_publicacion__day=hoy.day).order_by('?')[:20]


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = date.today()
        # context['contenidos'] = Post.objects.all()
        context['contenidos'] = Opinion.objects.all()

        return context




class detalleViewopinion(DetailView):
    model = Opinion
    template_name = 'detalles_opinion.html'
    def get_context_data(self, **kwargs):
       
        context = super().get_context_data(**kwargs)

        context['contenidos'] =Opinion.objects.get(pk=self.kwargs['pk'])

        return context



























