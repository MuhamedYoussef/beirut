from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.views import APIView

from .models import AidRecord
from .serializers import AidRecordSerializer




class AidRecordView(APIView):

    def get(self, request):
        return render(request, 'core/aid_record.html')

    def post(self, request):
        serializer = AidRecordSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return redirect('aid_record')
        
        messages.error(request, 'Something went wrong! Please try again')
        return redirect('aid_record_success')


class AidRecordListView(APIView):

    def get(self, request):
        records = AidRecord.objects.all()
        return render(request, 'core/aid_record_list.html', {'records': records})


class AidRecordDetailView(APIView):
    
    def get(self, request, id):
        record = get_object_or_404(AidRecord, id=id)
        return render(request, 'core/aid_record_detail.html', {'record': record})
