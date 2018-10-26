from django.shortcuts import render
from django.views.generic import ListView
from candidate.models import Candidate
from django.views.generic.edit import FormMixin, FormView
from candidate.forms import CandidateForm
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.

class Home(ListView, FormMixin):
    model = Candidate
    template_name = 'home.html'
    context_object_name = 'candidate'
    form_class = CandidateForm

    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, **kwargs):
        self.q = Candidate.objects.all()
        context = super(Home, self).get_context_data(**kwargs) 
        return context

    def get_queryset(self, **kwargs):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            q = Candidate.objects.filter(
                Q(skills__icontains=form.cleaned_data['skills'])&
                Q(preferred_loc__icontains=form.cleaned_data['loc'])&
                Q(work_exp__lte=form.cleaned_data['work_exp'])
            )
            return q
        return Candidate.objects.all()
