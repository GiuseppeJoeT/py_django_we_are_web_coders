from rest_framework import generics
from models import Poll, Thread, PollSubject
from serializers import PollSerializer, VoteSerializer


class PollViewSet(generics.ListAPIView):
    queryset = Poll.objects.all()
    #  we want all the objects in the Poll model to be used.
    serializer_class = PollSerializer
