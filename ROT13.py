def ROT13(randomstring):
    stri = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    stri2 = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    list = []
    list[:0] = randomstring
    list1 = []
    list1[:0] = stri
    list2 = []
    list2[:0] = stri2
    megethos = 0
    for i in list:
        megethos = megethos + 1  # megethos randomstring anti gia len(list)
    for i in range(megethos):
        for j in range(26):
            if list[i] == list2[j]:
                list[i] = list2[j + 13]
                break
            if list[i] == list1[j]:
                list[i] = list1[j + 13]
                break
    FINAL = ''
    for i in list:
        FINAL = FINAL + i
    return FINAL

'''Για input ο παρακατω κωδικας
dikiasouleksi=input('ΒΑΛΕ ΤΗΝ ΛΕΞΗ ΣΟΥ:')
ROT13(dikiasouleksi)'''





'''2ος ΤΡΟΠΟΣ
    def Rot13(randomstring):
       mytrans=str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
       'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
       return randomstring.translate(mytrans)


    text=input('ΒΑΛΕ ΤΥΧΑΙΑ ΛΕΞΗ ΜΕ ΛΑΤΙΝΙΚΟΥΣ ΧΑΡΑΚΤΗΡΕΣ:')
    Rot13(text)


    3ος ΤΡΟΠΟΣ
    def Rot13(randomstring):
        mytrans = {97:110,98:111,99:112,100:113,101:114,102:115,103:116,104:117,105:118,106:119,107:120,108:121,109:122,
              110:97,111:98,112:99,113:100,114:101,115:102,116:103,117:104,118:105,119:106,120:107,121:108,122:109,
              65:78,66:79,67:80,68:81,69:82,70:83,71:84,72:85,73:86,74:87,75:88,76:89,77:90,78:65,79:66,80:67,81:68,
              82:69,83:70,84:71,85:72,86:73,87:74,88:75,89:76,90:77}
        return randomstring.translate(mytrans)

    txt=input('ΒΑΛΕ ΤΥΧΑΙΑ ΛΕΞΗ ΜΕ ΛΑΤΙΝΙΚΟΥΣ ΧΑΡΑΚΤΗΡΕΣ:')
    Rot13(txt)'''





