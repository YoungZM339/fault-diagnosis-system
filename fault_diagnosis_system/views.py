import time

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
from django.core.files.base import ContentFile
from fault_diagnosis_ml import pre_test_json
from fault_diagnosis_ml import train
import json
from threading import Thread


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def upload_diagnosis(request):
    if request.method == 'POST':
        form = forms.DiagnosisTaskForm(request.POST, request.FILES)
        if form.is_valid():
            diagnosis_task = form.save(commit=False)
            diagnosis_task.owner = request.user
            diagnosis_task.diagnosis_status = "pending"
            diagnosis_task.save()
            try:
                def predict_and_save_result():
                    diagnosis_task.diagnosis_status = "processing"
                    diagnosis_task.save()
                    # 因为速度太快不得不sleep3秒以展现功能
                    time.sleep(3)
                    pre_test_json.predict(diagnosis_task.uploaded_file.path, diagnosis_task.id)
                    with open(f"fault_diagnosis_ml/json/{diagnosis_task.id}.json", "r+") as f:
                        diagnosis_task.diagnosis_result_file.save(f"{diagnosis_task.id}.json",
                                                                  ContentFile(f.read(), f.name))
                    diagnosis_task.diagnosis_status = "completed"
                    diagnosis_task.save()

                # Run the diagnosis process in a separate thread
                Thread(target=predict_and_save_result).start()
                msg = diagnosis_task.uploaded_file.name
            except:
                msg = "detect出错，请检查上传文件或者后端运行是否正常"
            return render(request, 'upload_diagnosis.html',
                          {'form': forms.DiagnosisTaskForm(), 'msg': msg})
        else:
            return render(request, 'upload_diagnosis.html', {'form': forms.DiagnosisTaskForm(), 'msg': '上传文件错误'})
    elif request.method == 'GET':
        return render(request, 'upload_diagnosis.html', {'form': forms.DiagnosisTaskForm()})
    else:
        return HttpResponse("请求格式不支持")


@login_required
def upload_train(request):
    if request.method == 'POST':
        form = forms.TrainTaskForm(request.POST, request.FILES)
        if form.is_valid():
            train_task = form.save(commit=False)
            train_task.owner = request.user
            train_task.train_status = "pending"
            train_task.save()
            try:
                def train_and_save_result():
                    train_task.train_status = "processing"
                    train_task.save()
                    # 因为速度太快不得不sleep3秒以展现功能
                    time.sleep(3)
                    train.train(train_task.uploaded_file.path, train_task.id)
                    with open(f"fault_diagnosis_ml/modles/{train_task.id}.pkl", "rb") as f:
                        train_task.train_result_file.save(f"{train_task.id}.pkl", ContentFile(f.read(), f.name))
                    train_task.train_status = "completed"
                    train_task.save()

                # Run the training process in a separate thread
                Thread(target=train_and_save_result).start()
                msg = train_task.uploaded_file.name
            except:
                msg = "train出错，请检查上传文件或者后端运行是否正常"
            return render(request, 'upload_train.html',
                          {'form': forms.TrainTaskForm(), 'msg': msg})
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
        return render(request, 'train_task_detail.html',
                      {'task': task})
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
