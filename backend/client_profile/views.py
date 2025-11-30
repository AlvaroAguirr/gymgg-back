from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import ClientProfile
from .serializers import ClientProfileSerializer

# --- Función Auxiliar ---
def check_staff_access(user):
    """Verifica si el usuario es staff o superuser."""
    return user.is_staff or user.is_superuser

# --- Vistas de API ---

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_client_profile(request):
    # Obtiene el perfil de fitness del usuario autenticado y lo serializa.

    user = request.user

    # RESTRICCIÓN DE SEGURIDAD
    if check_staff_access(user):
        return Response(
            {"error": "Acceso denegado. Los usuarios de staff no tienen un perfil de cliente asociado."},
            status=status.HTTP_403_FORBIDDEN
        )
        
    try:
        profile = ClientProfile.objects.get(user=user)
        # Usamos el Serializer para convertir el objeto Django a JSON
        serializer = ClientProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    except ClientProfile.DoesNotExist:
        return Response(
            {"message": "Perfil no encontrado."}, 
            status=status.HTTP_404_NOT_FOUND
        )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_client_profile(request):

    # Guarda o actualiza el perfil de fitness del usuario autenticado usando el Serializer.
    user = request.user
    
    # RESTRICCIÓN DE SEGURIDAD
    if check_staff_access(user):
        return Response(
            {"error": "Acceso denegado. Los usuarios de staff no pueden guardar perfiles de cliente."},
            status=status.HTTP_403_FORBIDDEN 
        )
    
    # Determinar si vamos a actualizar un perfil existente o crear uno nuevo
    try:
        profile = ClientProfile.objects.get(user=user)
        # Inicializar Serializer para actualización
        serializer = ClientProfileSerializer(profile, data=request.data, partial=False)
        
    except ClientProfile.DoesNotExist:
        # Inicializar Serializer para creación
        serializer = ClientProfileSerializer(data=request.data)

    # 1. Validar los datos de entrada
    if serializer.is_valid():
        
        # 2. Guardar en la base de datos
        if 'profile' in locals():
            # Actualizar
            profile = serializer.save(user=user) 
            created = False
        else:
            # Crear
            profile = serializer.save(user=user)
            created = True
        
        # Retornar una respuesta de éxito con los datos del perfil
        return Response({
            "message": "Perfil de fitness guardado exitosamente.",
            "created": created,
            "profile": serializer.data 
        }, status=status.HTTP_200_OK)
    
    # 3. Si la validación falla
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)