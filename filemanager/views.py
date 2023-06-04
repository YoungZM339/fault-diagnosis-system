from django.http import JsonResponse, HttpResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


# Create your views here.
@csrf_exempt
def upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get('file', None)
        if uploaded_file is not None:
            fs = FileSystemStorage()
            fs.save(uploaded_file.name, uploaded_file)
            json_data = {"code": 1, "msg": "文件上传成功", "file": {"name": uploaded_file.name},
                         "time": timezone.now()}
        else:
            json_data = {"code": 0, "msg": "请检查表单提交中的name属性是否是file或者检查是否正确上传了文件"}
        return JsonResponse(json_data)
    else:
        return HttpResponse("请使用POST请求数据")
