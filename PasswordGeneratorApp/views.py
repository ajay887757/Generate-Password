from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from random import randint , random , choices ,choice

class GeneratePassword(APIView):
    def get(self,request):
        try:
            data=request.GET
            thepass = ""
            length = request.GET.get('length')
            length = int(length)
            characters = list('abcdefghijklmnopqrstuvwxyz')
            
            if eval(request.GET.get('uppercase')):
                characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        
            if eval(request.GET.get('special')):
                characters.extend(list('£$%^&*!{}()'))
            
            if eval(request.GET.get('numbers')):
                characters.extend(list('0123456789'))
        
            i=0
            while i < length:
                i=i+1
                thepass = thepass + choice(characters)
            return Response({'password': thepass})

        except Exception as e :
            return Response ({"message":str(e)})

            