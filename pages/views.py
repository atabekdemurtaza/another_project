from django.views import generic 
from pages.models import Blog, Entry, Author

class EntryView(generic.ListView):

    template_name = 'pages/page_list.html'
    queryset = Entry.objects.all()
    context_object_name = 'pages' #objects

class EntryDetail(generic.DetailView):

    template_name = 'pages/page_detail.html'
    queryset = Entry.objects.all()
    
