from rest_framework.views import APIView
from .serializers import studentSerializer
from .models import studentDetails
from django.http.response import JsonResponse,Http404  
class studentView(APIView):

    # POST request to create a new student
    def post(self, request):
        data = request.data  
        print("Received POST data:", data)
        serializer = studentSerializer(data=data)  # Serialize the data

        if serializer.is_valid():  # If data is valid
            serializer.save()  
            print("Student created successfully") 
            return JsonResponse({"message": "Student created successfully"}, safe=False, status=201)
        
        print("Failed to create student:", serializer.errors) 
        return JsonResponse({"error": "Failed to add student"}, safe=False, status=400)

    def get_student(self,pk):
        try:
            student = studentDetails.objects.get(stdId=pk)
            return student
        except studentDetails.DoesNotExist():
            raise Http404                                                                                                                                                                                                                         
    def get(self, request, pk=None):  
        if pk:
            student = self.get_student(pk) 
            serializer = studentSerializer(student)  
            return JsonResponse(serializer.data, safe=False)  
        else:
            students = studentDetails.objects.all()  
            serializer = studentSerializer(students, many=True)  
            return JsonResponse(serializer.data, safe=False)
    def put(self,request,pk=None):
        try:
            student_update = studentDetails.objects.get(stdId=pk) 
        except studentDetails.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, safe=False, status=404)

        serializer = studentSerializer(instance=student_update, data=request.data, partial=True)  


        if serializer.is_valid():
            serializer.save()
            return JsonResponse("update successfulla",safe=False)
        return JsonResponse("faild to update")
    def delete(self,request,pk=None):
        try:
            student_delete = studentDetails.objects.get(stdId=pk) 
        except studentDetails.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, safe=False, status=404) 

        student_delete.delete()  
        return JsonResponse({"message": "Deleted successfully"}, safe=False, status=204)  
