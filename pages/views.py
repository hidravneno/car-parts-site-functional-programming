from django.shortcuts import render

def home(request):
    # Ejemplo de uso de helpers funcionales si tuvieras un modelo Page
    # from .models import Page
    # from .utils import filter_public_pages, get_page_titles, get_page_urls
    # pages = Page.objects.all()
    # public_pages = filter_public_pages(pages)
    # page_titles = get_page_titles(public_pages)
    # page_urls = get_page_urls(public_pages)
    # context = {
    #     'page_titles': page_titles,
    #     'page_urls': page_urls,
    # }
    # return render(request, 'pages/home.html', context)
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')
