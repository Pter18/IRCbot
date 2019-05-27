# IRCbot  
## Alumnos:
Pedro Alejandro Rodríguez Gallardo  
Isaias Abraham Manzano Cruz

# Uso  
Se debe extraer el comprimido, la contraseña es **malware**. Una vez hecho esto abrir la aplicación de Word que se extrae.  

# Especificaciones  
Aqui se muestran los programas utilizados para crear los binarios que se necesitará para crear el bot. El proyecto final es el archivo Dropper.zip el cual contiene el ejecutable que infecta al equipo.
Una vez infectado el equipo, el malware intenta resolver el nombre de dominio **'examen.practico.abpe'**, posteriormente se intenta conectar al **puerto 6667**.  
En este punto el atacante se puede conectar al servidor y ejecutar comandos. Los comandos disponibles son:  
- !@PING - Envia un mensaje PING al bot y este responde PONG  
- !@hi - Envia un saludo al bot  
- !@run <aplicacion> - Ejecuta la aplicación especificada  
- !@users - Lista los usuarios del sistema  
- !@files <usuario> - Lista los archivos en el directorio Documents del usuario especificado  
- !@cifraArchivo  <ruta_archivo> - Cifra el archivo indicado  
- !@reboot - Reinicia el equipo  
- !@shutdown - Apaga el equipo  

Cuando un archivo es cifrado, se le agrega la terminación .ggez y el nuevo formato es el siguiente:  
+__________________________+  
| Tamaño del archivo.......|  
| original.................|  
+__________________________+  
| Vector de................|  
| inicialización...........|  
+__________________________+  
| Llave AES cifrada........|  
| con RSA..................|  
+__________________________+  
| Archivo cifrado----------|  
| con AES------------------|  
+__________________________+  
