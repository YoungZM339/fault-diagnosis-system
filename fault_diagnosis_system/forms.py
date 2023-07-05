from django import forms
from . import models


class LoginForm(forms.Form):
    title = "用户登录"
    username = forms.CharField(label="用户名", max_length=150, widget=forms.TextInput())
    password = forms.CharField(label="密码", max_length=150, widget=forms.PasswordInput())


class DiagnosisTaskForm(forms.ModelForm):
    title = "诊断任务表单"

    class Meta:
        model = models.DiagnosisTask
        fields = ['uploaded_file']


class TrainTaskForm(forms.ModelForm):
    title = "训练任务表单"

    class Meta:
        model = models.TrainTask
        fields = ['uploaded_file']
