from django.http import JsonResponse, HttpResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        json_data = {"code": 1, "msg": "文件上传成功"}
        return JsonResponse(json_data)
    else:
        return HttpResponse("请使用POST请求数据")
