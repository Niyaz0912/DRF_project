from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from sections.models import Section, Content, Tests
from sections.permissions import IsModerator
from sections.serializers.sections_serializers import SectionListSerializer, SectionSerializer
from sections.serializers.section_content_serializers import SectionContentListSerializer, ContentSerializer

from sections.serializers.tests_serializers import TestsSerializer, TestQuestionSerializer
from sections.paginators import SectionPaginator, SectionContentPaginator, TestPaginator


class SectionListAPIView(ListAPIView):
    serializer_class = SectionListSerializer
    queryset = Section.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = SectionPaginator


class SectionCreateAPIView(CreateAPIView):
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser | IsModerator]


class SectionRetrieveAPIView(RetrieveAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = [IsAuthenticated]


class SectionUpdateAPIView(UpdateAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsModerator]


class SectionDestroyAPIView(DestroyAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsModerator]


class ContentListAPIView(ListAPIView):
    serializer_class = SectionContentListSerializer
    queryset = Content.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = SectionContentPaginator


class ContentCreateAPIView(CreateAPIView):
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser | IsModerator]


class ContentRetrieveAPIView(RetrieveAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = [IsAuthenticated]


class ContentUpdateAPIView(UpdateAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsModerator]


class ContentDestroyAPIView(DestroyAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsModerator]


class TestListAPIView(ListAPIView):
    serializer_class = TestsSerializer
    queryset = Tests.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = TestPaginator


class TestQuestionRetrieveAPIView(RetrieveAPIView):
    serializer_class = TestQuestionSerializer
    queryset = Tests.objects.all()

    # permission_classes = [IsAuthenticated]

    def post(self, request,*args, **kwargs):
        answers = [test.answer for test in Tests.objects.all()]
        answer = answers[self.kwargs.get('pk') - 1]. lower()
        user_answer = request.data.get('user_answer').lower()
        is_correct = user_answer == answer
        return Response({'is_correct': is_correct})
