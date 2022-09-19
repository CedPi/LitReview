from django import forms
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
        exclude = ("user", "ticket",)

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        CHOICES = [("0", " 0"),("1", " 1"),("2", " 2"),("3", " 3"),("4", " 4"),("5", " 5"),]
        self.fields["rating"] = forms.ChoiceField(choices=CHOICES, required=True)


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
