from django.urls import path
from . import views


app_name = 'courses'

urlpatterns = [
    path('courses-list/', views.CourseListView.as_view(), name='list'),
    path('course-create/', views.CourseCreateView.as_view(), name='create'),
    path('course-details/<int:pk>/', views.CourseDetailView.as_view(), name='detail'),
    path('course-update/<int:pk>/', views.UpdateCourseView.as_view(), name='update'),
    path('course-delete/<int:pk>/', views.CourseDeleteView.as_view(), name='delete'),
]