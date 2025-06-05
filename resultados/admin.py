from django.contrib import admin
from .models import Tirador, Campeonato, Resultado, Categoria, Equipo, Club, Federacion

@admin.register(Resultado)
class ResultadoAdmin(admin.ModelAdmin):
    list_display = ('tirador', 'campeonato', 'puntuacion', 'posicion')

    def posicion(self, obj):
        return obj.calcular_posicion()
    posicion.short_description = "Posición"

admin.site.register(Tirador)
admin.site.register(Campeonato)
admin.site.register(Categoria)
admin.site.register(Equipo)
admin.site.register(Club)
admin.site.register(Federacion)

# Register your models here.
