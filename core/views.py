from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.views import APIView

from .models import AidRecord, Offer
from .serializers import *


class AidRecordView(APIView):

    def get(self, request):
        return render(request, 'core/aid_record.html')

    def post(self, request):
        serializer = AidRecordSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return redirect('aid_record_success')
        
        messages.error(request, 'Something went wrong! Please try again')
        return redirect('aid_record')


class AidRecordListView(APIView):

    def get(self, request):
        records = AidRecord.objects.all()
        return render(request, 'core/aid_record_list.html', {'records': records})


class AidRecordDetailView(APIView):
    
    def get(self, request, id):
        record = get_object_or_404(AidRecord, id=id)
        return render(request, 'core/aid_record_detail.html', {'record': record})









class OfferView(APIView):

    def post(self, request):
        serializer = OfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'success'})
        print(serializer.errors)
        return JsonResponse({'msg': 'Something wrong happend'}, status=400)
