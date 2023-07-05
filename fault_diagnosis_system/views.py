from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
# from background_task import background
import json


@login_required
def index(request):
    return render(request, 'index.html')


# @background
# def diagnosis():
#     print("诊断任务执行")
#     pass


@login_required
def upload_diagnosis(request):
    if request.method == 'POST':
        form = forms.DiagnosisTaskForm(request.POST, request.FILES)
        if form.is_valid():
            diagnosis_task = form.save(commit=False)
            diagnosis_task.owner = request.user
            diagnosis_task.diagnosis_status = "pending"
            diagnosis_task.save()
            # diagnosis.delay()
            return render(request, 'upload_diagnosis.html',
                          {'form': forms.DiagnosisTaskForm(), 'msg': diagnosis_task.uploaded_file.name})
        else:
            return render(request, 'upload_diagnosis.html', {'form': forms.DiagnosisTaskForm(), 'msg': '上传文件错误'})
    elif request.method == 'GET':
        return render(request, 'upload_diagnosis.html', {'form': forms.DiagnosisTaskForm()})
    else:
        return HttpResponse("请求格式不支持")


# @background
# def train():
#     print("训练任务执行")
#     pass


@login_required
def upload_train(request):
    if request.method == 'POST':
        form = forms.TrainTaskForm(request.POST, request.FILES)
        if form.is_valid():
            train_task = form.save(commit=False)
            train_task.owner = request.user
            train_task.diagnosis_status = "pending"
            train_task.save()
            # train.delay()
            return render(request, 'upload_train.html',
                          {'form': forms.TrainTaskForm(), 'msg': train_task.uploaded_file.name})
        else:
            return render(request, 'upload_train.html', {'form': forms.TrainTaskForm(), 'msg': '上传文件错误'})
    elif request.method == 'GET':
        return render(request, 'upload_train.html', {'form': forms.TrainTaskForm()})
    else:
        return HttpResponse("请求格式不支持")


@login_required
def diagnosis_tasks_list(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        diagnosis_tasks = models.DiagnosisTask.objects.filter(owner=request.user)
        return render(request, 'diagnosis_tasks_list.html', {'diagnosis_tasks': diagnosis_tasks})
    else:
        return HttpResponse("请求格式不支持")


@login_required
def diagnosis_task_detail(request, task_id):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        task = get_object_or_404(models.DiagnosisTask, id=task_id)
        if task.diagnosis_result_file:
            json_data = json.load(task.diagnosis_result_file.file)
            json_data = json.dumps(json_data)
        else:
            json_data = {}
        return render(request, 'diagnosis_task_detail.html',
                      {'task': task, 'diagnosis_result_json_data': json_data})
    else:
        return HttpResponse("请求格式不支持")


@login_required
def train_tasks_list(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        train_tasks = models.TrainTask.objects.filter(owner=request.user)
        return render(request, 'train_tasks_list.html', {'train_tasks': train_tasks})
    else:
        return HttpResponse("请求格式不支持")


@login_required
def train_task_detail(request, task_id):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        task = get_object_or_404(models.TrainTask, id=task_id)
        if task.train_result_file:
            json_data = json.load(task.train_result_file.file)
            json_data = json.dumps(json_data)
        else:
            json_data = {}
        return render(request, 'train_task_detail.html',
                      {'task': task, 'train_result_json_data': json_data})
    else:
        return HttpResponse("请求格式不支持")


def user_login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/index')
        return render(request, 'login.html', {'msg': '用户名或密码错误', 'form': forms.LoginForm()})
    elif request.method == 'GET':
        return render(request, 'login.html', {'form': forms.LoginForm()})
    else:
        return HttpResponse("请求格式不支持")


def user_logout(request):
    logout(request)
    return redirect('/login')


def about_page(request):
    return render(request, 'about.html')
