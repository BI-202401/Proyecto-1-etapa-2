from ..models import Reviews


def get_reviews():
    queryset = Reviews.objects.all()
    return (queryset)


def get_reviews_filter(num: int):
    queryset = Reviews.objects.filter(classification=num)
    return (queryset)


def get_reviews_group_filter(num1: int, num2: int):
    queryset = Reviews.objects.filter(classification__in=[num1, num2])
    return (queryset)


def create_review(form):
    review = form.save()
    review.save()
    return ()
