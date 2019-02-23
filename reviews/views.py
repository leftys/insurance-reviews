from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.core.paginator import Paginator

from .models import Review, Product, Category



def index(request):
    latest_reviews = Review.objects.order_by('-creation_time')
    paginator = Paginator(latest_reviews, 10)
    page = request.GET.get('page')
    context = {
            'reviews': paginator.get_page(page),
    }
    return render(request, 'index.html', context)


def category_detail(request, category_id):
    category = Category.objects.get(id = category_id)
    latest_reviews = Review.objects.filter(product__category = category).order_by('-creation_time')
    paginator = Paginator(latest_reviews, 10)
    page = request.GET.get('page')
    context = {
            'category': category,
            'reviews': paginator.get_page(page),
    }
    return render(request, 'category_detail.html', context)


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
    except Product.DoesNotExist:
        selected_product = Product(name = request.POST['insurance'], creation_time = timezone.now())
        selected_product.save()
    review = Review(
        author = request.POST['name'],
        author_ip = request.META.get('REMOTE_ADDR'),
        product = selected_product,
        text = request.POST['message'],
        rating = request.POST['rating'],
        creation_time = timezone.now(),
    )
    review.save()
    return HttpResponseRedirect(reverse('index'))

