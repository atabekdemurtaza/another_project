from django.urls import path 
from pages.views import EntryView, EntryDetail

urlpatterns = [
    path('', EntryView.as_view()),
    path('<int:pk>/', EntryDetail.as_view())
]