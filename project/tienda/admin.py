from django.contrib import admin

from .models import Agencia
from .models import Reclamo
from .models import Operador
from .models import Servicio
from .models import Cliente
from .models import Tecnico
from .models import Departamento



# Register your models here.


admin.site.register(Agencia)
admin.site.register(Reclamo)
admin.site.register(Operador)
admin.site.register(Servicio)
admin.site.register(Cliente)
admin.site.register(Tecnico)
admin.site.register(Departamento)



