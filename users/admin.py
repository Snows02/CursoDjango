"""users admin calsses."""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
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
    # list_filter se utiliza para poder agregar una barra lateral que nos ayude
    # a encontrar (filtar) los registros que tenemos.
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )
    # fieldsets es para poder agrupar parametros dentro de una categoria
    # estructura: (tupla, (tupla 'name_section',{'fields': (parametros)}))
    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            ),
        }),
        ('Meta data', {
            'fields': (
                ('created', 'modified'),
            )
        }),
    )

    readonly_fields = ('created', 'modified', 'user')


class ProfileInline(admin.StackedInline):
    '''Stacked Inline View for Profile'''

    model = Profile
    can_delete = False
    verbosename_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
