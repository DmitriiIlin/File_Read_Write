import random

def Create_files(): 
    for i in range(1,11):
        file=open(str(i)+".txt",'wt')
        for _ in range(0,3):
            file.write(str(random.randint(1,100))+'\n')
        file.close()

def Read_information():
    summa=0
    for _ in range(0,2):
        a=input("Введите число в промежутке 1-10: ")
        if int(a)<=10 and int(a)>=1:
            file=open(str(a)+'.txt','rt')
            s=file.readline()
            while s!='':
                summa=summa+int(s.rstrip())
                s=file.readline()
            file.close()
        else:
            print("Некорректный ввод")
            break
    print(summa)

Create_files()
Read_information()

