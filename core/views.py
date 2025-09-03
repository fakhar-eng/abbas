from django.shortcuts import render, get_object_or_404, redirect
from .models import Core
from .forms import CoreForm

def index(request):
    return render(request, 'core/index.html')

def core_list(request):
   core = Core.objects.all().order_by('-created_at')  # کلاس کا نام Capitalized ہونا چاہیے
   return render(request, 'core/core_list.html', {'core': core})

def core_create(request):  # کالون غائب تھا
   if request.method == 'POST':
      form = CoreForm(request.POST, request.FILES)  # کلاس کا نام Capitalized ہونا چاہیے
      if form.is_valid():
            core = form.save(commit=False)
            core.user = request.user
            core.save()
            return redirect('core_list')
   else:
      form = CoreForm()  # سپیلنگ کی غلطی: 'from' کی بجائے 'form' اور کلاس کا نام Capitalized
   
   return render(request, 'core/core_form.html', {'form': form})  # یہ لائن انڈینٹیشن درست کی

def core_edit(request, core_id):  # متغیر نام میں سپیس غلط تھی
    core = get_object_or_404(Core, pk=core_id, user=request.user)  # لائن کو درست کیا

    if request.method == 'POST':
        form = CoreForm(request.POST, request.FILES, instance=core)
        if form.is_valid():
            core = form.save(commit=False)
            core.user = request.user
            core.save()  # 'core_list' کی بجائے صرف save() کال کریں
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
