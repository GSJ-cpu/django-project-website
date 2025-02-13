from django.shortcuts import render, redirect
from django.http import HttpResponse
from testforms.forms import HomeForm
from django.views.generic import TemplateView
from .models import Person
from .models import Exhibit
from django.db.models import Q

'''
1. Server requests infomation from the URLs given view
2. View returns appropriate information
AUTHOR: GHSJ
DATE: 17DEC24
'''

class Home(TemplateView):
    template_name = 'test_home.html'

    def get(self, request):
        form = HomeForm()
        people = Person.objects.all()
        args = {'form':form, 'people':people}
        return render(request, self.template_name, args)
    
    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            name = form.save(commit=False)
            name.save()

            text = form.cleaned_data['name'] # Ensures the input will not harm the server
            form = HomeForm() # Resets form
            return redirect('/testing')
        args = {'form':form, 'name':text}
        return render(request, self.template_name, args)


def trying(request):
    return HttpResponse('Among us')

def index(request):
    if 'q' in request.GET: # If a query is entered
        q = request.GET['q']
        #data = Data.objects.filter(first_name__icontains=q)
        multiple_q = Q(Q(title__icontains=q) | Q(location__icontains=q) | Q(date__icontains=q)) # Refers to title & location
        data = Exhibit.objects.filter(multiple_q) # Filter data according to title & location
    else:
        data = Exhibit.objects.all
    context = {
        'data': data
    }
    return render(request, 'search.html', context)

def about_page(request):
    return render(request, 'about.html')

def account_page(request):
    return render(request, 'account.html')

def memberevents_page(request):
    return render(request, 'memevents.html')
