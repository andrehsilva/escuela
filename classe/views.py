from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.db.models import Q
from .models import Classe, School





class ClasseView(View):
    template_name = 'classe/index.html'

    def get(self, request, *args, **kwargs):
        classes = Classe.objects.all()
        search_query = ""
        context = {"classes": classes, "search_query": search_query}
        return render(request, self.template_name, context=context)
    
