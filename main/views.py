from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *
from airline_management_system.settings import *
from django.views import View,generic
from django.views.decorators.csrf import *
from django.utils.decorators import method_decorator
from django.http.multipartparser import MultiPartParser
from datetime import datetime
import uuid
import json  
from django.core.serializers.json import DjangoJSONEncoder


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
            return HttpResponse("success")
        else:
            print(form.errors)
            return HttpResponse("fail")
    def get(self,request):#R
        request_form=request.GET.dict()
        if len(request.GET.dict())!=0:
            Id=request_form['id']
            queryset=TestTable.objects.get(id=Id)
            lists=get_object_or_404(TestTable,id=Id)
            return render(request, 'detail_list.html', context={'dets': lists})
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
            #print(form)
            identifier=form["Identifier"]
            to_be_changed=form["To be changed"]
            #print(form[to_be_changed],form[identifier])
            # print(identifier,to_be_changed)
            try:
                if identifier=="Name":
                    if to_be_changed=="Name":
                        updater=TestTable.objects.filter(name=form[identifier]).update(name=form[to_be_changed])
                        
                    elif to_be_changed=="Position":
                        updater=TestTable.objects.filter(name__exact=form[identifier]).update(position=form[to_be_changed])
                                                                      
                    elif to_be_changed=="Salary":
                        updater=TestTable.objects.filter(name__exact=form[identifier]).update(salary=form[to_be_changed])
                        
                elif identifier=="Position":
                    if to_be_changed=="Name":
                        updater=TestTable.objects.filter(position__exact=form[identifier]).update(name=form[to_be_changed])
                        
                    elif to_be_changed=="Position":
                        updater=TestTable.objects.filter(position__exact=form[identifier]).update(Position=form[to_be_changed])
                                                                     
                    elif to_be_changed=="Salary":
                        updater=TestTable.objects.filter(position__exact=form[identifier]).update(salary=form[to_be_changed])
                        
                elif identifier=="Date of birth":
                    if to_be_changed=="Name":
                        updater=TestTable.objects.filter(dob=form[identifier]).update(name=form[to_be_changed])
                        
                    elif to_be_changed=="Position":
                        updater=TestTable.objects.filter(dob=form[identifier]).update(Position=form[to_be_changed])
                                                                      
                    elif to_be_changed=="Salary":
                        updater=TestTable.objects.filter(dob=form[identifier]).update(salary=form[to_be_changed])
                        
                elif identifier=="DOJ":
                    if to_be_changed=="Name":
                        updater=TestTable.objects.filter(doj=form[identifier]).update(name=form[to_be_changed])
                        
                    elif to_be_changed=="Position":
                        updater=TestTable.objects.filter(doj=form[identifier]).update(Position=form[to_be_changed])
                                                                     
                    elif to_be_changed=="Salary":
                        updater=TestTable.objects.filter(doj=form[identifier]).update(salary=form[to_be_changed])
                        
                elif identifier=="Salary":
                    if to_be_changed=="Name":
                        updater=TestTable.objects.filter(salary=form[identifier]).update(name=form[to_be_changed])
                        
                    elif to_be_changed=="Position":
                        updater=TestTable.objects.filter(salary=form[identifier]).update(Position=form[to_be_changed])
                                              
                    elif to_be_changed=="Salary":
                        updater=TestTable.objects.filter(salary=form[identifier]).update(salary=form[to_be_changed])
                        
            except Exception as e:
                #print(e)
                return HttpResponse("fail")
            return HttpResponse("success")            
    def delete(self,request):#D
        qwerty=MultiPartParser(request.META, request, request.upload_handlers).parse()
        form=qwerty[0].dict()
        identifier=form["Identifier"]
        file_names=TestTable.objects.filter(name__exact=form[identifier]).values('profile_image')
        print("names of files: ",file_names)
        print("Length = ",len(file_names))
        try:
            # print("In try")
            for i in file_names:
                print("here",i)
                file=os.path.join(MEDIA_ROOT,i['profile_image'])
                print("names: ",file)
                os.remove(file)
            # print("end of loop")
            if identifier=="Name":    
                updater=TestTable.objects.filter(name__exact=form[identifier]).delete()
            elif identifier=="Position":
                updater=TestTable.objects.filter(position__exact=form[identifier]).delete()
            elif identifier=="Date of birth":
                updater=TestTable.objects.filter(dob=form[identifier]).delete()
            elif identifier=="DOJ":
                updater=TestTable.objects.filter(doj=form[identifier]).delete()
            elif identifier=="Salary":
                updater=TestTable.objects.filter(salary=form[identifier]).delete()
            elif identifier=="Gender":
                updater=TestTable.objects.filter(gender=form[identifier]).delete()
            elif identifier=="Age":
                updater=TestTable.objects.filter(age=form[identifier]).delete()
            elif identifier=="Permanent Employee":
                updater=TestTable.objects.filter(permanent_employee=form[identifier]).delete()
            elif identifier=="Bio":
                updater=TestTable.objects.filter(bio=form[identifier]).delete()
            # print("End of try")
        except Exception as e:
            print (e)
            return HttpResponse("fail"+str(e))
        return HttpResponse("success")

class editer(View):
    def post(self,request,id):
        mod=TestTable.objects.get(id=id)
        form=TestForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(instance=mod)
        else:
            print(form.errors)
        return HttpResponse("success")

    def get(self,request,id):
        mod=TestTable.objects.filter(id=id).values()
        queryset=TestTable.objects.get(id=id)
        lists=get_object_or_404(TestTable,id=id)
        form=TestForm1(initial=mod[0])
        return render(request,"update.html",{"form":form,"mod":lists})
    
def edit(request):
    if request.method=="POST":
        id=request.POST.get("id")
        return redirect("edit/"+id)
    else:
        return render(request,"edit.html")