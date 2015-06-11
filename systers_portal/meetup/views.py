from django.views.generic.detail import DetailView

from meetup.models import MeetupLocation


class MeetupLocationDetailView(DetailView):
    """Meetup Location page view, show only details that user requested"""
    model = MeetupLocation
