from django.db import models

class Tirador(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    licencia = models.CharField(max_length=50, unique=True, blank=True, null=True)
    club = models.ForeignKey('Club', on_delete=models.SET_NULL, null=True, blank=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=True)
    equipo = models.ForeignKey('Equipo',on_delete=models.SET_NULL,null=True,blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
    class Meta:
        verbose_name = "Tirador"
        verbose_name_plural = "Tiradores"


class Campeonato(models.Model):
    nombre = models.CharField(max_length=150)
    fecha = models.DateField()
    club = models.ForeignKey('Club', on_delete=models.SET_NULL, null=True, blank=True)
    temporada = models.CharField(max_length=10)

    TIPO_CHOICES = [
        ('Nacional', 'Nacional'),
        ('Autonómico', 'Autonómico'),
        ('Internacional', 'Internacional'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return f"{self.nombre} ({self.temporada})"

    class Meta:
        verbose_name = "Campeonato"
        verbose_name_plural = "Campeonatos"

class Resultado(models.Model):
    tirador = models.ForeignKey('Tirador', on_delete=models.CASCADE)
    campeonato = models.ForeignKey('Campeonato', on_delete=models.CASCADE)
    puntuacion = models.IntegerField()

    def __str__(self):
        return f"{self.tirador} - {self.campeonato} - {self.puntuacion} ptos"
    
    def calcular_posicion(self):
        resultados = Resultado.objects.filter(
            campeonato=self.campeonato
        ).order_by('-puntuacion', 'id')  # En caso de empate, orden estable
        posiciones = {r.id: i + 1 for i, r in enumerate(resultados)}
        return posiciones.get(self.id)

    class Meta:
        verbose_name = "Resultado"
        verbose_name_plural = "Resultados"

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    club = models.ForeignKey('Club', on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

class Club(models.Model):
    nombre = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100, blank=True)
    federacion = models.ForeignKey('Federacion',on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Club"
        verbose_name_plural = "Clubes"

class Federacion(models.Model):
    nombre = models.CharField(max_length=100)
    ambito = models.CharField(
        max_length=50,
        choices=[
            ('Autonómica', 'Autonómica'),
            ('Nacional', 'Nacional'),
            ('Internacional', 'Internacional')
        ]
    )
    pais = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Federación"
        verbose_name_plural = "Federaciones"