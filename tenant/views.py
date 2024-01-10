from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.db.models import Q
from .models import Tenant

# Create your views here.
class TenantView(View):
    template_name = 'tenant/index.html'

    def get(self, request, *args, **kwargs):
        tenant = Tenant.objects.all()
        search_query = ""
        context = {"tenants": tenant, "search_query": search_query}
        return render(request, self.template_name, context=context)