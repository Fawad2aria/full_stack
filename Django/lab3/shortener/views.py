from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
from django.views import View 

from lab3.forms import SubmitUrlform
from .models import Urlshort

baseurl = "localhost:8000"

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlform()
        shortened_url = Urlshort.objects.all()

        context = {
            "title": "URL Shortener",
            "form": the_form, 
            "retrieve_url": shortened_url,
            "baseurl": baseurl,

        }
        return render(request, "shortener/index.html", context)

    def post(self, request, *args, **kwrgs):
        form = SubmitUrlform(request.POST)
        context = {
            "title": "URL Shortener",
            "form": form
        }
        template = "shortener/index.html"
        
        obj, created = Urlshort.objects.get_or_create(url=request.POST['url'])
        context = {
            "object": obj,
            "baseurl": baseurl,
            "created": created,
        }
        if created: 
            template = "shortener/success.html"

        else:
            template = "shortener/already-exists.html"

        return render(request, template, context)


def redirect_url(request, shortcode):
    
    obj = get_object_or_404(Urlshort, shortcode=shortcode)
    obj.count += 1
    obj.save()    
    return HttpResponseRedirect(obj.url)

    
