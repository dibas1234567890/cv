
import io
from django.http import FileResponse
from django.views import View
from django.shortcuts import HttpResponse, render
from reportlab.pdfgen import canvas


class resume_downloader_view(View):
    def cv_exporter(request):
        path = 'Dibas_Basnet_Resume_June_2024.pdf'
        
        

        response = FileResponse(open(path, 'rb'), as_attachment=True)
        return response
    
    def index(request):
        content = "Get the CV Below"
        return render(request, 'index.html', {'content':content})
