"""users admin calsses."""

# Django
from django.contrib import admin

# Models
from users.models import Profile


# list_editable es para pode editar los campos sin tener que entrar al
# parametro.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''Admin View for Profile'''

    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    # list_display_links es para poder acceder al objeto a traves de dicho
    # parametro .
    list_display_links = ('pk', 'user')
    # search_fields se utiliza para poder agregar la busqueda a mi modelo en el
    # admin y los parametros que se le mandan son por los que puedo buscar
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name'
    )

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
        )
