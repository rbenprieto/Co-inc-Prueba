Para levantar el proyecto solo es necesario tener instalado el interprete de python y el framework django. 

Una vez tengan ambos instalados 

1. escribir en la consola, ubicado en la ruta donde se encuentran los archivos manage.py y la base de datos
      $ python manage.py runserver
      
2. Dirigirse al navegador y escribir lo siguiente para ingresar a la app web
      $ localhost:8000 

3. Escribir en el navegador lo siguiente para ingresar al admin
      $ localhost:8000/admin
      
4. Para dejar de verlo pulsar lo siguiente en la consola donde activaron el servidor
      Control + c
      
      
EXPLICACIÓN DE LA SOLUCIÓN 
Esta aplicación web la hice con python utilizando el framework Django con base de datos SQLite3 bajo el modelo cliente-servidor. En esta app se puede ver, añadir y eliminar data. En el back habilité el admin y corrí los templates con Jinja 2, además de usar los mejores estándares que conozco en la conexión de archivos. Realicé integración entre el back y front mediante el ORM con distintas formas de visualización. 

En el front usé HTML, CSS, JS y BootStrap 5; Organicé todo bajo el método de estáticos y bloques de contenido, permitiendo escalabilidad ordenada. El formulario se encuentra controlado con validación de contenido con HTML, BootStrap y JS que evitan algunos errores en el diligenciamiento de la información. ¡Ojalá sea de tu agrado y espero verte en la siguiente fase!
