from django.shortcuts import render, redirect,get_object_or_404  # Import render and redirect functions
from django.http import HttpResponse  # Import HttpResponse if used
from .models import Resource  # Import the Resource model
from .forms import ResourceForm  # Import the ResourceForm for creating/updating resources
from django.core.paginator import Paginator

def resource_list(request):
    status_filter = request.GET.get('status')  
    if status_filter:
        resources = Resource.objects.filter(status=status_filter)
    else:
        resources = Resource.objects.all()
    
    print("Resources being displayed:", resources)  

    paginator = Paginator(resources, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/resource_list.html', {'page_obj': page_obj, 'status_filter': status_filter})



# Delete resource view

def resource_delete(request, pk):
    resource = get_object_or_404(Resource, pk=pk)  
    if request.method == 'POST':
        resource.delete()  
        return redirect('resource_list')  
    return render(request, 'core/resource_confirm_delete.html', {'resource': resource})




# View to create a new resource

def resource_create(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resource_list')  
    else:
        form = ResourceForm()
    return render(request, 'core/resource_form.html', {'form': form})

# View to edit an existing resource
def resource_update(request, pk):
    resource = Resource.objects.get(pk=pk)  # Get the resource by primary key
    if request.method == 'POST':
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()  # Save changes to the resource
            return redirect('resource_list')  # Redirect to the resource list
    else:
        form = ResourceForm(instance=resource)
    return render(request, 'core/resource_form.html', {'form': form})
