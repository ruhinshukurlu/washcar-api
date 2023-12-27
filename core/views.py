from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class ListUsers(APIView):

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = ['salam']
        return Response(usernames)