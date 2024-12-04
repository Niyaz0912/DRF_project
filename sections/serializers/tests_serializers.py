from rest_framework.serializers import ModelSerializer
from rest_framework.relations import SlugRelatedField

from sections.models import Tests, Section


class TestsSerializer(ModelSerializer):
    test_section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        model = Tests
        fields = ('id', 'test_section',)


class TestQuestionSerializer(ModelSerializer):
    test_section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        model = Tests
        fields = ('id', 'test_section', 'question', )

