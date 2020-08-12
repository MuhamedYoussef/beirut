from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='core/index.html'), name='index'),
    
    path ('aid_record', AidRecordView.as_view(), name='aid_record'),
    path ('aid_record_list', AidRecordListView.as_view(), name='aid_record_list'),
    path ('aid_record/<str:id>', AidRecordDetailView.as_view(), name='aid_record_detail'),   
    
    path('aid_record_success', TemplateView.as_view(template_name='core/aid_record_success.html'), name='aid_record_success'),
    
    path ('offer', OfferView.as_view(), name='offer')   

]
