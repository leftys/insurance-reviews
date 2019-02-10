from django.shortcuts import render
from django.http import HttpResponse

from .models import Review



def index(request):
    latest_reviews = Review.objects.order_by('-creation_time')[:5]
    context = {
            'reviews': latest_reviews
    }
    return render(request, 'index.html', context)
    # return HttpResponse("Hello world!")
