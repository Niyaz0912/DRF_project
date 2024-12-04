from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField

from sections.models import Section, SectionContent
from sections.serializers.section_content_serializers import SectionContentSectionSerializer


class SectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class SectionListSerializer(ModelSerializer):
    section_content_title = SerializerMethodField()

    def get_section_content_data(self, section):
        return SectionContentSectionSerializer(SectionContent.objects.filter(section=section), many=True).data

    class Meta:
        model = Section
        fields = ('id', 'title', 'section_content_title')
