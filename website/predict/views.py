from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
import json 
from . import Clean
from .forms import SymptomForm
from .store import getsymptoms

def home(request):
    context = {'b':'Helloworld'}
    return render(request,'main.html',context)
class AjaxHandler(View):
    def get(self, request):
        text = request.GET.get('values')
        is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
        
        if is_ajax:
            sympts = text.split(',')
            
            sympts = [int(e) for e in sympts[:-1]]
            mainList = getsymptoms()
            mainList.sort()
            
            symptoms = [mainList[i] for i in sympts]
            diseases = Clean.runApp(symptoms)
            dis = ', '.join(diseases)
            
            return JsonResponse({'ans':dis, 'dis1': diseases[0], 'dis2':diseases[1], 'dis3':diseases[2]}, status=200)
        
        return render(request, 'trail.html')