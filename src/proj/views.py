from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from .filters import ProjectFilter
from .models import Project
# Create your views here.
from django.core.paginator import Paginator
from .form import JoinForm , ProjectForm


def project_list(request):

    project_list = Project.objects.all()
    projects_count = project_list.count

    ## filters
    myfilter = ProjectFilter(request.GET,queryset=project_list)
    project_list = myfilter.qs

    paginator = Paginator(project_list , 3)  # Show 5 projects per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'projects': page_obj ,'count': projects_count , 'myfilter' : myfilter }
    return render(request,'project/project_list.html',context)


def project_detail(request,slug):
    project_detail =  Project.objects.get(slug=slug)

    if request.method == 'POST':
        form = JoinForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.project = project_detail
            myform.save()
            print('DOne')

    else:
        form = JoinForm()

    context = {'project': project_detail, 'form1': form}
    return render(request, 'project/project_detail.html', context)

@login_required
def add_project(request):
    if request.method=='POST':
        form = ProjectForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('projects:project_list'))

    else:
        form = ProjectForm()

    return render(request,'project/add_project.html',{'form':form})
