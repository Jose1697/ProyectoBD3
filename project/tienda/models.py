
from djongo import models
from django.core.exceptions import ValidationError
from django import forms
from datetime import datetime


class Reclamo(models.Model):
	  _id = models.CharField(max_length=10)
	  tipo_reclamo=models.CharField(max_length=1000)
	  fecha_reclamo=models.DateField()
	  descripcion=models.CharField(max_length=1000)
	  estado=models.IntegerField()
	  prioridad=models.IntegerField()      
	  
	  def _str_(self):
            return self._id 
class ReclamoForm(forms.ModelForm):
	  class Meta:
	        model = Reclamo
	        fields = (
	            '_id',
	        )



class Operador(models.Model):
	  _id =models.CharField(max_length=10)
	  nombre=models.CharField(max_length=1000)
	  fecha_ingreso=models.DateField()
	  fecha_nacimiento=models.DateField()
	  Reclamo=models.ArrayField(model_container=Reclamo,model_form_class=ReclamoForm)
	        
	  def _str_(self):
            return self._id     
                    


class Servicio(models.Model):
	  _id =  models.CharField(max_length=10)
	  tipo_servicio=models.CharField(max_length=1000)
	  costo=models.FloatField()
	  Estado=models.IntegerField()
	        
	  def _str_(self):
            return self._id 
class ServicioForm(forms.ModelForm):
	  class Meta:
	        model = Servicio
	        fields = (
	            '_id',
	        )  



class Cliente(models.Model):
	  _id =models.CharField(max_length=10)
	  nombre=models.IntegerField()
	  apellidos=models.IntegerField()
	  contraseña=models.CharField(max_length=1000)
	  correo=models.CharField(max_length=1000)
	  reclamo=models.ArrayField(model_container=Reclamo,model_form_class=ReclamoForm)
	  servicio=models.ArrayField(model_container=Servicio,model_form_class=ServicioForm)      
	  def _str_(self):
            return self._id 



class Informe(models.Model):
	  _id = models.CharField(max_length=10)
	  fecha_informe=models.IntegerField()
	  observacion=models.IntegerField()
	        
	  class Meta:
            abstract = True


class Tecnico(models.Model):
	  _id = models.CharField(max_length=10)
	  nombre=models.IntegerField()
	  apellidos=models.IntegerField()
	  fecha_ingreso=models.IntegerField()
	  fecha_nacimiento=models.DateField() 
	  servicio=models.ArrayField(model_container=Servicio,model_form_class=ServicioForm)           
	  informe= models.EmbeddedField(model_container=Informe)
	  def _str_(self):
            return self._id 


class TecnicoForm(forms.ModelForm):
	  class Meta:
	        model = Tecnico
	        fields = (
	            '_id',
	        )  

        

class Inventario(models.Model):
	  _id = models.CharField(max_length=10)
	  capacidadinven=models.IntegerField()
	  Estado=models.IntegerField()
	        
	  class Meta:
            abstract = True


class Departamento(models.Model):
      _id = models.CharField(max_length=10)
      direcion=models.CharField(max_length=1000)
      capacidad=models.IntegerField()
      Inventario= models.EmbeddedField(model_container=Inventario)
      def _str_(self):
            return self._id 
class DepartamentoForm(forms.ModelForm):
	  class Meta:
	        model = Departamento
	        fields = (
	            '_id',
	        )  


class Agencia(models.Model):
      ruc= models.CharField(max_length=10)
      nombre: models.CharField(max_length=1000)
      Tecnico:models.CharField(max_length=100)
      Departamento = models.ArrayField(model_container=Departamento)
      Tecnico = models.ArrayField(model_container=Tecnico,model_form_class=TecnicoForm)
      Departamento = models.ArrayField(model_container=Departamento,model_form_class=DepartamentoForm)

 
  















#dd
#BERNILLA SAD OLVIDALA XD
#gazaso54156465
#ga
#hola
#guilermo
#nunca estaras con ella
#Delegada sdfsdfsdfsdfsefdsefsdfsef
#BEELMUTTTTTTTTTTTT
#wfwefwefefe
#51 goles en fifa xdxdxdxdxdxdx
#DAYANITA TE AMO BY JOSE LUIS GAAAAAAAAA
#cambio mio okei