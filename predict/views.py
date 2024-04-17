from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ReviewForm
from .logic.logic import get_reviews, get_reviews_filter, get_reviews_group_filter
from .predictor import predict


def review_list(request):
    reviews = get_reviews()
    context = {
        'review_list': reviews,
        'filter': False,
        'quantity': len(reviews)
    }
    return render(request, 'reviews.html', context)


def review_list_all(request):
    reviews = get_reviews()
    context = {
        'review_list': reviews,
        'filter': True,
        'quantity': len(reviews)
    }
    return render(request, 'reviews.html', context)


def review_list_bad(request):
    reviews = get_reviews_group_filter(1, 2)
    context = {
        'review_list': reviews,
        'filter': True,
        'quantity': len(reviews)

    }
    return render(request, 'reviews.html', context)


def review_list_good(request):
    reviews = get_reviews_group_filter(4, 5)
    context = {
        'review_list': reviews,
        'filter': True,
        'quantity': len(reviews)

    }
    return render(request, 'reviews.html', context)


def review_list_1(request):
    reviews = get_reviews_filter(1)
    context = {
        'review_list': reviews,
        'filter': True,
        'quantity': len(reviews)

    }
    return render(request, 'reviews.html', context)


def review_list_2(request):
    reviews = get_reviews_filter(2)
    context = {
        'review_list': reviews,
        'filter': True,
        'quantity': len(reviews)
    }
    return render(request, 'reviews.html', context)


def review_list_3(request):
    reviews = get_reviews_filter(3)
    context = {
        'review_list': reviews,
        'filter': True,
        'quantity': len(reviews)
    }
    return render(request, 'reviews.html', context)


def review_list_4(request):
    reviews = get_reviews_filter(4)
    context = {
        'review_list': reviews,
        'filter': True,
        'quantity': len(reviews)
    }
    return render(request, 'reviews.html', context)


def review_list_5(request):
    reviews = get_reviews_filter(5)
    context = {
        'review_list': reviews,
        'filter': True,
        'quantity': len(reviews)
    }
    return render(request, 'reviews.html', context)


def review_group(request):
    reviews = get_reviews()
    context = {
        'review_list': reviews
    }
    return render(request, 'review_group.html', context)


def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            text = review.review
            review.classification = predict(text)
            review.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Successfully created review')
            return HttpResponseRedirect(reverse('reviewCreate'))
        else:
            print(form.errors)
    else:
        form = ReviewForm()

    context = {
        'form': form,
    }
    return render(request, 'review_create.html', context)
