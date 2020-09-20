from django.urls import path
from pdfconvert import views


urlpatterns = [
    path('', views.main, name="customer_view"),
    path('add/', views.add_profile, name="add_profile"),
    path('pdf/<int:pk>/', views.customer_render_pdf, name="cutomerpdf"),
    path('test/<int:pk>/', views.render_pdf_view, name="test-view"),

]
