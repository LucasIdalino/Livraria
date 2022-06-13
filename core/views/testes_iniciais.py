from django.http import HttpResponse


def teste(request):
    return HttpResponse('Olá Pessoas.')

def second_teste(request):
    return HttpResponse('Essa é a segunda página.')