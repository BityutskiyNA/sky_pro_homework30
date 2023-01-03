from rest_framework.viewsets import ModelViewSet

from selection.models import Selection
from selection.serializers import SelectionSerializer


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
