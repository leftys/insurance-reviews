from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from .models import Review, Product



def index(request):
    latest_reviews = Review.objects.order_by('-creation_time')[:5]
    context = {
            'reviews': latest_reviews,
    }
    return render(request, 'index.html', context)


def new_review(request):
    insurances = Product.objects.all()
    context = {
        'insurances': insurances,
    }
    return render(request, 'new_review.html', context)


def about(request):
    return render(request, 'about.html')


def submit_review(request):
    try:
        selected_product = Product.objects.get(name = request.POST['insurance'])
    except KeyError:
        selected_product = Product(name = request.POST['insurance'])
        selected_product.save()
    review = Review(
        author = request.POST['name'],
        author_ip = request.META.get('REMOTE_ADDR'),
        product = selected_product,
        text = request.POST['message'],
        rating = 0, # TODO
        creation_time = timezone.now(),
    )
    review.save()
    return HttpResponseRedirect(reverse('index'))

