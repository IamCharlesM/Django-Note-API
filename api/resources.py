from tastypie.resources import ModelResource
from api.models import Note

class NoteResource(ModelResource):
    class Meta:
        # Quesryset, what models the resource is concerned with
        queryset = Note.objects.all()
        resource_name = 'note'