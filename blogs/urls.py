from django.urls import path 
from .views import (
                    PublicationListView, 
                    PublicationCreteView,
                    PublicationDetailView,
                    PublicationUpdateView,
                    PublicationDeleteView,
                  )                   

urlpatterns = [
    path('', PublicationListView.as_view(), name='publications-list'),
    path('publication/new/', PublicationCreteView.as_view(), name='publication-create'),
    path('publication/<int:pk>/', PublicationDetailView.as_view(), name='publication-detail'),
    path('publication/<int:pk>/update/', PublicationUpdateView.as_view(), name='publication-update'),
    path('publication/<int:pk>/delete/', PublicationDeleteView.as_view(), name='publication-delete'), 
]
