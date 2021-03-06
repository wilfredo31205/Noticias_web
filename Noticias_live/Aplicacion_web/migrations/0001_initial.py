# Generated by Django 3.0.8 on 2020-09-28 00:00

import ckeditor.fields
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre')),
                ('apellidos', models.CharField(max_length=120, verbose_name='apellido')),
                ('email', models.EmailField(max_length=200, verbose_name='Correo Electronico')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('web', models.URLField(blank=True, null=True, verbose_name='web1')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('Twitter', models.URLField(blank=True, null=True, verbose_name='Twiter')),
                ('Instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Categoria3',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre de la categoria')),
                ('imagen_referencial', models.ImageField(upload_to='categoria/', verbose_name='Imagen referencial')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo electronico')),
                ('asunto', models.CharField(max_length=100, verbose_name='asunto')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
            },
        ),
        migrations.CreateModel(
            name='Noticias_Recientes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('Portada', models.ImageField(max_length=255, upload_to='imagenes/', verbose_name='Imagen preferencial')),
                ('Titulo', models.CharField(max_length=150, verbose_name='Titulo')),
                ('contenidos', ckeditor.fields.RichTextField(default=True)),
            ],
            options={
                'verbose_name': 'Noticia_Reciente',
                'verbose_name_plural': 'Noticias_Recientes',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('Titulo', models.CharField(max_length=150, unique=True, verbose_name='Titulo del post')),
                ('slug', models.CharField(max_length=150, unique=True, verbose_name='Slug')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('contenido', ckeditor.fields.RichTextField()),
                ('imagen_preferencial', models.ImageField(max_length=255, upload_to='imagenes/', verbose_name='Imagen preferencial')),
                ('publicado', models.BooleanField(default=False, verbose_name='Publicado / No publicado ')),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha de publicacion')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplicacion_web.Categoria3')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='segmento_inferior',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('imagen', models.ImageField(max_length=255, upload_to='imagenes/', verbose_name='Imagen de la publicacion')),
                ('Titulo', models.CharField(max_length=150, unique=True, verbose_name='Titulo del post')),
                ('Autor', models.CharField(max_length=100, unique=True, verbose_name='Autor del post')),
                ('descripcion', ckeditor.fields.RichTextField()),
                ('contenido', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Segmento_inferior',
                'verbose_name_plural': 'Segmentos_inferiores',
            },
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('Titulo', models.CharField(max_length=150, unique=True, verbose_name='Titulo del post')),
                ('video', models.FileField(upload_to='videos/', verbose_name='Videos')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.CreateModel(
            name='web1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('nosotros', models.TextField(verbose_name='Nosotros')),
                ('telefono', models.CharField(max_length=10, verbose_name='Telefono')),
                ('email', models.EmailField(max_length=200, verbose_name='Correo Electronico')),
                ('direccion', models.CharField(max_length=200, verbose_name='Direccion')),
            ],
            options={
                'verbose_name': 'Web',
                'verbose_name_plural': 'Webs',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='vistas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplicacion_web.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Post_de_Interes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('count', models.IntegerField(default=1)),
                ('De_interes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='De_interes', to='Aplicacion_web.Post')),
            ],
            options={
                'verbose_name': 'Intere',
                'verbose_name_plural': 'interes',
            },
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('Portada', models.ImageField(max_length=255, upload_to='imagenes/', verbose_name='Imagen preferencial')),
                ('Titulo', models.CharField(max_length=150, verbose_name='Titulo')),
                ('contenidos1', ckeditor.fields.RichTextField(default=True)),
                ('fecha_publicacion', models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de publicacion')),
                ('categoria', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicacion_web.Categoria3')),
            ],
            options={
                'verbose_name': 'Opinion',
                'verbose_name_plural': 'Opiniones',
            },
        ),
        migrations.CreateModel(
            name='Most_Popular',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('count', models.IntegerField(default=1)),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='most_popular_today', to='Aplicacion_web.Post')),
            ],
            options={
                'verbose_name': 'Most_popular',
                'verbose_name_plural': 'Most_populares',
            },
        ),
    ]
