"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from unicodedata import name
from django import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from django.urls import path
import authentication.views
import review.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", review.views.home_page, name="home"),
    path("all-posts", review.views.all_posts, name="all-posts"),
    path("signup/", authentication.views.signup_page, name="signup"),
    path(
        "login/",
        LoginView.as_view(
            template_name="authentication/login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path(
        "password-change/",
        PasswordChangeView.as_view(
            template_name="authentication/password_change.html",
            success_url="/password-change-done",
        ),
        name="password-change",
    ),
    path(
        "password-change-done/",
        PasswordChangeDoneView.as_view(
            template_name="authentication/password_change_done.html"
        ),
        name="password-change-done",
    ),
    path("ticket/add/", review.views.ticket_add, name="ticket-add"),
    path("ticket/<int:ticket_id>/edit/", review.views.ticket_edit, name="ticket-edit"),
    path("ticket/list/", review.views.ticket_list, name="ticket-list"),
    path(
        "ticket/<int:ticket_id>/delete/", review.views.ticket_delete, name="ticket-delete"
    ),
    path("review/add/", review.views.review_add, name="review-add"),
    path("review/add/<int:ticket_id>", review.views.review_add, name="review-answer"),
    path("review/<int:review_id>/edit/", review.views.review_edit, name="review-edit"),
    path("review/list/", review.views.review_list, name="review-list"),
    path(
        "review/<int:review_id>/delete/", review.views.review_delete, name="review-delete"
    ),
    path("subscriptions/", review.views.subscriptions, name="subscriptions"),
    path(
        "subsciption/<int:sub_id>/cancel",
        review.views.subscription_cancel,
        name="subscription-cancel",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
