from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from review.models import Review
from django.db.models import Q

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect("review:index")
    # 로그인 상태면 회원가입 ㄴㄴ
    if request.method == "POST":
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            Profile.objects.create(user=user)
            return render(request, "accounts/login.html")
    else:
        signup_form = CustomUserCreationForm()

    context = {
        "signup_form": signup_form,
    }
    if signup_form.errors:
        context['error']=[]
        for value in signup_form.errors.values():
            context['error'].append(value)
    return render(request, "accounts/signup.html", context)


def login(request):
    # 로그인 상태면 로그인 ㄴㄴ
    if request.user.is_authenticated:
        return redirect("review:index")
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect(request.GET.get("next") or "review:index")
    else:
        login_form = AuthenticationForm()

    context = {
        "login_form": login_form,
    }

    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("review:index")


def open_profile(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)


def open_profile(request, pk):
    profile = Profile.objects.order_by("-pk")
    review = Review.objects.order_by("-pk")
    user = get_object_or_404(get_user_model(), pk=pk)
    reviews = user.review_set.all()
    reviews_count = len(reviews)
    address_split = user.address.split(" ")
    address1 = address_split[0]
    address2 = address_split[1]
    context = {
        "profile": profile,
        "review": review,
        "user": user,
        "reviews": reviews,
        "reviews_count": reviews_count,
        "address1": address1,
        "address2": address2,
    }
    return render(request, "accounts/open_profile.html", context)


def update(request):
    return render(request, "accounts/update.html")


def profile(request, pk):
    profile = Profile.objects.order_by("-pk")
    review = Review.objects.order_by("-pk")
    user = get_object_or_404(get_user_model(), pk=pk)
    reviews = user.review_set.all()
    reviews_count = len(reviews)

    context = {
        "profile": profile,
        "review": review,
        "user": user,
        "reviews": reviews,
        "reviews_count": reviews_count,
    }

    return render(request, "accounts/profile.html", context)


# 회원 탈퇴
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        messages.warning(request, "회원 탈퇴 되었습니다.")
        auth_logout(request)

    return redirect("review:index")

# 검색 기능
def get_queryset(self):
    search_keyword = self.request.GET.get('q', '')
    search_type = self.request.GET.get('type', '')
    notice_list = Notice.objects.order_by('-id') 
    
    if search_keyword :
        if len(search_keyword) > 0 :
            if search_type == 'all':
                search_notice_list = notice_list.filter(Q (title__icontains=search_keyword) | Q (content__icontains=search_keyword) | Q (writer__user_id__icontains=search_keyword))
            elif search_type == 'title_content':
                search_notice_list = notice_list.filter(Q (title__icontains=search_keyword) | Q (content__icontains=search_keyword))
            elif search_type == 'title':
                search_notice_list = notice_list.filter(title__icontains=search_keyword)    
            elif search_type == 'content':
                search_notice_list = notice_list.filter(content__icontains=search_keyword)    
            elif search_type == 'writer':
                search_notice_list = notice_list.filter(writer__user_id__icontains=search_keyword)

            return search_notice_list
        else:
            messages.error(self.request, '검색어는 1글자 이상 입력해주세요.')
    return notice_list

# notice/views.py

def get_context_data(self, **kwargs):
    search_keyword = self.request.GET.get('q', '')
    search_type = self.request.GET.get('type', '')

    if len(search_keyword) > 1 :
        context['q'] = search_keyword
    context['type'] = search_type

    return context

@require_POST
@login_required
def follow(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)

    # 프로필에 해당하는 유저를 로그인한 유저가 팔로우 할 수 없음
    if request.user == user:
        messages.warning(request, "스스로 팔로우 할 수 없습니다.")
        return redirect("accounts:detail", pk)

    # 팔로우 상태면, 팔로우 취소를 누르면 삭제
    if request.user in user.followers.all():
        user.followers.remove(request.user)
        is_followed = False

    # 팔로우 상태가 아니면, '팔로우'를 누르면 추가
    else:
        user.followers.add(request.user)
        is_followed = True

    data = {
        "followers_count": user.followers.count(),
        "followings_count": user.followings.count(),
        "is_followed": is_followed,
    }

    return JsonResponse(data)


@login_required
def update(request, pk):
    if request.user.pk != pk:
        return redirect("accounts:profile", pk)

    user = get_object_or_404(get_user_model(), pk=pk)

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect("accounts:profile", pk)
    else:
        profile_form = ProfileForm(instance=user.profile)

    context = {
        "user": user,
        "profile_form": profile_form,
    }

    return render(request, "accounts/update.html", context)
