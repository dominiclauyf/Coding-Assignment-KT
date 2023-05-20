from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    # Reference https://stackoverflow.com/questions/35432985/django-rest-framework-override-page-size-in-viewset/62843648#62843648
    page_size = 100
    max_page_size = 100
    page_size_query_param = "page_size"
