from django.contrib import admin
from .models import ClientProfile

@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    # Configuración para mostrar el modelo ClientProfile en el panel de administración.
    # Campos a mostrar en la lista (tabla) del admin
    list_display = ('user_email', 'gender', 'age', 'fitness_level', 'goal', 'condition')

    # Campos que se pueden usar para filtrar la lista
    list_filter = ('gender', 'fitness_level', 'experience', 'duration')

    # Campos que permiten buscar texto
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'goal')

    # Campos que aparecerán en la página de detalle/edición del perfil
    fieldsets = (
        ('Información del Usuario', {
            'fields': ('user',),
            'description': 'Usuario relacionado. El ID de usuario no puede ser modificado.'
        }),
        ('Datos de Fitness y Objetivos', {
            'fields': ('gender', 'age', 'condition', 'goal', 'experience', 'duration', 'fitness_level'),
            'classes': ('collapse',), # Esto hace que la sección sea plegable inicialmente
        }),
    )

    # Método para obtener el email del usuario (para mostrarlo en list_display)
    @admin.display(description='Email del Usuario')
    def user_email(self, obj):
        return obj.user.email