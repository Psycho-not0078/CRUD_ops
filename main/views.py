from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *
from airline_management_system.settings import *
from django.views import View
from django.views.decorators.csrf import *
from django.utils.decorators import method_decorator
from django.http.multipartparser import MultiPartParser
from datetime import datetime
import uuid
import json  
from django.core.serializers.json import DjangoJSONEncoder

url = "https://www.geeksforgeeks.org/fibonacci-sum-subset-elements/"

def create(request):#C
    context ={}
    
    # print(MEDIA_ROOT,MEDIA_URL)
    if request.method=="POST":
        form = TestForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,"success.html")
        else:
            print(form.errors)
            return HttpResponse(form.errors['Profile_image'])
        
    elif request.method=="GET":
        form=TestForm()
        context['form']= form
        return render(request, "create.html", context)


# def functs(request):
#     if request.method=="PUT":
#         print("!")
#     elif request.method=="DELETE":
#         print("lol")
#     return 0

@method_decorator(csrf_exempt, name='dispatch')
class init_functs(View):
    def post(self,request):#C
        form = TestForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = TestForm()
            return HttpResponse("success")
        else:
            return HttpResponse("fail")
    def get(self,request):#R
        request_form=request.GET.dict()
        if len(request.GET.dict())!=0:
            Id=request_form['id']
            queryset=TestTable.objects.filter(id=Id)
            print(type(queryset))
            print(queryset.values())
            queryset_ret=list(queryset.values())
            print(queryset_ret)
            queryset_ret[0]["file_url"]="127.0.0.1:8000/media/"+queryset_ret[0]["profile_image"]
            return JsonResponse(queryset_ret[0])
        else:
            context ={}
            form=TestForm()
            context['form']= form
            return render(request, "create.html", context)
    def put(self,request):#U
            # print(request.method,request.body)
            qwerty=MultiPartParser(request.META, request, request.upload_handlers).parse()
            # print(type(qwerty),qwerty)
            form=qwerty[0].dict()
            # print(form)
            identifier=form["Identifier"]
            to_be_changed=form["To be changed"]
            # print(identifier,to_be_changed)
            try:
                if identifier=="Name":
                    if to_be_changed=="Name":
                        updater=TestTable.objects.filter(name=form[identifier]).update(name=form[to_be_changed])
                    elif to_be_changed=="Position":
                        updater=TestTable.objects.filter(name=form[identifier]).update(position=form[to_be_changed])
                    elif to_be_changed=="DOB":
                        updater=TestTable.objects.filter(name=form[identifier]).update(dob=form[to_be_changed])
                    elif to_be_changed=="DOJ":
                        updater=TestTable.objects.filter(name=form[identifier]).update(doj=form[to_be_changed])
                    elif to_be_changed=="Salary":
                        updater=TestTable.objects.filter(name=form[identifier]).update(salary=form[to_be_changed])
                elif identifier=="Position":
                    if to_be_changed=="Name":
                        updater=TestTable.objects.filter(position=form[identifier]).update(name=form[to_be_changed])
                    elif to_be_changed=="Position":
                        updater=TestTable.objects.filter(position=form[identifier]).update(Position=form[to_be_changed])
                    elif to_be_changed=="DOB":
                        updater=TestTable.objects.filter(position=form[identifier]).update(dob=form[to_be_changed])
                    elif to_be_changed=="DOJ":
                        updater=TestTable.objects.filter(position=form[identifier]).update(doj=form[to_be_changed])
                    elif to_be_changed=="Salary":
                        updater=TestTable.objects.filter(position=form[identifier]).update(salary=form[to_be_changed])
                elif identifier=="DOB":
                    if to_be_changed=="Name":
                        updater=TestTable.objects.filter(dob=form[identifier]).update(name=form[to_be_changed])
                    elif to_be_changed=="Position":
                        updater=TestTable.objects.filter(dob=form[identifier]).update(Position=form[to_be_changed])
                    elif to_be_changed=="DOB":
                        updater=TestTable.objects.filter(dob=form[identifier]).update(dob=form[to_be_changed])
                    elif to_be_changed=="DOJ":
                        updater=TestTable.objects.filter(dob=form[identifier]).update(doj=form[to_be_changed])
                    elif to_be_changed=="Salary":
                        updater=TestTable.objects.filter(dob=form[identifier]).update(salary=form[to_be_changed])
                elif identifier=="DOJ":
                    if to_be_changed=="Name":
                        updater=TestTable.objects.filter(doj=form[identifier]).update(name=form[to_be_changed])
                    elif to_be_changed=="Position":
                        updater=TestTable.objects.filter(doj=form[identifier]).update(Position=form[to_be_changed])
                    elif to_be_changed=="DOB":
                        updater=TestTable.objects.filter(doj=form[identifier]).update(dob=form[to_be_changed])
                    elif to_be_changed=="DOJ":
                        updater=TestTable.objects.filter(doj=form[identifier]).update(doj=form[to_be_changed])
                    elif to_be_changed=="Salary":
                        updater=TestTable.objects.filter(doj=form[identifier]).update(salary=form[to_be_changed])
                elif identifier=="Salary":
                    if to_be_changed=="Name":
                        updater=TestTable.objects.filter(salary=form[identifier]).update(name=form[to_be_changed])
                    elif to_be_changed=="Position":
                        updater=TestTable.objects.filter(salary=form[identifier]).update(Position=form[to_be_changed])
                    elif to_be_changed=="DOB":
                        updater=TestTable.objects.filter(salary=form[identifier]).update(dob=form[to_be_changed])
                    elif to_be_changed=="DOJ":
                        updater=TestTable.objects.filter(salary=form[identifier]).update(doj=form[to_be_changed])
                    elif to_be_changed=="Salary":
                        updater=TestTable.objects.filter(salary=form[identifier]).update(salary=form[to_be_changed])
            except Exception as e:
                print(e)
                return HttpResponse("fail")
            return HttpResponse("success")            
    def delete(self,request):#D
        qwerty=MultiPartParser(request.META, request, request.upload_handlers).parse()
        form=qwerty[0].dict()
        identifier=form["Identifier"]
        file_names=TestTable.objects.filter(name=form[identifier]).values_list('profile_image').values()
        print(file_names)
        try:
            if identifier=="Name":    
                updater=TestTable.objects.filter(name=form[identifier]).delete()
            elif identifier=="Position":
                updater=TestTable.objects.filter(position=form[identifier]).delete()
            elif identifier=="DOB":
                updater=TestTable.objects.filter(dob=form[identifier]).delete()
            elif identifier=="DOJ":
                updater=TestTable.objects.filter(doj=form[identifier]).delete()
            elif identifier=="Salary":
                updater=TestTable.objects.filter(salary=form[identifier]).delete()
            for i in file_names:
                file=os.path.join(MEDIA_ROOT,i)
                os.remove(i)
        except:
            return HttpResponse("fail")
        return HttpResponse("success")