#O código quando executado, pedirá que você digite o nome da face primeiro.
# Em seguida, ele usará o haarcascade para encontrar o rosto no fluxo da câmera.
# Ele irá procurar 50 amostras cada no intervalo de 100ms.
# Uma vez que 50 faces de amostra foram encontradas, ele armazena os dados de amostra no diretório 'baseDados' dentro do diretório de trabalho.

import cv2
import numpy as np
import sqlite3
import os

#Inicio a conexão com o Banco de Dados
conn = sqlite3.connect('database.db')

#Se não existir a pasta para armazenar as fotos, crio ela.
if not os.path.exists('./baseDados'):
    os.makedirs('./baseDados')

c = conn.cursor()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

#Armazeno o nome da face no banco de dados antes de iniciar
nome = input("Digite um nome para a Face e tecle ENTER: ")
c.execute('INSERT INTO usuarios (nome) VALUES (?)', (nome,))

uid = c.lastrowid

sampleNum = 0

while True:
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		sampleNum = sampleNum+1
		cv2.imwrite("baseDados/user."+str(uid)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
		cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
		cv2.waitKey(100)
	cv2.imshow('img',img)
	cv2.waitKey(1);
	if sampleNum > 50:
		break
cap.release()

conn.commit()

conn.close()
cv2.destroyAllWindows()