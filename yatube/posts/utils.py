from django.conf import settings
from django.core.paginator import Paginator


def get_paginator(posts, request):
    paginator = Paginator(posts, settings.POST_NUM)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return {
        'paginator': paginator,
        'page_number': page_number,
        'page_obj': page_obj,
    }
