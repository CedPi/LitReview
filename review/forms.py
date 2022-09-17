from dataclasses import field
from urllib import request
from django import forms
from django.contrib.auth import get_user
from django.contrib.auth.models import User
from review.models import Ticket, Review, UserFollows


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"
        exclude = ("user",)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        ticket_ids = Review.objects.values_list("ticket_id")
        if "instance" in kwargs:
            ticket_id = kwargs["instance"].ticket_id
            ticket_ids = Review.objects.exclude(ticket_id=ticket_id).values_list(
                "ticket_id"
            )
        self.fields["ticket"].queryset = Ticket.objects.exclude(id__in=ticket_ids)


class FollowUserForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(FollowUserForm, self).__init__(*args, **kwargs)
        choices = User.objects.exclude(id__in=[user.id])
        users = forms.ModelChoiceField(required=True, queryset=choices)
        self.fields['followed_user'] = users

    class Meta:
        model = UserFollows
        fields = "__all__"
        exclude = ("user",)
