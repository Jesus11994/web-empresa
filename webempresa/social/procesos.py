from .models import Link 

def contexto_diccionario(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.Key] = link.url
    return ctx
