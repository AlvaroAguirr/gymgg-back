from rest_framework import serializers
from .models import ClientProfile

class ClientProfileSerializer(serializers.ModelSerializer):
    # Definimos 'fitnessLevel' con la fuente 'fitness_level' para usar camelCase en JSON 
    # y snake_case en el modelo, manteniendo la coherencia con la aplicación móvil.
    fitnessLevel = serializers.CharField(source='fitness_level')
    
    class Meta:
        model = ClientProfile
        fields = [
            'gender', 
            'age', 
            'condition', 
            'goal', 
            'experience', 
            'duration', 
            'fitnessLevel' # Usamos el campo con camelCase definido arriba
        ]
        # El campo 'user' se manejará automáticamente en la vista, no se expone aquí.

    # Sobrescribimos el método to_representation para asegurar que la salida use 'fitnessLevel'
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # Sanea y renombra la clave de salida
        ret['fitnessLevel'] = ret.pop('fitness_level', ret.get('fitnessLevel'))
        return ret