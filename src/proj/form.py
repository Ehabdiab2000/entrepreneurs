from django import forms
from .models import Join ,Project




class JoinForm(forms.ModelForm):
    class Meta:
        model = Join
        fields = ['name' ,'email','webiste','cv','message']



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ('owner','slug')


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ('owner','slug')