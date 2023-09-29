from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages


# Create your views here.
layout = """


"""


def index(request):
    """
    html = ""
        <h1> INICIO!! </h1>
        <p> Años hasta el 2050:  </p>         
        <ul>
    ""

    year = 2023

    while year <= 2050:

        if year % 2 == 0:
            html += f" <li> {str(year)} </li>"
        year += 1

    html += "</ul>" 
    """
    year = 2023
    hasta = range(year, 2051)

    nombre = 'Cecilio José Avila2'
    lenguajes = ['JavaScript', 'Python', 'PHP', 'C']

    return render(request, 'index.html', {
        'title': 'Inicio',
        'mi_variable': 'Soy un dato que está en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta
    })


def hola_mundo(request):
    # http://127.0.0.1:8000/hola-mundo
    return render(request, 'hola_mundo.html')


def pagina(request, redirigir=0):

    if redirigir == 1:
        return redirect('/contacto/')

    return render(request, 'pagina.html', {
        'texto': 'Este es mi Texto original',
        'lista': ['Uno', 'Dos', 'Tres']
    })  # http://127.0.0.1:8000/pagina-pruebas/


def contacto(request, nombre=""):

    return HttpResponse(layout + f"<h2> Contacto {nombre}</h2>")


def crear_articulo(request, title, content, public):
    articulo = Article(
        title=title,
        content=content,
        public=public,
    )

    articulo.save()

    return HttpResponse(f"Articulo creado: <strong> {articulo.title}</strong> - {articulo.content}")


def save_article(request):
    # if request.method == 'GET':
    if request.method == 'POST':

        title = request.POST['title']  # title = request.GET['title']

        if len(title) <= 5:
            return HttpResponse("El titulo es muy pequeño")

        content = request.POST['content']  # content = request.GET['content']
        public = request.POST['public']  # content = request.GET['content']

        articulo = Article(
            title=title,
            content=content,
            public=public
        )

        articulo.save()

        return HttpResponse(f"Artículo creado: <strong> {articulo.title}</strong> - {articulo.title}")
    else:
        return HttpResponse("<h2> No se ha podido crear el artículo </h2>")


def create_article(request):

    return render(request, 'create_article.html')


def articulo(request):

    try:
        articulo = Article.objects.get(title="superman", public=True)
        response = f"Articulo: <br/> {articulo.id}. {articulo.title}"
    except:
        response = "<h1> Artículo no encontrado </h1>"

    return HttpResponse(response)


def editar_articulo(request, id):

    articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = "Película del 2017"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Artículo {articulo.id} editado: <strong> {articulo.title}</strong> - {articulo.content}")


def listar_articulos(request):

    # articulos = Article.objects.order_by('id')[01].exclude(
    #     public=False
    # )

    articulos = Article.objects.filter(public=True).order_by('-id')

    return render(request, 'articulos.html', {
        'articulos': articulos
    })


"""articulos = Article.objects.filter(id__lte=2, title__contains="1") 

        articulos = Article.objects.filter(
             Q(title__contains="2") | Q(public=True)
             ) 
               
            articulos = Article.objects.filter(
             title="Articulo",             
             
        ).exclude(
            public=False
         ) """

# articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title='Articulo 3' AND public=0")


def create_full_article(request):

    if request.method == 'POST':

        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']

            articulo = Article(
                title=title,
                content=content,
                public=public
            )

            articulo.save()

            # Crear mensaje flash (sesion que solo se muestra una vez)

            # lo mostramos en la vista de articulos.html
            messages.success(
                request, f'Has creado correctamente el artículo  {articulo.id} :(')

            return redirect('articulos')
            # return HttpResponse(articulo.title + '-' + articulo.content  + '-' + str(articulo.public))

    else:
        formulario = FormArticle()

    return render(request, 'create_full_article.html', {
        'form': formulario
    })


def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')
