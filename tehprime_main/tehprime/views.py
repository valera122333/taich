from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import About, Cart, Contact, Postavki, Project, Vendor
# Create your views here.
from django.contrib import messages
from .forms import *

from django.contrib.auth.decorators import login_required


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
    return redirect('favourites.html')


def about(request):
    about = About.objects.all()
    return render(request, 'ТехПрайм_О_компаний.html', {'about': about})


def proect(request):
    projects = Project.objects.all()
    return render(request, "ТехПрайм_Проекты.html", {"projects": projects})


def project_detail(request, project_id):
    projects = get_object_or_404(Project, pk=project_id)
    return render(request, 'project_detail.html', {'projects': projects})


def postavki(request):
    postavki = Postavki.objects.all()
    return render(request, 'ТехПрайм_Поставки.html', {'postavki': postavki})


def postavki_detail(request, post_id):
    post = get_object_or_404(Postavki, pk=post_id)
    return render(request, 'postavki_detail.html', {'post': post})


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
