from rest_framework.views import APIView
from .serializers import studentSerializer
from .models import studentDetails
from django.http import JsonResponse, Http404  
import random 
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class studentView(APIView):

    def get(self, request, pk=None): 
        try:
            if pk:
                student = studentDetails.objects.get(stdId=pk)
                serializer = studentSerializer(student) 
                return JsonResponse(serializer.data, safe=False)  
            else:
                students = studentDetails.objects.all()  
                serializer = studentSerializer(students, many=True)  
                return JsonResponse(serializer.data, safe=False)
        except studentDetails.DoesNotExist:
            raise Http404('Student not found!!!')

    def post(self, request):
        data = request.data  
        print("Received POST data:", data)  # Log incoming data for debugging
        try:
            serializer = studentSerializer(data=data)  
            if serializer.is_valid(): 
                serializer.save()  
                print("Student created successfully") 
                return JsonResponse({"message": "Student created successfully"}, safe=False, status=201)
            else:
                # Log and return validation errors
                print("Validation failed:", serializer.errors)
                return JsonResponse({"error": "Validation failed", "details": serializer.errors}, status=400)
        except Exception as e:
            # Log any unexpected exceptions
            print("Unexpected error:", str(e))
            return JsonResponse({"error": "Unexpected error occurred"}, status=405)
    

    def put(self, request, pk):
        try:
            student_update = studentDetails.objects.get(stdId=pk) 
        except studentDetails.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, safe=False, status=404)

        serializer = studentSerializer(instance=student_update, data=request.data, partial=True)  

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Update successful"}, safe=False)
        return JsonResponse({"error": "Failed to update"}, safe=False, status=400)

    def delete(self, request, pk=None):
        if pk:
            try:
                student_delete = studentDetails.objects.get(stdId=pk) 
            except studentDetails.DoesNotExist:
                return JsonResponse({"error": "Student not found"}, safe=False, status=404) 
            student_delete.delete()  
            return JsonResponse({"message": "Deleted successfully"}, safe=False, status=204)
        else:
            student_delete = studentDetails.objects.all()
            student_delete.delete()
            return JsonResponse({"Deleted": "All student data was deleted"}, safe=False)
    
class GradingView(APIView):
    stored_score = None

    def post(self, request, pk=None):
        if not pk:
            return JsonResponse({"error": "Student ID is required"}, safe=False, status=400)
        score = request.data.get('score')
        print("Received score:", score)

        try:
            student = studentDetails.objects.get(stdId=pk)
            if score is not None:
                student.Score = score
                student.save()
                return JsonResponse({"message": "Score updated successfully", "Score": student.Score}, safe=False, status=200)
            else:
                
                score = random.randint(0, 100)
                student.Score = score
                student.save()
                GradingView.stored_score = score
                return JsonResponse({"score": score, "message": "Grading completed."}, safe=False)
        except studentDetails.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, safe=False, status=404) 

    def get(self, request, pk=None):
        if pk:
            try:
                score = studentDetails.objects.values('Score').get(stdId=pk)['Score']
                return JsonResponse({"Score": score}, safe=False)
            except studentDetails.DoesNotExist:
                return JsonResponse({"error": "Student not found"}, safe=False, status=404)
        else:
            return JsonResponse({"error": "Please provide a student ID"}, safe=False, status=400)
