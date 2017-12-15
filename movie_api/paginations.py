from rest_framework.pagination import (
	LimitOffsetPagination,
	PageNumberPagination
	)


class ListMoviesPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'    
