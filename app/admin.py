from django.contrib import admin
from .models import *

admin.site.site_header='Administración Sitio Arriendos'
admin.site.index_title='Panel De Control'
admin.site.site_title='Arriendos'

# class Usuario(admin.ModelAdmin):
#     list_display=('name')
#     model=Usuario
    
    
# class CustomUserAdmin(UserAdmin):
#     # add_form=  UsuarioCreationForm
#     # form=UsuarioChangeForm
#     model = Usuario
#     list_display =['username','apellidos', 'email', 'tipo de usuario',  'is_staff']
#     fieldsets = UserAdmin.fieldsets + (
#         (None,{'fields':('nombre','apellidos', 'rut', 'direccion', 'telefono','tipo de usuario','correo_electronico')}),
#         )
#     add_fieldsets=UserAdmin.add_fieldsets + ( # type: ignore
#         (None,{'fields':('nombre','apellidos', 'rut', 'direccion', 'telefono','tipo de usuario','correo_electronico')}),
#         )
  
# admin.site.register(Usuario, CustomUserAdmin)
    
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Propiedad)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Solicitud_Arriendo)