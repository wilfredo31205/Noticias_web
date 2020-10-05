from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField
from django.shortcuts import reverse
from django.utils.text import slugify



# Aaui van mis modelos

class User(AbstractUser):
    pass


    def __str__(self):


        return self.username





class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=True)
    fecha_modificacion = models.DateField('Fecha de modificacion', auto_now=True, auto_now_add=False)
    fecha_eliminacion = models.DateField('Fecha de eliminacion', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class Categoria3(ModeloBase):
    nombre = models.CharField('Nombre de la categoria', max_length=100, unique=True)
    imagen_referencial = models.ImageField('Imagen referencial', upload_to='categoria/')

    # ageField('Imagen referencial',upload_to='categoria/') lo que hace es que carga la imagen en la carpeta llamada categoria#

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Autor(ModeloBase):
    nombre = models.CharField('nombre', max_length=100)
    apellidos = models.CharField('apellido', max_length=120)
    email = models.EmailField('Correo Electronico', max_length=200)
    descripcion = models.TextField('Descripcion')
    web = models.URLField('web1', null=True, blank=True)
    facebook = models.URLField('Facebook', null=True, blank=True)
    Twitter = models.URLField('Twiter', null=True, blank=True)
    Instagram = models.URLField('Instagram', null=True, blank=True)

    def __str__(self):
        return '{0}.{1}'.format( self.nombre,self.apellidos)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


class Post(ModeloBase):
    Titulo = models.CharField('Titulo del post', max_length=150, unique=True)
    slug = models.CharField('Slug', max_length=150, unique=True)
    descripcion = models.TextField('Descripcion')
    #autor3 = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria3, on_delete=models.CASCADE)
    contenido = RichTextField()
    imagen_preferencial = models.ImageField('Imagen preferencial', upload_to='imagenes/', max_length=255)
    publicado = models.BooleanField('Publicado / No publicado ', default=False)
    fecha_publicacion = models.DateField('Fecha de publicacion')
    Contador_visitas = models.IntegerField( default =0,blank=False, null=False)
    

    def __str__(self):
        return self.Titulo

    def get_absolute_url(self):
        return reverse("detail",kwargs={
            'slug': self.slug
        })

    @property
    def get_vistas_count(self):

        return self.vistas_set.all().count()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class vistas(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)




class web1(ModeloBase):
    nosotros = models.TextField('Nosotros')
    telefono = models.CharField('Telefono', max_length=10)
    email = models.EmailField('Correo Electronico', max_length=200)
    direccion = models.CharField('Direccion', max_length=200)

    class Meta:
        verbose_name = 'Web'
        verbose_name_plural = 'Webs'

    def __str__(self):
        return self.nosotros


class segmento_inferior(ModeloBase):
    imagen = models.ImageField('Imagen de la publicacion',upload_to='imagenes/', max_length=255)
    Titulo = models.CharField('Titulo del post', max_length=150, unique=True)
    Autor = models.CharField('Autor del post', max_length=100, unique=True)
    descripcion = RichTextField()
    contenido = RichTextField()


    def __str__(self):
        return self.Titulo


    class Meta:
        verbose_name = 'Segmento_inferior'
        verbose_name_plural = 'Segmentos_inferiores'


class Contacto(ModeloBase):
    nombre = models.CharField('Nombre', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=150)
    correo = models.EmailField('Correo electronico')
    asunto = models.CharField('asunto', max_length=100)
    mensaje = models.TextField('Mensaje')

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.correo


class Noticias_Recientes(ModeloBase):
    Portada  = models.ImageField('Imagen preferencial', upload_to='imagenes/', max_length=255)
    Titulo = models.CharField('Titulo',max_length=150)
    # contenido_noticias_Recientes = RichTextField()
    contenidos =RichTextField(default=True)


    def __str__(self):
        return self.Titulo

    class Meta:
        verbose_name = 'Noticia_Reciente'
        verbose_name_plural = 'Noticias_Recientes'






class Most_Popular(ModeloBase):
    noticia  = models.ForeignKey(Post,related_name="most_popular_today",on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    # fecha_creacion = models.DateField('Fecha de creacion', auto_now_add=True)


    def __str__(self):
        return self.noticia.Titulo

    def get_absolute_url(self):
        return reverse("detail",kwargs={
            'slug': self.slug
        })

        

    class Meta:
        verbose_name = 'Most_popular'
        verbose_name_plural = 'Most_populares'



class Post_de_Interes(ModeloBase):
    De_interes  = models.ForeignKey(Post,related_name="De_interes",on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    # fecha_creacion = models.DateField('Fecha de creacion', auto_now_add=True)


    def __str__(self):
        return self.De_interes.Titulo

    def get_absolute_url(self):
        return reverse("detail",kwargs={
            'slug': self.slug
        })

        

    class Meta:
        verbose_name = 'Intere'
        verbose_name_plural = 'interes'




class Videos(ModeloBase):
    Titulo  =  Titulo = models.CharField('Titulo del post', max_length=150, unique=True)
    video = models.FileField('Videos',  upload_to='videos/')


    def __str__(self):
        return self.Titulo

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'  


class Opinion(ModeloBase):
    Portada  = models.ImageField('Imagen preferencial', upload_to='imagenes/', max_length=255)
    Titulo = models.CharField('Titulo',max_length=150)
    #autor3 = models.ForeignKey(User, on_delete=models.CASCADE)
    contenidos1 = RichTextField(default=True)
    #autor3 = models.ForeignKey(Autor, on_delete=models.CASCADE,default=True)
    categoria = models.ForeignKey(Categoria3, on_delete=models.CASCADE,default=True)
    fecha_publicacion = models.DateField('Fecha de publicacion', auto_now_add=True,null=True)  
   #  Fecha_creacion = models.DateField('Fecha de creacion', auto_now_add=True)
    def __str__(self):
        return self.Titulo

   



    class Meta:
        verbose_name = 'Opinion'
        verbose_name_plural = 'Opiniones'



