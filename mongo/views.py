from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse ,redirect
# Create your views here.
# .表示当前包下的models
from .models import StudentModel
from django.views.generic import View
from django.core.paginator import Paginator
class Student(View):
    def get(self, request):
        StudentModel.objects.create(name='水2', age= 20)
        return HttpResponse('hello word')

def get_data(request):
    return HttpResponse('hello word u')

def index(request):
    article = StudentModel.objects
    context = {
        'ArtiInfo':article
    }
    return render(request, 'product-list.html', context) # 传递context参数

def delete(request):
    result = StudentModel.objects.filter(name='张三').first().delete()
    print(result)
    return HttpResponse('hello word')

def del_classes(request):
    nid = request.GET.get('nid')
    StudentModel.objects.filter(name=nid).first().delete()
    return redirect('/product')