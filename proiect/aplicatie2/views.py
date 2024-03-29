from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie2.models import Companies


class CompaniesView(LoginRequiredMixin, ListView):
    model = Companies   # from models (din baza de date)
    template_name = 'aplicatie2/companies_index.html'


class CreateCompanieView(LoginRequiredMixin, CreateView):
    model = Companies
    fields = ['nume', 'website', 'tip_companie']
    template_name = 'aplicatie2/companies_form.html'

    def get_success_url(self):
        return reverse('companies:lista_companii')


class UpdateCompanieView(LoginRequiredMixin, UpdateView):
    model = Companies
    fields = ['nume', 'website', 'tip_companie']
    template_name = 'aplicatie2/companies_form.html'

    def get_success_url(self):
        return reverse('companies:lista_companii')


@login_required
def delete_companie(request, pk):
    Companies.objects.filter(id=pk).update(active=0)
    return redirect('companies:lista_companii')


@login_required
def activate_companie(request, pk):
    Companies.objects.filter(id=pk).update(active=1)
    return redirect('companies:lista_companii')
