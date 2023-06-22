import django_filters
from app.models import MusicFile

class MusicFilterForm(django_filters.FilterSet):
    uploader = django_filters.CharFilter(field_name='uploader__email',lookup_expr='icontains')
    ordering = django_filters.OrderingFilter(choices=(('visibility', 'visibility sort'),
                                                      ('title', 'title sort'),
                                                      ),

                                               fields=(('visibility', 'visibility'),
                                                       ('title', 'title'),
                                                       ),)
    class Meta:
        model = MusicFile
        fields = ['visibility']
