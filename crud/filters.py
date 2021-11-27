import django_filters
from django_filters import NumberFilter,CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
    start_salary = NumberFilter(field_name='salary', lookup_expr='lte')
    end_salary = NumberFilter(field_name='salary', lookup_expr='gte')
    name = CharFilter(field_name='name',lookup_expr='icontains')
    surname = CharFilter(field_name='surname',lookup_expr='icontains')

    class Meta:
        model = Users
        fields = ('name','surname','phone','email','cname')

