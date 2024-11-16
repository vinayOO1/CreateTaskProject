from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from task.utils import custom_celery_handler


# Create your views here.
class TaskCreateList(APIView):

    def post(self, request):

        try:
            # Trigger the Celery task
            custom_celery_handler()
            # Return a valid JSON response
            return Response({"message": "Task triggered successfully!"}, status=status.HTTP_200_OK)
        except Exception as e:
            # Handle any errors and return a proper JSON error response
            return Response(
                {"error": str(e), "message": "Failed to trigger task."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        # # calling task on celery
        # custom_celery_handler()
        # success_data = {}
        # message = 'Task created successfully'
        # return HttpResponse({'data': success_data, 'message': message, 'error': False}, status=status.HTTP_200_OK)
