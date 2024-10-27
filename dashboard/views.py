from django.shortcuts import render
from dashboard_admin.models import ProductEntry, TokoEntry
from dashboard.models import JournalEntry
from dashboard.forms import journalEntryForm
from django.http import JsonResponse

import datetime
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render, redirect  
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.utils.html import strip_tags

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

def chunked(iterable, n):
    return [iterable[i:i + n] for i in range(0, len(iterable), n)]

def get_stores(request):
    stores = TokoEntry.objects.all().values('id', 'name')
    store_list = list(stores)
    return JsonResponse(store_list, safe=False)

def show_main(request):
    products = ProductEntry.objects.all()
    product_chunks = chunked(products, 3)

    return render(request, "main.html", {'product_chunks': product_chunks})

@login_required(login_url='/login')
def profile(request):
    return render(request, "profile.html")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('dashboard:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("dashboard:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    else:
       form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('dashboard:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
@require_POST
def create_journal_entry_ajax(request):
    title = strip_tags(request.POST.get("title"))
    store = strip_tags(request.POST.get("store"))
    description = strip_tags(request.POST.get("description"))
    time = strip_tags(request.POST.get("time"))
    ratings = strip_tags(request.POST.get("ratings"))
    user = request.user

    new_journal = JournalEntry(
        title=title, 
        store=store,
        description=description,
        time=time,
        ratings=ratings,
        user=user
    )
    new_journal.save()

    return HttpResponse(b"CREATED", status=201)

def edit_journal(request, id):
    journal_from_id = JournalEntry.objects.get(pk = id)
    journal_form = journalEntryForm(request.POST or None, instance=journal_from_id)

    if journal_form.is_valid() and request.method == "POST":
        journal_form.save()
        return HttpResponseRedirect(reverse('dashboard:profile'))

    context = {'form': journal_form}
    return render(request, "edit_journals.html", context)

def delete_journal(request, id):
    journal_from_id =  JournalEntry.objects.get(pk = id)
    journal_from_id.delete()

    return HttpResponseRedirect(reverse('dashboard:profile'))

def show_xml(request):
    data =  JournalEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data =  JournalEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data =  JournalEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data =  JournalEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


