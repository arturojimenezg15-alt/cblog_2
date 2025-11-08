from django.urls import path 
from .views import (
                    PublicationListView, 
                    PublicationCreteView,
                    PublicationDetailView,
                  )                   

urlpatterns = [
    path('', PublicationListView.as_view(), name='publications-list'),
    path('publication/new/', PublicationCreteView.as_view(), name='publication-create'),
    path('publication/<int:pk>/', PublicationDetailView.as_view(), name='publication-detail'),
]
