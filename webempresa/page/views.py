from django.shortcuts import render, get_object_or_404

from page.models import Page


def page(request, page_id, page_title):
    pages = get_object_or_404(Page, id=page_id)
    return render(request, 'page/sample.html', {'page': pages})
