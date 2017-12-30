from rest_framework.pagination import (
	LimitOffsetPagination,
	PageNumberPagination,
	)


class VideotLimitOffsetPagination(LimitOffsetPagination):
	default_limit = 8
	max_limit = 8

class VideoPageNumberPagination(PageNumberPagination):
	page_size = 5