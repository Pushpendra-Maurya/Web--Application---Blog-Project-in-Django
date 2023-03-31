from django.shortcuts import render,redirect
from .models import BlogModel
from .forms import BlogForm
from  django.contrib import messages
# Create your views here.


def home(request):

    blog = BlogModel.objects.all()

    context = {"blog":blog}
    return render(request, 'home.html', context)



def DashBoard(request):


    blog = BlogModel.objects.all()

    context = {"blog":blog}

    return render(request, 'dashboard.html' , context)



def addblog(request):
    forms = BlogForm()
    if request.method == 'POST':
        forms = BlogForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Blog SuccessFully Added ")
            return redirect('dashboard')
    context = {'forms':forms} 
    return render(request, 'addblog.html' , context)




def deleteblog(request , id):
    blog = BlogModel.objects.get(id =id ) #right side id itsa optional id u can change id = pk, name. anything

    blog.delete()
    messages.warning(request,'SuceessFully Deleted  Data On DataBase')
    return redirect('dashboard')


def updateblog(request, id):
    blog = BlogModel.objects.get(id =id ) #right side id itsa optional id u can change id = pk, name. anything
    if request.method =='POST':
        new_title = request.POST.get('updatetitle')
        new_desc = request.POST.get('updatedsc')
        blog.title = new_title
        blog.desc = new_desc
        # print(new_title)
        # print(new_desc)
        blog.save()
        messages.info(request, 'SuccessFully data Updated on DataBase ')
        return redirect('dashboard')
    context = {"blog":blog}
    return render(request, 'update.html' , context)

