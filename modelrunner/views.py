from django.http import HttpResponse, JsonResponse
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt

from models_functions.train import train
from models_functions.detect import detect
from models_functions.val import val


# Create your views here.
@csrf_exempt
def model_train(request):
    if request.method == 'POST':
        pass
    else:
        return HttpResponse("请使用POST请求数据")


@csrf_exempt
def model_detect(request):
    if request.method == 'POST':
        pass
    else:
        return HttpResponse("请使用POST请求数据")


@csrf_exempt
def model_val(request):
    if request.method == 'POST':
        pass
    else:
        return HttpResponse("请使用POST请求数据")


@csrf_exempt
def test_result(request):
    if request.method == 'POST':
        json_data = train()
        return JsonResponse(json_data)
    else:
        return HttpResponse("请使用POST请求数据")
