import sys
import csv
 
print """Agenda
---------------------
1) Leer
2) Insertar Nombre
0) Exit"""
 
while 1:
    char = sys.stdin.read(1)
    if char == "0":
        break
    if char == "1":
        with open('data.csv','r')as file:
            data = csv.reader(file, delimiter ='|')
            for line in data:
                print line
        break
    if char == "2":
        with open('data.csv','a')as file:
            data = csv.writer(file, delimiter=',')
            esp = raw_input("")
            names = raw_input("Ingresa un Nombre:")
            email = raw_input("Ingresa un Email:")
            data.writerow([names,email])
        break
 