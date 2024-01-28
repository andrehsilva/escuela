from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.db import IntegrityError
from .models import Classe, School, Serie, Segment, Period


class ClasseView(View):
    template_name = 'classe/index.html'

    def get(self, request, *args, **kwargs):
        classes = Classe.objects.all()
        periods = Period.objects.all()
        schools = School.objects.all()
        series = Serie.objects.all()
        search_query = ""
        context = {"classes": classes, "periods": periods, "schools": schools, "series": series, "search_query": search_query}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        search_query = ""

        if "create" in request.POST:
            # Obtenha os dados da turma a ser criada
            name = request.POST.get("name")
            serie_id = request.POST.get("serie")
            period = request.POST.get("period")
            school_id = request.POST.get("school")

            print()

            try:

        
                # Crie uma nova instância de Classe com a instância de Serie
                new_classe = Classe(
                    name=name,
                    serie=serie_instance,
                    period=period,
                    school_id=school_id,
                )

                # Salve a instância
                new_classe.save()
                messages.success(request, "Turma criada com sucesso!")
                return redirect('classe')

            except Serie.DoesNotExist:
                messages.error(request, "A série especificada não foi encontrada.")
                return redirect('classe')  # Ou redirecione para onde for necessário
