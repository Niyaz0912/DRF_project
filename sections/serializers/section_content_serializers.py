from rest_framework.serializers import ModelSerializer
from rest_framework.relations import SlugRelatedField


from sections.models import Section, SectionContent


class SectionContentSerializer(ModelSerializer):
    class Meta:
        model = SectionContent
        fields = '__all__'


class SectionContentSectionSerializer(ModelSerializer):
    class Meta:
        model = SectionContent
        fields = ('id', 'title',)


class SectionContentListSerializer(ModelSerializer):
    section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        model = SectionContent
        fields = ('id', 'section', 'title')
