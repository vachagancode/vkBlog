from django.shortcuts import render, redirect
from .forms import EntryCreationForm

from .models import Entry
# Create your views here.
def index(request):
    title = "Blog"
    context = {'title': title}
    return render (request, 'blog/index.html', context)

def view(request):
    title = 'Vachagan Karapetyan'
    entries = Entry.objects.order_by('-date_added')
    context = {
        'title': title,
        'entries': entries,
    }
    return render (request, 'blog/main.html', context)

def only_admin(request):
    return render(request, 'blog/only_admin.html')

def new_entry(request):
    if request.user.is_authenticated:
        title = "New Entry"
        if request.method != 'POST':
            form = EntryCreationForm()
        else:
            form = EntryCreationForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('blogs:index')
        
        context = {
            'title': title,
            'form': form,
        }
        return render(request, 'blog/new_entry.html', context)
    else:
        return redirect('blogs:only_admin')

def about_me(request):
    title = 'About Me'
    return render(request, 'blog/about.html')