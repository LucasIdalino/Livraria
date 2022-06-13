import json

from core.models import Categoria
from django.views import View 
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator



@method_decorator(csrf_exempt, name='dispatch')
class CategoriasView(View):
    def get(self, request, id=None):
        if id:
            qs = Categoria.objects.get(id=id)
            data = {}
            data['id'] = qs.id
            data['descrição'] = qs.descrição
            return JsonResponse(data)
            
        else:
            data = list(Categoria.objects.values())
            formatted_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(formatted_data, content_type='application/json')


    def post(self, request):
        data_json = json.loads(request.body)
        nova_categoria = Categoria.objects.create(**data_json)
        data = {'id': nova_categoria.id, 'descricao': nova_categoria.descrição}
        return JsonResponse(data)

    def patch(self, request, id):
        json_data = json.loads(request.body)
        qs = Categoria.objects.get(id=id)
        qs.descrição = json_data['descrição']
        qs.save()
        data = {}
        data['id'] = qs.id
        data['descrição'] = qs.descrição
        return JsonResponse(data)

    def delete(self, request, id):
        qs = Categoria.objects.get(id=id)
        qs.delete()
        data = {'mensagem': 'Item excluido com sucesso.'}
        return JsonResponse(data)