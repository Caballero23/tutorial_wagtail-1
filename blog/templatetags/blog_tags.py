from blog.models import BlogCategory as Category
from noticias.models import Noticia
from blog.models import FooterText
from django.template import Library 

register = Library()


@register.inclusion_tag('components/categories_list.html',
                        takes_context=True)
def categories_list(context):
    categories = Category.objects.all()
    return {
        'request': context['request'],
        'categories': categories
    }

@register.inclusion_tag('components/noticias_list.html',
                        takes_context=True)
def noticias_list(context):
    noticias = Noticia.objects.all().order_by('-id')[:5]

    return {
        'request': context['request'],
        'noticias': noticias,
    }

@register.inclusion_tag('components/footer_text.html', takes_context=True)
def get_footer_text(context):
    footer_text = ""
    if FooterText.objects.first() is not None:
        footer_text = FooterText.objects.first().titulo
    return {
        'footer_text': footer_text,
    }