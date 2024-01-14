from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.db.models import Q
from .models import Tenant





class TenantView(View):
    template_name = 'tenant/index.html'

    def get(self, request, *args, **kwargs):
        tenants = Tenant.objects.all()
        search_query = ""
        context = {"tenants": tenants, "search_query": search_query}
        return render(request, self.template_name, context=context)
    

    def post(self, request, *args, **kwargs):
        tenants = Tenant.objects.all()
        search_query = ""

        if "create" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            # Verifica se o e-mail já existe
            existing_tenant = Tenant.objects.filter(email=email)
            if existing_tenant.exists():
                messages.warning(request, "E-mail já cadastrado por outro Grupo Escolar.")
                return redirect('tenant')

        # Continuação do seu código...
            new_tenant = Tenant(name=name, email=email)
            new_tenant.save()
            messages.success(request, "Grupo escolar criado com sucesso!")
            return redirect('tenant')

        elif "update" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            email = request.POST.get("email")

            # Verifica se o e-mail já existe
            existing_tenant = Tenant.objects.exclude(id=id).filter(email=email)
            if existing_tenant.exists():
                messages.warning(request, "E-mail já cadastrado por outro Grupo Escolar.")
                return redirect('tenant')

        # Continuação do seu código...
            tenant = get_object_or_404(Tenant, id=id)
            tenant.name = name
            tenant.email = email
            tenant.save()
            messages.success(request, "Grupo escolar editado com sucesso!")
            return redirect('tenant')


        elif "delete" in request.POST:
            id = request.POST.get("id")
            tenant = Tenant.objects.get(id=id)
            tenant.delete()
            messages.success(request, "Grupo escolar excluído com sucesso!")
            return redirect('tenant')

        elif "search" in request.POST:
            search_query = request.POST.get("query")
            tenants = Tenant.objects.filter(Q(name__icontains=search_query) | Q(email__icontains=search_query))

        context = {"tenants": tenants, "search_query": search_query}
        return render(request, self.template_name, context=context)