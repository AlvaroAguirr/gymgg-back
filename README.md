# Dockerizacion del backend 
Para tener el proyecto dockerizado necesitas realizar estos pasos:
 - actualiza el proyecto en la rama master
 - Abre la aplicacion de docker
 -  abre la terminal y dirigirte a la ruta donde se encuetran los archivos de `Dockerfile` y `doker-compose.yml`
## Creación y levantamiento del contenedor por primera vez

- una vez hubicado en la ruta de los archivos relizaras este comando ` docker compose up --build `
- despues de que haya terminado el proceso abriraras **otra terminal** e iras a la misma ruta y ejecutas el siguiente comando `docker ps`
- te mostara algo como esto

   ` CONTAINER ID      IMAGE            COMMAND                NAMES`

   `xxxxxxxxxxxx   gymgg-back-web   "sh -c ' python mana…"     django_app`   

   Copiaras el container id y escribiras el siguente comando para abrir la termianl de bash, necesaria para crear un superUser`docker exec -it CONTAINER-ID bash`
  cambiara un poco el formato de la terminal haras lo siguiente
  - buscar la ruta donde se encuentra el archivo manage.py verifcando carpetas con ``` ls  ``` o `cd`
  - luego ejectuas `python3 manage.py createsuperuser`
  - haras lo que te pide, dar un correo nombre, dar contraseña 2 veces y confirmar
  - listo ya se habra creado el usuario y ahora puedes salir usando `exit` ya podras regresar a la primera terminal para ver la respuestas del servidor
  - para terminar el servicio de docker sobre la terminal donde se ejecuta el docker solo usa el comando de **ctrl + c**
## volver a levantar el contedor
Para esto solo necesitas ejecutar el comando de `docker compose up` en la direccion donde este los archivos mencionados al inicio
puedes cerrar el servicio usando el mismo comando de **ctrl + c**


