from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .models import About, Cart, Contact, Project, Vendor
# Create your views here.
from django.contrib import messages
from .forms import *

from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect
from django.views.generic import (DetailView,
                                  ListView,
                                  FormView,)


from .models import Standard, Subject, Lesson, Contact
from django.urls import reverse_lazy

from django.http import HttpResponseRedirect
# фишки

from django.contrib.auth.decorators import login_required
from django.contrib import messages


class StandardListView(ListView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'standard_list_view.html'


class SubjectListView(DetailView):
    context_object_name = 'standards'

    model = Standard
    template_name = 'subject_list_view.html'


class LessonListView(DetailView):
    context_object_name = 'subjects'
    model = Subject
    template_name = 'lesson_list_view.html'


class LessonDetailView(DetailView, FormView):
    context_object_name = 'lessons'
    model = Lesson
    template_name = 'lesson_detail_view.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(request=self.request)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'form' in request.POST:
            form_class = self.get_form_class()
            form_name = 'form'

        form = self.get_form(form_class)

        if form_name == 'form' and form.is_valid():
            print("comment form is returned")
            return self.form_valid(form)

    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.Standard
        subject = self.object.subject
        return reverse_lazy('lesson_detail', kwargs={'standard': standard.slug,
                                                     'subject': subject.slug,
                                                     'slug': self.object.slug})

    def form_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.lesson_name = self.object.comments.name
        fm.lesson_name_id = self.object.id
        fm.save()
        return HttpResponseRedirect(self.get_success_url())


def home(request):
    cart = Cart.objects.all()
    return render(request, 'home.html', {'cart': cart})


def vendor(request):
    vendors = Vendor.objects.all()
    return render(request, 'ТехПрайм_Вендоры.html', {"vendors": vendors})


@login_required
def contact(request):
    if request.method == 'POST':
        contact = Contact(contact_info=request.user)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        contact_info = request.user
        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.subject = subject

        contact.save()
        messages.success(
            request, f"Добавилась новая заявка! от пользователя  {contact_info}")

        contact.save()
        return redirect('/', f"Добавилась новая заявка! ")
    return render(request, 'ТехПрайм_Контакты.html')


def delete_contact(request, pk=None):
    Contact.objects.get(id=pk).delete()
    messages.success(
        request, f'Заявка успешно удалена пользователем!{request.user.username} !')
    return redirect('home.html')


def about(request):
    about = About.objects.all()
    return render(request, 'ТехПрайм_О_компаний.html', {'about': about})


def proect(request):
    projects = Project.objects.all()
    return render(request, "ТехПрайм_Проекты.html", {"projects": projects})


def project_detail(request, project_id):
    projects = get_object_or_404(Project, pk=project_id)
    return render(request, 'project_detail.html', {'projects': projects})


def card_detail(request, card_id):
    card = get_object_or_404(Cart, pk=card_id)
    return render(request, 'card_detail.html', {'card': card})


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')

            messages.success(
                request, f"Аккаунт создан для пользователя {username}!")
            return redirect('login')
    else:

        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def favourite_list(request):
    new = Project.objects.all().filter(favourites=request.user)
    zayzvka = Contact.objects.all().filter(contact_info=request.user)

    return render(request,
                  'favourites.html',
                  {'new': new, 'zayzvka': zayzvka})


def favourite_add(request, id):
    books = get_object_or_404(Project, id=id)
    if books.favourites.filter(id=request.user.id).exists():
        books.favourites.remove(request.user)
    else:
        books.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
