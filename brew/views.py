from django.shortcuts import render
from brew.models import BrewInfo
from django.http import HttpResponse

# Create your views here.
# Create your views here.
def home(request):
    all_brews = BrewInfo.objects.all().values('id', 'bean_text', 'pub_date', )
    context = {
        "all_brews": all_brews,
    }
    return render(request, "home.html", context)


def health(request):
    return HttpResponse("I am health.")


def submit(request):
    return HttpResponse("I am submit.")


def queryByBeanName(request, query_name):
    brew_detail = BrewInfo.objects.get(bean_text=query_name)
    context = {
        "brew_detail": brew_detail,
    }
    return render(request, "detail.html", context)


def new_brew(request):

    brew = BrewInfo(bean_text=request.POST['bean_name'])
    brew.save()

    all_brews = BrewInfo.objects.all().values('id', 'bean_text', 'pub_date', )
    context = {
        "all_brews": all_brews,
    }
    return render(request, "home.html", context)
