from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .forms import UserLoginForm, UserRegisterForm


# Create your views here.
@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                json_data = {"code": 1, "msg": "登陆成功", "user": {"username": user.username, "email": user.email},
                             "time": timezone.now()}
            else:
                json_data = {"code": 0, "msg": "账号或密码错误"}
            return JsonResponse(json_data)
    else:
        return HttpResponse("请使用POST请求数据")


@csrf_exempt
def user_logout(request):
    logout(request)
    json_data = {"code": 1, "msg": "已执行退出命令", "time": timezone.now()}
    return JsonResponse(json_data)


@csrf_exempt
def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            data = user_register_form.cleaned_data
            user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password'])
            if user:
                login(request, user)
                json_data = {"code": 1, "msg": "注册成功", "user": {"username": user.username, "email": user.email},
                             "time": timezone.now()}
            else:
                json_data = {"code": 0, "msg": "注册失败，未知错误", "time": timezone.now()}
            return JsonResponse(json_data)
        else:
            return HttpResponse("请使用POST请求数据")


@csrf_exempt
def user_delete(request):
    if request.method == 'POST':
        username = request.POST['username']
        user = User.objects.get(username=username)
        user.delete()
        json_data = {"code": 1, "msg": "已经成功删除该账户", "time": timezone.now()}
        return JsonResponse(json_data)
    else:
        return HttpResponse("请使用POST请求数据")


@csrf_exempt
def user_get_profile(request):
    if request.method == 'POST':
        user = request.user
        if user.is_authenticated:
            json_data = {"code": 1, "msg": "已经成功获取该账户信息",
                         "user": {"username": user.username, "email": user.email}, "time": timezone.now()}
            return JsonResponse(json_data)
        else:
            json_data = {"code": 0, "msg": "未登录，无法获取用户信息"}
            return JsonResponse(json_data)
    else:
        return HttpResponse("请使用POST请求数据")
