from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Doctors
from .serializers import DoctorsSerializer

# Create your views here.

#get all doctors
@api_view(['GET'])
def getDoctors(request):
    doctors = Doctors.objects.all()
    serializer = DoctorsSerializer(doctors, many=True)
    return Response(serializer.data)

#get single doctor
@api_view(['GET'])
def getDoctor(request, pk):
    doctor = Doctors.objects.get(id=pk)
    serializer = DoctorsSerializer(doctor, many=False)
    return Response(serializer.data)


#add doctor
@api_view(['POST'])
def addDoctor(request):
    serializer = DoctorsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

#update doctor
@api_view(['PUT'])
def updateDoctor(request, pk):
    doctor = Doctors.objects.get(id=pk)
    serializer = DoctorsSerializer(instance=doctor, data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

# delete doctor
@api_view(['DELETE'])
def deleteDoctor(request, pk):
    doctor = Doctors.objects.get(id=pk)
    doctor.delete()

    return Response('Doctor successfully delted!')

