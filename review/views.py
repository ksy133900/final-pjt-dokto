from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.


def pro_index(request):
    return render(request, "review/pro_index.html")

def index(request):
    # review = Review.objects.order_by("-pk")
    return render(request, "review/index.html")
    
def genre(request):
    test = [0,1,2,3,4,5,6,7,8,9]
    context = {
        "test": test
    }
    return render(request, "review/genre.html", context)

def create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        photo_form = PhotoForm(request.POST, request.FILES)
        images = request.FILES.getlist("image")
        # tags = request.POST.get("tags", "").split(",")

        # if request.POST.get("tags", "") != "":
        #     tags = request.POST.get("tags", "").split(",")
        # else:
        #     tags = None

        if review_form.is_valid() and photo_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user

            if len(images):
                for image in images:
                    image_instance = Photo(review=review, image=image)
                    review.save()
                    image_instance.save()

            review.save()
            # if tags:
            #     for tag in tags:
            #         tag = tag.strip()
            #         article.tags.add(tag)
            #         article.save()

            return redirect("review:index")
    else:
        review_form = ReviewForm()
        photo_form = PhotoForm()
    context = {
        "review_form": review_form,
        "photo_form": photo_form,
    }
    return render(request, "review/create.html", context)


# def detail(request):

#     return render(request, "review/detail.html")
