from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.

#This function will add new student and show all student list

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid(): #it will check form is valid
            fm.save()  #this will save data to database with this we cannot save the data to databse
            fm = StudentRegistration()  # blank from will show note : in real time redirect krna page py abhi ky liye ye use krna

    else:
        fm = StudentRegistration() #blank from will show
    stud = User.objects.all()
    return render(request, 'Authapp/addandshow.html',{'form': fm, 'stud': stud})


#This function will update and delete

def update_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    #for get method else part is there
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'Authapp/updatestudent.html', {'form': fm})




# this function will delete student list
def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')