from django.shortcuts import render, get_object_or_404, redirect
from .models import Core
from .forms import CoreForm

def index(request):
    return render(request, 'core/index.html')

def core_list(request):
   core = Core.objects.all().order_by('-created_at')  
   return render(request, 'core/core_list.html', {'core': core})

def core_create(request):  
   if request.method == 'POST':
      form = CoreForm(request.POST, request.FILES)  
      if form.is_valid():
            core = form.save(commit=False)
            core.user = request.user
            core.save()
            return redirect('core_list')
   else:
      form = CoreForm()  
   
   return render(request, 'core/core_form.html', {'form': form})  

def core_edit(request, core_id):  
    core = get_object_or_404(Core, pk=core_id, user=request.user)  

    if request.method == 'POST':
        form = CoreForm(request.POST, request.FILES, instance=core)
        if form.is_valid():
            core = form.save(commit=False)
            core.user = request.user
            core.save()  
            return redirect('core_list')
    else:
        form = CoreForm(instance=core)
    return render(request, 'core/core_form.html', {'form': form})

def core_delete(request, core_id):
    core = get_object_or_404(Core, pk=core_id, user=request.user)
    if request.method == 'POST':
        core.delete()
        return redirect('core_list')
    return render(request, 'core/core_confirm_delete.html', {'core': core})
