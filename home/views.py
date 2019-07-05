from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.
from home.forms import StudentSearchForm
from home.models import Student
from home.forms import StudentEditModelForm
from home.forms import StudentCreateForm

def home_view(request):
    if request.method=='POST':
        search=StudentSearchForm(request.POST)
        if search.is_valid():
            value=search.cleaned_data.get('q')
            result=Student.objects.filter(student_name__contains=value)
            return  render(request,'home.html',{'result':result,'form':StudentSearchForm()})
    else:
        form=StudentSearchForm()
        return render(request,'home.html',{'form':form})

    #form1=StudentSearchForm()
    #form2=StudentDetailForm()
    #context={'form':form1,'details':form2}
    return render(request,'home.html',context)

def deletestudent(request,id):
    result=Student.objects.get(id=id)
    result.delete()
    messages.success(request,'Deleted Successfully')
    return redirect('/')

def editstudent(request,id):
    student=Student.objects.get(id=id)
    if request.method=='POST':
        modelform=StudentEditModelForm(request.POST,instance=student)
        if modelform.is_valid():
            modelform.save()
            messages.success(request,'Update Successfully')
            return redirect('/')
    else:
        modelform=StudentEditModelForm(instance=student)
        return render(request,'edit.html',{'form':modelform,'value':'Edit'})

def createstudent(request):
    if request.method=='POST':
        form=StudentCreateForm(request.POST)
        if form.is_valid():
            student=Student.objects.create(student_name=form.cleaned_data.get('student_name'),department=form.cleaned_data.get('department'))
            student.save()
            messages.success(request,'Created Successfully')
            return redirect('/')
    else:
        form=StudentCreateForm()
        return render(request,'create.html',{'form':form,'value':'Create'})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
