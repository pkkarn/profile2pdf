from django.urls import path
from pdfconvert import views


urlpatterns = [
    path('', views.CustomerListView.as_view(), name="customer_view"),
    path('pdf/<int:pk>/', views.customer_render_pdf, name="cutomerpdf"),
    path('test/<int:pk>/', views.render_pdf_view, name="test-view"),

]
