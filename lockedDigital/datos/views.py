from multiprocessing import context
from rest_framework.views import APIView
from rest_framework.views import Response 

from .models import Reconocimiento
from .serializers import ReconocimientoSerializer

class IndexView(APIView):
    def get (self, request):
        context = {'mensaje':'servidor activo'}
        return Response(context)

