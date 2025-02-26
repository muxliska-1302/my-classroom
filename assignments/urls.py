from django.urls import path
from . import views


app_name = 'assignments'

urlpatterns = [
    path('assignments-list/', views.AssignmentListView.as_view(), name='list'),
    path('assignment-create/', views.AssignmentCreateView.as_view(), name='create'),
    path('assignments-detail/<int:pk>/', views.AssignmentDetailView.as_view(), name='detail'),
    path('assignments-update/<int:pk>/', views.AssignmentUpdateView.as_view(), name='update'),
    path('assignments-delete/<int:pk>/', views.AssignmentDeleteView.as_view(), name='delete'),
]