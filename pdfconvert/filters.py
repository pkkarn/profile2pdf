import django_filters
from django_filters import CharFilter
from .models import Customer


class ProfileFilter(django_filters.FilterSet):
    namesearch = CharFilter(field_name="name", lookup_expr='icontains')
    aboutsearch = CharFilter(field_name="about", lookup_expr='icontains')

    class Meta:
        model = Customer
        fields = ['namesearch', 'aboutsearch']
