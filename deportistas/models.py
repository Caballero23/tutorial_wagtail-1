from django.db import models


from wagtail.core.models import Page 
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models

# Create your models here.
class deportista(models.Model):
    year = models.CharField('year', max_length=250)
    nombre = models.CharField('nombre', max_length=250)
    deporte = models.CharField('deporte', max_length=250)
  

    panels = [
        FieldPanel('year'),
        FieldPanel('nombre'),
        FieldPanel('deporte'),

    ]
    
    

    def __str__(self):
        return f'{self.nombre} ({self.year})({self.deporte})'
    
    list_filter = ('nombre', 'year', 'deporte')

# Modelo de página de deportistas
class DeportistasIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def paginate(self, request, deportistas, *args):
        page = request.GET.get('page')

        paginator = Paginator(deportistas, 10)

        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages


    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        year = request.GET.get('year')
        nombre = request.GET.get('year')
        qs = ''

        if year:
            deportistas = deportista.objects.filter(year__gte=1990, year__lt=2000)
            qs = f'year={year}'
        else:
            deportistas = deportista.objects.all()
            

        context['deportistas'] = deportista.objects.all().order_by('-year')
        context['qs'] = qs

        
        return context