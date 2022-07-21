from dataclasses import field
from django import forms
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
    class Meta:
        model = UserFollows
        fields = "__all__"
        exclude = ("user",)
