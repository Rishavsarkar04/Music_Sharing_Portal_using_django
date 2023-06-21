import django_filters
from app.models import MusicFile

class MusicFilterForm(django_filters.FilterSet):
    uploader = django_filters.CharFilter(field_name='uploader__email',lookup_expr='icontains')
    class Meta:
        model = MusicFile
        fields = ['visibility']
