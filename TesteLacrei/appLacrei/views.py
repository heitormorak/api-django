from rest_framework import viewsets
from rest_framework.response import Response
from appLacrei.models import Profissional, Consulta
from appLacrei.serializer import ProfissionalSerializer, ConsultaSerializer

class ProfissionaisViewSet(viewsets.ModelViewSet):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer

class ConsultasViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    def list(self, request, *args, **kwargs):
        profissional_id = self.request.query_params.get('profissional_id')
        
        if profissional_id:
            queryset = Consulta.objects.filter(profissional__id=profissional_id)
        else:
            queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
