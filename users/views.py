from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import User
from courses.models import Course
from assignments.models import Assignment
from django.views import View
from .forms import UserForm


def home(request):
    users = User.objects.all()
    courses = Course.objects.all()
    assignments = Assignment.objects.all()
    ctx = {
        'users':users,
        'assignments':assignments,
        'courses':courses
    }
    return render(request, 'index.html', ctx)

class UsersListView(View):
    def get(self, request):
        users = User.objects.all()
        ctx = {'users':users}
        return render(request, 'users/users.html', ctx)

class UserCreateView(View):
    def get(self, request):
        form = UserForm()
        ctx = {'form':form}
        return render(request, 'users/users-form.html', ctx)

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('users:list'))
        ctx = {'form':form}
        return render(request, 'users/users-form.html', ctx)

class UserUpdateView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserForm(instance=user)
        ctx = {
            'user': user,
            'form':form
        }
        return render(request, 'users/users-form.html', ctx)
    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(reverse('users:list'))
        ctx = {
            'user': user,
            'form': form
        }
        return render(request, 'users/users-form.html', ctx)

class UserDeleteView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        ctx = {'user':user}
        return render(request, 'users/users-delete-confirm.html', ctx)
    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return redirect('users:list')