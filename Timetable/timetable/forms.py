from django import forms

from .models import Tag, Deadline


class DeadlineForm(forms.ModelForm):
    class Meta:
        model = Deadline
        exclude = ('user', )


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = '__all__'



