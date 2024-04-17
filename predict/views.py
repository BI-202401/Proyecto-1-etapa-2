from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ReviewForm
from .logic.logic import get_reviews, create_review


def review_list(request):
    reviews = get_reviews()
    context = {
        'review_list': reviews
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
            # TODO añadir predicción del modelo
            print(review.review)
            review.classification = 5
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
