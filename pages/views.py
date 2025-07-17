from django.shortcuts import render

def home(request):
    # Si en el futuro se pasan páginas, usar helpers funcionales
    # from .utils import filter_public_pages, get_page_titles
    # pages = Page.objects.all()
    # public_pages = filter_public_pages(pages)
    # page_titles = get_page_titles(public_pages)
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')
