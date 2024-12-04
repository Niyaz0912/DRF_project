from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from sections.models import Section, SectionContent
from sections.permissions import IsModerator
from sections.serializers.sections_serializers import SectionListSerializer,SectionSerializer
from sections.serializers.section_content_serializers import SectionContentListSerializer, SectionContentSerializer
from sections.paginators import SectionPaginator, SectionContentPaginator


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