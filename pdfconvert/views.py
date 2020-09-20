from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Customer
from django.views.generic import ListView
from .filters import ProfileFilter
from .forms import CustomerForm


def main(request):
    customers = Customer.objects.all()
    pfilter = ProfileFilter(request.GET, queryset=customers)
    customers = pfilter.qs
    context = {
        'object_list': customers
    }
    return render(request, 'pdfconvert/main.html', context)


def add_profile(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customer_view')
    return render(request, 'pdfconvert/add_profile.html', {'form': form})


def customer_render_pdf(request, pk):
    template_path = 'pdfconvert/pdf2.html'
    customer = Customer.objects.get(id=pk)
    context = {
        'myvar': 'This is content',
        'customer': customer
    }

    response = HttpResponse(content_type='application/pdf')  # specifying type of response
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'   # This is for download
    response['Content-Disposition'] = 'filename="customer.pdf"'  # to display
    template = get_template(template_path)  # storing template
    html = template.render(context)  # rendcering data into template
    pisa_status = pisa.CreatePDF(
        html, dest=response  # html(render data template), response(type of pdf conversion)
    )  # to create and conver pdf

    if pisa_status.err:
        return HttpResponse('we had some errors <pre>' + html + '</pre>')
    return response


def render_pdf_view(request, pk):
    template_path = 'pdfconvert/pdf1.html'
    customer = Customer.objects.get(id=pk)
    context = {
        'myvar': 'This is content',
        'customer': customer
    }

    response = HttpResponse(content_type='application/pdf')  # specifying type of response
    response['Content-Disposition'] = 'attachment;' + ' filename="' + customer.name + '.pdf"'  # This is for download
    # response['Content-Disposition'] = 'filename="report.pdf"'  # to display
    template = get_template(template_path)  # storing template
    html = template.render(context)  # rendcering data into template
    pisa_status = pisa.CreatePDF(
        html, dest=response  # html(render data template), response(type of pdf conversion)
    )  # to create and conver pdf

    if pisa_status.err:
        return HttpResponse('we had some errors <pre>' + html + '</pre>')
    return response
