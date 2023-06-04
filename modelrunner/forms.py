from django import forms


class ModelForm(forms.Form):
    filename = forms.CharField()
    batchsize = forms.CharField()
    epochs = forms.CharField()
