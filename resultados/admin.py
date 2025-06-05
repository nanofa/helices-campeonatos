from django.contrib import admin
from .models import Tirador, Campeonato, Resultado, Categoria, Equipo, Club, Federacion, Cancha, Tiro

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
admin.site.register(Cancha)
admin.site.register(Tiro)

# Register your models here.
