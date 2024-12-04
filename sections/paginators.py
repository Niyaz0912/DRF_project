from rest_framework.pagination import PageNumberPagination


class SectionPaginator(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10


class SectionContentPaginator(SectionPaginator):
    page_size = 10


class TestPaginator(SectionPaginator):
    page_size = 5
