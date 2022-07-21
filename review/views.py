from urllib import response
from django.db import IntegrityError
from django.db.models import Q
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from review.forms import TicketForm, ReviewForm, FollowUserForm
from review.models import Ticket, Review, UserFollows


@login_required
def home_page(request):
    posts = []
    reviews = Review.objects.all().order_by("time_created")
    closed_tickets = reviews.values_list("ticket_id", flat=True)
    tickets = Ticket.objects.all().order_by("time_created")
    posts += list(reviews) + list(tickets)
    posts.sort(key=lambda o: (o.time_created), reverse=True)
    print(closed_tickets)
    return render(
        request,
        "review/home.html",
        context={"posts": posts, "closed_tickets": closed_tickets},
    )


@login_required
def ticket_add(request):
    form = TicketForm(initial={"user": request.user})
    print(request.user)
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user_id = request.user.id
            ticket.save()
            return redirect("ticket-list")
    return render(request, "review/ticket_add.html", context={"form": form})


@login_required
def ticket_edit(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save()
            return redirect("ticket-list")
    else:
        form = TicketForm(instance=ticket)
        return render(
            request,
            "review/ticket_add.html",
            context={"form": form, "title": ticket.title},
        )


@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(user_id=request.user.id)
    return render(request, "review/ticket_list.html", context={"tickets": tickets})


@login_required
def ticket_delete(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if ticket.user.id == request.user.id:
        ticket.delete()
        messages.success(request, f"Le ticket {ticket} a bien été supprimé")
    else:
        messages.warning(request, f"Action interdite")
    return redirect("ticket-list")


@login_required
def review_add(request, ticket_id=None):
    init_form = {}
    if ticket_id is not None:
        init_form["ticket"] = ticket_id
    form = ReviewForm(initial=init_form)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user_id = request.user.id
            review.save()
            return redirect("review-list")
    return render(request, "review/review_add.html", context={"form": form})


@login_required
def review_edit(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect("review-list")
    else:
        form = ReviewForm(instance=review)
        return render(
            request,
            "review/review_add.html",
            context={"form": form, "title": review.ticket.title},
        )


@login_required
def review_list(request):
    reviews = Review.objects.filter(user_id=request.user.id)
    return render(request, "review/review_list.html", context={"reviews": reviews})


@login_required
def review_delete(request, review_id):
    review = Review.objects.get(id=review_id)
    if review.user.id == request.user.id:
        review.delete()
        messages.success(request, f"La review {review} a bien été supprimée")
    else:
        messages.warning(request, f"Action interdite")
    return redirect("review-list")


@login_required
def subscriptions(request):
    error = None
    User = get_user_model()
    uf = UserFollows.objects.all()
    followed_users = uf.filter(user=request.user.id)
    users = uf.filter(followed_user=request.user.id)
    form = FollowUserForm()
    if request.method == "POST":
        form = FollowUserForm(request.POST)
        if form.is_valid():
            uf = form.save(commit=False)
            uf.user = request.user
            try:
                uf.save()
            except IntegrityError:
                error = f"Vous êtes déjà abonné à {uf.followed_user.username}"
    return render(
        request,
        "review/subscriptions.html",
        context={"users": users, "f_users": followed_users, "form": form, "error": error},
    )


@login_required
def subscription_cancel(request, sub_id):
    sub = UserFollows.objects.filter(id=sub_id)
    sub.delete()
    return redirect("subscriptions")
