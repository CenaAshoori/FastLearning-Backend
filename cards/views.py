from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import CardModel,CategoryModel
from .serializers import CardSerializer,CategorySerializer
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly

import os
from django.conf import settings
from django.http import HttpResponse, Http404


class CardListCreateView(ListCreateAPIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = CardModel.objects.all()
    serializer_class = CardSerializer

class CardRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    allowed_methods = ['GET']
    queryset = CardModel.objects.all()
    serializer_class = CardSerializer

class CategoryListCreateView(ListCreateAPIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
class CategoryModelRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    allowed_methods = ['GET']
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

def download_image(request, image_name):
    image_path = os.path.join(settings.IMAGE_ROOT, image_name)
    if os.path.exists(image_path):
        with open(image_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/jpeg")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(image_name)
            return response
    else:
        raise Http404
def download_file(request, file_name):
    file_path = os.path.join(settings.FILE_ROOT, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/jpeg")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    else:
        raise Http404
