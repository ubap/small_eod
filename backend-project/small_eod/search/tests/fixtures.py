from ..filterset import BaseFilterSet
from django.db.models import Q

class DemoFilterSet(BaseFilterSet):
    search_fields = ['name']
    filters = {
        'a': lambda value: Q(a=value)
    }