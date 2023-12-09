from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .models import Court

# Create your views here.
def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))

def court(request):
    court = Court.objects.all().values()
    template = loader.get_template('court.html')
    context = {
    'court': court,
    }
    return HttpResponse(template.render(context, request))

def court_detail(request, id):
    court = Court.objects.get(id=id)
    template = loader.get_template('court_detail.html')
    context = {
    'court': court,
    }
    return HttpResponse(template.render(context, request))