from rest_framework.pagination import PageNumberPagination

class DefaultPagination(PageNumberPagination):
    page_size = 10  # default
    page_size_query_param = 'page_size'  # allow clients to change it: ?page_size=20
    max_page_size = 100  # limit to avoid abuse