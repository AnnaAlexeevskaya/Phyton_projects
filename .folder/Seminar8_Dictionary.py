# 1. Открыть файл
# 2. Создать контакт
# 3. Изменить контакт
# 4. Найти контакт
# 5. Удалить контакт
# 6. Показать контакты
# 7. Выход

contact = dict()


def Find_Name():
    print("ввдедите фио")
    name=input()
    print('телефон',contact[name][0],'комментарий',contact[name][1])

def Dell_Name():
    print("введите ФИО удаляемого контакта")
    del contact[input()]

def Change_Name():
    print("введите фио изменяемого контакта и новое имя через пробел")
    name1,name2=input().split()
    contact[name2] = contact.pop(name1)
    print('Новое имя контакта',name2,'телефон',contact[name2][0],'комментарий',contact[name2][1])
    
def Append_Name():
    print("введите фио")
    name=input()
    s=[]
    print("введите телефон")
    s.append(input())
    print("введите коментарий")
    s.append(input())
    contact[name]=s
    print('Новый контакт')
    print(name,'телефон',contact[name][0],'комментарий',contact[name][1])
    
def Print_Full_Name():
    for key,value in contact.items():
        print(key,'телефон',value[0], 'комментарий',value[1])

def Copy_to_file():
    # open both files 
    with open('input.txt','r') as firstfile, open('input2.txt','a') as secondfile: 
      
        # read content from first file 
        for line in firstfile: 
               
             # append content to second file 
             secondfile.write(line)
    secondfile.close()
             

def Print_Menu():
    print("Меню:")
    print(" 1: показать контакт")
    print(" 2: удалить контакт")
    print(" 3: изменить контакт")
    print(" 4: добавить новый контакт")
    print(" 5: вывести все контакты на экран")
    print(" 6: копировать все контакты в другой файл")
    print(" 0: выйти из программы")
    
with open('input.txt', 'r+') as contacts:
    A=contacts.readline().split()
    while A:
        contact[A[0]]=A[1:]
        A=contacts.readline().split()
         
Print_Menu()
Menu=[1,2,3,4,5,0]
a=int(input())
#print(contact)
while not (a in Menu):
    Print_Menu()
    a=int(input())
while a:
    if a==1:
       Find_Name() 
    elif a==2:
        Dell_Name()    
    elif a==3:
        Change_Name()
    elif a==4:
        Append_Name()
    elif a==5:
        Print_Full_Name()   
    elif a == 6:
           Copy_to_file()
    
    Print_Menu()
    a=int(input())
    
contacts.close()
contacts=open('input.txt','w')
    
for key,value in contact.items():
    print(key,value)
    contacts.write(str(key)+' ')
    contacts.write(str(value[0])+' ')
    contacts.write(str(value[1])+' ')
    contacts.write('\n')
    
        
        
        
        
        
        