from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.db.models import Q
from .models import School

class SchoolView(View):
    template_name = 'school/index.html'

    def get(self, request, *args, **kwargs):
        tenants = School.objects.all()
        search_query = ""
        context = {"tenants": tenants, "search_query": search_query}
        return render(request, self.template_name, context=context)