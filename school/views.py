from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.db.models import Q
from .models import School
from tenant.models import Tenant
from django.db import IntegrityError



class SchoolView(View):
    template_name = 'school/index.html'

    def get(self, request, *args, **kwargs):
        schools = School.objects.all().select_related('tenant')
        tenants = Tenant.objects.all()
        search_query = ""
        context = {"tenants": tenants, "schools": schools, "search_query": search_query}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        schools = School.objects.all()
        search_query = ""

        if "create" in request.POST:
            # Obtenha os dados da escola a ser criada
            name = request.POST.get("name")
            namesocial = request.POST.get("namesocial")
            cnpj = request.POST.get("cnpj")
            namefantasy = request.POST.get("namefantasy")
            description = request.POST.get("description")
            tenant_id = request.POST.get("tenant")
            
            try:
                # Tente criar uma nova instância de School
                new_school = School(
                    name=name,
                    namesocial=namesocial,
                    cnpj=cnpj,
                    namefantasy=namefantasy,
                    description=description,
                    tenant_id=tenant_id
                )

                # Salve a instância
                new_school.save()
                messages.success(request, "Escola criada com sucesso!")
                return redirect('school')

            except IntegrityError:
                # Captura a exceção de violação de unicidade e trata de acordo
                messages.error(request, "Já existe uma escola com esses dados.")
                return redirect('school')  # Ou redirecione para onde for necessário
        
        elif "update" in request.POST:
        # Obtenha os dados da escola a ser atualizada
            school_id = request.POST.get("id")  # Supondo que você tenha um campo oculto com o ID da escola
            name = request.POST.get("name")
            namesocial = request.POST.get("namesocial")
            cnpj = request.POST.get("cnpj")
            namefantasy = request.POST.get("namefantasy")
            description = request.POST.get("description")
            tenant_id = request.POST.get("school")

            try:
                # Tente obter a escola existente pelo ID
                existing_school = get_object_or_404(School, id=school_id)

                # Atualize os campos necessários
                existing_school.name = name
                existing_school.namesocial = namesocial
                existing_school.cnpj = cnpj
                existing_school.namefantasy = namefantasy
                existing_school.description = description
                existing_school.tenant_id = tenant_id

                print("ID:", existing_school.id)
                print("Name:", name)
                print("Tenant ID:", tenant_id)

                # Salve a instância atualizada
                existing_school.save()

                messages.success(request, "Escola atualizada com sucesso!")
                return redirect('school')

            except School.DoesNotExist:
                messages.error(request, "Escola não encontrada.")
                return redirect('school')  # Ou redirecione para onde for necessário
            
        elif "delete" in request.POST:
            school_id = request.POST.get("id")  # Supondo que você tenha um campo oculto com o ID da escola

            try:
                # Tente obter a escola existente pelo ID
                existing_school = get_object_or_404(School, id=school_id)

                # Exclua a instância
                existing_school.delete()

                messages.success(request, "Escola excluída com sucesso!")
                return redirect('school')

            except School.DoesNotExist:
                messages.error(request, "Escola não encontrada.")
                return redirect('school')  # Ou redirecione para onde for necessário
        
        elif "search" in request.POST:
            search_query = request.POST.get("query")
            schools = School.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))

        context = {"schools": schools, "search_query": search_query}
        return render(request, self.template_name, context=context)