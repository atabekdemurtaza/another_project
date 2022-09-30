from django.urls import path 
from pages.views import EntryView

urlpatterns = [
    path('', EntryView.as_view())
]