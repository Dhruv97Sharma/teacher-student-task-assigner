from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Task, Assignment, Profile
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.

class Home(LoginRequiredMixin, View):
    template_name = "assignment_platform/home.html"
    login_url = 'login/'
    def __init__(self, **kwargs):
        pass

    def get(self, request):
        # Only fetch students
        users = get_user_model().objects.filter(is_staff=False)
        if request.user.is_superuser:
            tasks = Task.objects.filter(owner=request.user)
        else:
            tasks = Task.objects.filter(assignments__student=request.user)
        assignments = Assignment.objects.filter(student=request.user)
        return render(request,self.template_name,{'users': users, 'tasks': tasks, 'assignments': assignments})

class TaskView(View):
    def post(self, request):
        title = request.POST.get("name")
        description = request.POST.get("description")
        studentID = request.POST.getlist("students[]")
        # Create a new task
        user= request.user
        newTask = Task(title=title, description=description, owner= user)
        newTask.save()
        students = get_user_model().objects.filter(id__in=studentID)
        # For assigned students create assignments
        for student in students:
            assignment = Assignment(student=student)
            assignment.save()
            newTask.assignments.add(assignment)
            newTask.save()
        return JsonResponse({"message": "Successfully Saved!"})

class AssignmentView(View):
    def post(self, request):
        assignmentID = request.POST.get("assignmentID")
        status = request.POST.get("status")
        assignment = Assignment.objects.get(id=int(assignmentID))
        assignment.status = int(status)
        assignment.save()
        return JsonResponse({"message": "Status Successfully Updated!"})


class TaskListView(ListView):
    model = Task
    template_name = 'assignment_platform/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'tasks'
    ordering = ['-date_posted']
    paginate_by = 5


class UserTaskListView(ListView):
    model = Task
    template_name = 'assignment_platform/user_tasks.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Task.objects.filter(owner=user).order_by('-date_posted')


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.owner:
            return True
        return False


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = '/'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.owner:
            return True
        return False

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'assignment_platform/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'assignment_platform/profile.html', context)

@login_required
def assigntask(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.task)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.task)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Task has been assigned!')
            return redirect('home')

    else:
        u_form = UserUpdateForm(instance=request.task)
        p_form = ProfileUpdateForm(instance=request.task)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'assignment_platform/home.html', context)
