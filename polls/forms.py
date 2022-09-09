from pyexpat import model
from secrets import choice
from django import forms
from polls.models import Question, Choice
from django.contrib import admin
from django.forms import formset_factory


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']


class ChoiceForm(forms.ModelForm):
    # question = forms.CharField(max_length=200)
    # inlines = [ChoiceInline]
    class Meta:
        model = Choice
        fields = ['question','choice_text']
        



class ChoiceInline(forms.Form):
    choice = formset_factory(ChoiceForm, extra=2)

