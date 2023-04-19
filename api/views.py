from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

# ---------------------Model ViewSet-------------------------------------------

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# --------------------Read Only Model ViewSet----------------------------------

# class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer