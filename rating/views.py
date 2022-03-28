from rest_framework.viewsets import ModelViewSet
from rating.models import Rating
from rating.serializers import RatingSerializer


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
