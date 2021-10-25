alfavit_eu =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_ua = 'АБВГҐДЄЖЗИIЙЇКЛМНОПРСТУФХЦЧШЩЬЮЯ'
shu=input("+ чи -: ")
krok = int(input('крок: '))
message = input("повідомлення: ").upper()
end = ''
lang = input('мова ua/eu: ')
if shu == '+':  
    if lang == 'ua':
        for i in message:
            loc = alfavit_ua.find(i)
            new_loc = loc + krok
            if i in alfavit_ua:
                end += alfavit_ua[new_loc]
            else:
                end += i
    else:
        for i in message:
            loc = alfavit_eu.find(i)
            new_loc = loc + krok
            if i in alfavit_eu:
                end += alfavit_eu[new_loc]
            else:
                end += i
    print (end)
else:
    if lang == 'ua':
        for i in message:
            loc = alfavit_ua.find(i)
            new_loc = loc - krok
            if i in alfavit_ua:
                end += alfavit_ua[new_loc]
            else:
                end += i
    else:
        for i in message:
            loc = alfavit_eu.find(i)
            new_loc = loc - krok
            if i in alfavit_eu:
                end += alfavit_eu[new_loc]
            else:
                end += i
    print (end)