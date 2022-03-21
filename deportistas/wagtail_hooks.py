from wagtail.contrib.modeladmin.options import (ModelAdmin, ModelAdminGroup, modeladmin_register)

from deportistas.models import deportista

'''
N.B. To see what icons are available for use in Wagtail menus and StreamField block types,
enable the styleguide in settings:

INSTALLED_APPS = (
   ...
   'wagtail.contrib.styleguide',
   ...
)

or see http://kave.github.io/general/2015/12/06/wagtail-streamfield-icons.html

This demo project includes the full font-awesome set via CDN in base.html, so the entire
font-awesome icon set is available to you. Options are at http://fontawesome.io/icons/.
'''


class DeporistasAdmin(ModelAdmin):
    # These stub classes allow us to put various models into the custom "Wagtail Bakery" menu item
    # rather than under the default Snippets section.
    model = deportista
    search_fields = ('year', 'nombre', 'deporte')
    menu_icon = 'site' 
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('nombre', 'year', 'deporte')
    list_filter = ( 'deporte',)
class DeportistasAdminGroup(ModelAdminGroup):
    
    menu_icon = 'site' 
    items = ()




# When using a ModelAdminGroup class to group several ModelAdmin classes together,
# you only need to register the ModelAdminGroup class with Wagtail:
modeladmin_register(DeporistasAdmin)
