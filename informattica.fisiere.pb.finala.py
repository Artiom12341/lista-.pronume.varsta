with open ('date.copii.txt','r') as f :
    prenume=eval(f.readline())
    varsta=eval(f.readline())
print('a)')
for x in range(len(prenume)):
    print(prenume[x],'are',varsta[x])
prenume.extend(['Andreea','Ioan'])
varsta.extend(['34','23'])
print('b)')
for x in range(len(prenume)):
    print(prenume[x],'are',varsta[x])
print('lista prenume modificata=',prenume)
print('lista varsta modificata=',varsta)
del prenume[2:3]
del varsta[2:3]
print ('c)','prenume fara date Ana=',prenume,'\n''varsta fara  date Ana=',varsta)
print('d)','primele trei elemente din prenume=',prenume[0:3])
print('e)','lista prenume de la dreapta la stanga=',prenume[::-1])
print ('f)','lista prenume cu elementele 2,4=',prenume[2:3],',',prenume[4:5],'\n''lista varsta cu elementele 2,4=',varsta[2:3],',',varsta[4:5],'\n','lista prenume cu elementele 0-5=',prenume[0:6],'\n''lista varsta cu elementele 0-5=',varsta[0:6])