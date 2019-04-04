from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Places
from .forms import CreateForm, LoginForm, UpdateForm, AddPOIForm, RemovePOIForm
import urllib, json

# https://stackoverflow.com/questions/150505/capturing-url-parameters-in-request-get
# https://docs.djangoproject.com/en/2.1/topics/templates/
# https://stackoverflow.com/questions/53083880/django-2-reverse-for-index-not-found-index-is-not-a-valid-view-function-o
# https://stackoverflow.com/questions/38987/how-to-merge-two-dictionaries-in-a-single-expression
# https://docs.djangoproject.com/en/dev/topics/db/queries/#backwards-related-objects
# https://developers.google.com/maps/documentation/geocoding/intro#geocoding
# https://www.powercms.in/blog/how-get-json-data-remote-url-python-script


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as require
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('wheredoyoulive:user_index', \
                args=(form.cleaned_data['username'],)))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()
    return render(request, 'wheredoyoulive/homepage.html', \
        {'form': form, \
        'make': reverse('wheredoyoulive:make'), \
        'user_index': reverse('wheredoyoulive:index')})


def make(request):
    form = CreateForm()
    return render(request, 'wheredoyoulive/FormPage.html', \
    {'form': form, \
    'page': })


def user_index(request, username):
    if (User.objects.filter(username=username)):
        u = User(username=username, latitude=0, longitude=0)
        u.save()
        return render(request, 'wheredoyoulive/userpage.html', \
            {'username': username, \
            'name': u.name, \
            'latitude': u.latitude, \
            'longitude': u.longitude, \
            'update': reverse('wheredoyoulive:update', args=(username,)), \
            'delete': reverse('wheredoyoulive:delete'), \
            'add_poi': reverse('wheredoyoulive:add_poi'), \
            'remove_poi': reverse('wheredoyoulive:rm_poi')})
    else:
        return HttpResponse('you\'re bad')


def update(request, username):
    return render(request, 'wheredoyoulive/FormPage.html', \
        {'form': form, \
        'page': reverse('wheredoyoulive:user_index')})


def delete(request, username):
    u = User.objects.get(username=username)
    u.delete()
    return HttpResponseRedirect(reverse('wheredoyoulive:index'))


def add_poi(request, username):
    u = User.objects.get(username=username)
    if request.method == 'POST':
        form = AddPOIForm(request.POST)
        if form.is_valid():
            address = form['Address'].replace(' ', '+')
            url = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=#AddKey' % address

            p = Place(user_id=u.id, title=form.cleaned_data['title'], )
            #return HttpResponseRedirect(reverse('wheredoyoulive:user_index', \
            #    args=(form.cleaned_data['username'],)))
    else:
        form = AddPOIForm()
    return render(request, 'wheredoyoulive/FormPage.html', \
        {'form': form, \
         'page': reverse('wheredoyoulive:add_poi')})
    #return HttpResponse('addpoi')
    #Can you add the page with the button to home here?


def rm_poi(request, username):
    return HttpResponse('rmpoi')
