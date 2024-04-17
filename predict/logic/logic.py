from ..models import Reviews


def get_reviews():
    queryset = Reviews.objects.all()
    return (queryset)


def create_review(form):
    review = form.save()
    review.save()
    return ()
