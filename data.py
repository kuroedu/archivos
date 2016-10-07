import csv

with open('data.csv','r')as file:
    data = csv.reader(file, delimiter=',')
    for line in data:
        print line
        
with open('data.csv','a')as file:
    data = csv.writer(file, delimiter=',')
    data.writerow(['Cartoon','mail.mail.god'])