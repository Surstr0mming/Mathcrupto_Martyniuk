import binascii

with open('Cryptedtext.txt', 'r', encoding='utf-8') as input_file:
    # зчитування вмісту файлу
    cryptotext = input_file.read()
print(cryptotext)


def str2hex(s):
    return binascii.hexlify(bytes(str.encode(s)))


def hex2str(h):
    return binascii.unhexlify(h)


cryptotext_hex = str2hex(cryptotext)
cryptotext_hex = cryptotext_hex.decode('utf-8')
print(cryptotext_hex)

unhexsring = hex2str(cryptotext_hex).decode('utf-8')


m = 0
mas_crypto_hex = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for i_x in range(4):
    for i_y in range(4):
        string = cryptotext_hex[0 + m] + cryptotext_hex[1 + m]
        mas_crypto_hex[i_y][i_x] = string
        m += 2
print(mas_crypto_hex)
print("wwwwwwwwwwwwwwwwww ", mas_crypto_hex)
mas_crypto_hex = [['32', '88', '31', 'e0'],
                  ['43', '5a', '31', '37'],
                  ['f6', '30', '98', '07'],
                  ['a8', '8d', 'a2', '34']]


key = "I wnt to decrypt"
key_hex = str2hex(key)
key_hex = key_hex.decode('utf-8')
print(key_hex)


m = 0
mas_key_hex = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for i_x in range(4):
    for i_y in range(4):
        string = key_hex[0 + m] + key_hex[1 + m]
        mas_key_hex[i_y][i_x] = string
        m += 2

print("eeeeeeeeeeeeeeeeee ", mas_key_hex)
mas_key_hex = [['2b' ,'28' ,'ab' ,'09' ],
               ['7e' ,'ae' ,'f7' ,'cf' ],
               ['15' ,'d2' ,'15' ,'4f' ],
               ['16' ,'a6' ,'88' ,'3c' ]]
decrypted_key = [['2b' ,'28' ,'ab' ,'09' ],
               ['7e' ,'ae' ,'f7' ,'cf' ],
               ['15' ,'d2' ,'15' ,'4f' ],
               ['16' ,'a6' ,'88' ,'3c' ]]




slov = { '0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000',
        '9':'1001', 'a':'1010', 'b':'1011', 'c':'1100', 'd':'1101', 'e':'1110', 'f':'1111'}


for i_x in range(4):
    for i_y in range(4):
        number0 = mas_crypto_hex[i_y][i_x][0]
        number1 = mas_crypto_hex[i_y][i_x][1]
        number0 = slov.get(number0)
        number1 = slov.get(number1)
        mas_crypto_hex[i_y][i_x] = number0 + number1
print(mas_crypto_hex)

for i_x in range(4):
    for i_y in range(4):
        number0 = mas_key_hex[i_y][i_x][0]
        number1 = mas_key_hex[i_y][i_x][1]
        number0 = slov.get(number0)
        number1 = slov.get(number1)
        mas_key_hex[i_y][i_x] = number0 + number1
print(mas_key_hex)

result_mas = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for i_x in range(4):
    for i_y in range(4):
        number_text = mas_crypto_hex[i_y][i_x]
        number_key = mas_key_hex[i_y][i_x]
        number_result = ''
        for i in range(len(number_key)):

            if (int(number_text[i]) + int(number_key[i]) == 2):
                number_result += '0'
            else:
                prom = int(number_text[i]) + int(number_key[i])
                number_result += str(prom)
        result_mas[i_y][i_x] = number_result
print(result_mas, "0000000000000000000")


S_BOX = {'00':'63', '01':'7c', '02':'77', '03':'7b', '04':'f2', '05':'6b', '06':'6f', '07':'c5', '08':'30', '09':'01', '0a':'67', '0b':'2b',
         '0c':'fe', '0d':'d7', '0e':'ab', '0f':'76', '10':'ca', '11':'82', '12':'c9', '13':'7d', '14':'fa', '15':'59', '16':'47', '17':'f0',
         '18':'ad', '19':'d4', '1a':'a2', '1b':'af', '1c':'9c', '1d':'a4', '1e':'72', '1f':'c0', '20':'b7', '21':'fd', '22':'93', '23':'26',
         '24':'36', '25':'3f', '26':'f7', '27':'cc', '28':'34', '29':'a5', '2a':'e5', '2b':'f1', '2c':'71', '2d':'d8', '2e':'31', '2f':'15',
         '30':'04', '31':'c7', '32':'23', '33':'c3', '34':'18', '35':'96', '36':'05', '37':'9a', '38':'07', '39':'12', '3a':'80', '3b':'e2',
         '3c':'eb', '3d':'27', '3e':'b2', '3f':'75', '40':'09', '41':'83', '42':'2c', '43':'1a', '44':'1b', '45':'6e', '46':'5a', '47':'a0',
         '48':'52', '49':'3b', '4a':'d6', '4b':'b3', '4c':'29', '4d':'e3', '4e':'2f', '4f':'84', '50':'53', '51':'d1', '52':'00', '53':'ed',
         '54':'20', '55':'fc', '56':'b1', '57':'5b', '58':'6a', '59':'cb', '5a':'be', '5b':'39', '5c':'4a', '5d':'4c', '5e':'58', '5f':'cf',
         '60':'d0', '61':'ef', '62':'aa', '63':'fb', '64':'43', '65':'4d', '66':'33', '67':'85', '68':'45', '69':'f9', '6a':'02', '6b':'7f',
         '6c':'50', '6d':'3c', '6e':'9f', '6f':'a8', '70':'51', '71':'a3', '72':'40', '73':'8f', '74':'92', '75':'9d', '76':'38', '77':'f5',
         '78':'bc', '79':'b6', '7a':'da', '7b':'21', '7c':'10', '7d':'ff', '7e':'f3', '7f':'d2', '80':'cd', '81':'0c', '82':'13', '83':'ec',
         '84':'5f', '85':'97', '86':'44', '87':'17', '88':'c4', '89':'a7', '8a':'7e', '8b':'3d', '8c':'64', '8d':'5d', '8e':'19', '8f':'73',
         '90':'60', '91':'81', '92':'4f', '93':'dc', '94':'22', '95':'2a', '96':'90', '97':'88', '98':'46', '99':'ee', '9a':'b8', '9b':'14',
         '9c':'de', '9d':'5e', '9e':'0b', '9f':'db', 'a0':'e0', 'a1':'32', 'a2':'3a', 'a3':'0a', 'a4':'49', 'a5':'06', 'a6':'24', 'a7':'5c',
         'a8':'c2', 'a9':'d3', 'aa':'ac', 'ab':'62', 'ac':'91', 'ad':'95', 'ae':'e4', 'af':'79', 'b0':'e7', 'b1':'c8', 'b2':'37', 'b3':'6d',
         'b4':'8d', 'b5':'d5', 'b6':'4e', 'b7':'a9', 'b8':'6c', 'b9':'56', 'ba':'f4', 'bb':'ea', 'bc':'65', 'bd':'7a', 'be':'ae', 'bf':'08',
         'c0':'ba', 'c1':'78', 'c2':'25', 'c3':'2e', 'c4':'1c', 'c5':'a6', 'c6':'b4', 'c7':'c6', 'c8':'e8', 'c9':'dd', 'ca':'74', 'cb':'1f',
         'cc':'4b', 'cd':'bd', 'ce':'8b', 'cf':'8a', 'd0':'70', 'd1':'3e', 'd2':'b5', 'd3':'66', 'd4':'48', 'd5':'03', 'd6':'f6', 'd7':'0e',
         'd8':'61', 'd9':'35', 'da':'57', 'db':'b9', 'dc':'86', 'dd':'c1', 'de':'1d', 'df':'9e', 'e0':'e1', 'e1':'f8', 'e2':'98', 'e3':'11',
         'e4':'69', 'e5':'d9', 'e6':'8e', 'e7':'94', 'e8':'9b', 'e9':'1e', 'ea':'87', 'eb':'e9', 'ec':'ce', 'ed':'55', 'ee':'28', 'ef':'df',
         'f0':'8c', 'f1':'a1', 'f2':'89', 'f3':'0d', 'f4':'bf', 'f5':'e6', 'f6':'42', 'f7':'68', 'f8':'41', 'f9':'99', 'fa':'2d', 'fb':'0f',
         'fc':'b0', 'fd':'54', 'fe':'bb', 'ff':'16'}

slov1 = { '0000':'0', '0001':'1', '0010':'2', '0011':'3', '0100':'4', '0101':'5', '0110':'6', '0111':'7', '1000':'8',
        '1001':'9', '1010':'a', '1011':'b', '1100':'c', '1101':'d', '1110':'e', '1111':'f', }


crypted_mas = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for i_x in range(4):
    for i_y in range(4):
        number0 = result_mas[i_y][i_x][:4]
        number1 = result_mas[i_y][i_x][4:]
        number0 = slov1.get(number0)
        number1 = slov1.get(number1)
        crypted_mas[i_y][i_x] = number0 + number1
print("aaaaaaaaaaaaaaaaaaaaaaa ", crypted_mas)




''' w0 = mas_key_hex[0][0] + mas_key_hex[0][1] + mas_key_hex[0][2] + mas_key_hex[0][3]
    w1 = mas_key_hex[1][0] + mas_key_hex[1][1] + mas_key_hex[1][2] + mas_key_hex[1][3]
    w2 = mas_key_hex[2][0] + mas_key_hex[2][1] + mas_key_hex[2][2] + mas_key_hex[2][3]
    w3 = mas_key_hex[3][0] + mas_key_hex[3][1] + mas_key_hex[3][2] + mas_key_hex[3][3]'''
#print("111111111111111111111111111")
#print(mas_key_hex)
#коли буду робити не для вправи з книжки, треба буде перекинути з бітового в словник slov

div = ['01', '02', '04', '08', '10', '20', '40', '80', '1b', '36']

def mul_by_02(num):
    res = slov.get(num[0]) + slov.get(num[1])

    if (res[0] == '0'):
        z_02 = res[1:8] + '0'
    else:
        res = res[1:8] + '0'
        one_b = '00011011'
        z_02 = ''
        for i in range(len(one_b)):
            if int(res[i]) + int(one_b[i]) == 2:
                z_02 += '0'
            elif int(res[i]) + int(one_b[i]) == 1:
                z_02 += '1'
            else:
                z_02 += '0'


    return z_02

def mul_by_03(num):

    res1 = slov.get(num[0]) + slov.get(num[1])

    if (res1[0] == '0'):
        z = res1[1:8] + '0'
    else:
        res1 = res1[1:8] + '0'
        one_b = '00011011'
        z = ''
        for i in range(len(one_b)):
            if int(res1[i]) + int(one_b[i]) == 2:
                z += '0'
            elif int(res1[i]) + int(one_b[i]) == 1:
                z += '1'
            else:
                z += '0'

    res2 = slov.get(num[0]) + slov.get(num[1])
    z3 = ''
    for i in range(len(res2)):
        if int(z[i]) + int(res2[i]) == 2:
            z3 += '0'
        elif int(z[i]) + int(res2[i]) == 1:
            z3 += '1'
        else:
            z3 += '0'
    return z3


mas_mas = ['', '', '', '', '', '', '', '', '', '']
for i in range(10):
    #subbytes
    #1
    round_mas = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i_x in range(4):
        for i_y in range(4):
            number0 = crypted_mas[i_y][i_x]
            number0 = S_BOX.get(number0)
            round_mas[i_y][i_x] = number0
    #shiftrows
    #2
    pivot = round_mas[1][3]
    round_mas[1][3] = round_mas[1][0]
    pivot2 = round_mas[1][2]
    round_mas[1][2] = pivot
    pivot3 = round_mas[1][1]
    round_mas[1][1] = pivot2
    round_mas[1][0] = pivot3



    pivot = round_mas[2][2]
    round_mas[2][2] = round_mas[2][0]
    round_mas[2][0] = pivot
    pivot2 = round_mas[2][1]
    round_mas[2][1] = round_mas[2][3]
    round_mas[2][3] = pivot2


    pivot = round_mas[3][1]
    round_mas[3][1] = round_mas[3][0]
    round_mas[3][0] = round_mas[3][3]
    round_mas[3][3] = round_mas[3][2]
    round_mas[3][2] = pivot










    #MIXcolumns
    #3
    if (i != 9):
        for i_mix in range(4):
            '''
            s0 = mul_by_02(round_mas[0][i]) ^ mul_by_03(round_mas[1][i]) ^ round_mas[2][i] ^ round_mas[3][i]
            s1 = round_mas[0][i] ^ mul_by_02(round_mas[1][i]) ^ mul_by_03(round_mas[2][i]) ^ round_mas[3][i]
            s2 = round_mas[0][i] ^ round_mas[1][i] ^ mul_by_02(state[2][i]) ^ mul_by_03(round_mas[3][i])
            s3 = mul_by_03(round_mas[0][i]) ^ round_mas[1][i] ^ round_mas[2][i] ^ mul_by_02(round_mas[3][i])
            '''
            #s0

            str_0_1 =  mul_by_02(round_mas[0][i_mix])
            str_0_2 = mul_by_03(round_mas[1][i_mix])
            str_0_3 = slov.get(round_mas[2][i_mix][0]) + slov.get(round_mas[2][i_mix][1])
            str_0_4 = slov.get(round_mas[3][i_mix][0]) + slov.get(round_mas[3][i_mix][1])
            z_0_1 = ''
            for i_0_1 in range(len(str_0_1)):
                if int(str_0_1[i_0_1]) + int(str_0_2[i_0_1]) == 2:
                    z_0_1 += '0'
                elif int(str_0_1[i_0_1]) + int(str_0_2[i_0_1]) == 1:
                    z_0_1 += '1'
                else:
                    z_0_1 += '0'

            z_0_2 = ''
            for i_0_2 in range(len(str_0_3)):
                if int(str_0_3[i_0_2]) + int(str_0_4[i_0_2]) == 2:
                    z_0_2 += '0'
                elif int(str_0_3[i_0_2]) + int(str_0_4[i_0_2]) == 1:
                    z_0_2 += '1'
                else:
                    z_0_2 += '0'

            z_0_3 = ''
            for i_0_3 in range(len(z_0_2)):
                if int(z_0_1[i_0_3]) + int(z_0_2[i_0_3]) == 2:
                    z_0_3 += '0'
                elif int(z_0_1[i_0_3]) + int(z_0_2[i_0_3]) == 1:
                    z_0_3 += '1'
                else:
                    z_0_3 += '0'

            #s1

            str_1_1 = slov.get(round_mas[0][i_mix][0]) + slov.get(round_mas[0][i_mix][1])
            str_1_2 = mul_by_02(round_mas[1][i_mix])
            str_1_3 = mul_by_03(round_mas[2][i_mix])
            str_1_4 = slov.get(round_mas[3][i_mix][0]) + slov.get(round_mas[3][i_mix][1])

            z_1_1 = ''
            for i_1_1 in range(len(str_1_1)):
                if int(str_1_1[i_1_1]) + int(str_1_2[i_1_1]) == 2:
                    z_1_1 += '0'
                elif int(str_1_1[i_1_1]) + int(str_1_2[i_1_1]) == 1:
                    z_1_1 += '1'
                else:
                    z_1_1 += '0'
            z_1_2 = ''
            for i_1_2 in range(len(str_1_3)):
                if int(str_1_3[i_1_2]) + int(str_1_4[i_1_2]) == 2:
                    z_1_2 += '0'
                elif int(str_1_3[i_1_2]) + int(str_1_4[i_1_2]) == 1:
                    z_1_2 += '1'
                else:
                    z_1_2 += '0'

            z_1_3 = ''
            for i_1_3 in range(len(z_1_2)):
                if int(z_1_1[i_1_3]) + int(z_1_2[i_1_3]) == 2:
                    z_1_3 += '0'
                elif int(z_1_1[i_1_3]) + int(z_1_2[i_1_3]) == 1:
                    z_1_3 += '1'
                else:
                    z_1_3 += '0'


            #s2
            str_2_1 = slov.get(round_mas[0][i_mix][0]) + slov.get(round_mas[0][i_mix][1])
            str_2_2 = slov.get(round_mas[1][i_mix][0]) + slov.get(round_mas[1][i_mix][1])
            str_2_3 = mul_by_02(round_mas[2][i_mix])
            str_2_4 = mul_by_03(round_mas[3][i_mix])
            z_2_1 = ''
            for i_2_1 in range(len(str_2_1)):
                if int(str_2_1[i_2_1]) + int(str_2_2[i_2_1]) == 2:
                    z_2_1 += '0'
                elif int(str_2_1[i_2_1]) + int(str_2_2[i_2_1]) == 1:
                    z_2_1 += '1'
                else:
                    z_2_1 += '0'

            z_2_2 = ''
            for i_2_2 in range(len(str_2_3)):
                if int(str_2_3[i_2_2]) + int(str_2_4[i_2_2]) == 2:
                    z_2_2 += '0'
                elif int(str_2_3[i_2_2]) + int(str_2_4[i_2_2]) == 1:
                    z_2_2 += '1'
                else:
                    z_2_2 += '0'

            z_2_3 = ''
            for i_2_3 in range(len(z_2_2)):
                if int(z_2_1[i_2_3]) + int(z_2_2[i_2_3]) == 2:
                    z_2_3 += '0'
                elif int(z_2_1[i_2_3]) + int(z_2_2[i_2_3]) == 1:
                    z_2_3 += '1'
                else:
                    z_2_3 += '0'



            # s3
            str_3_1 = mul_by_03(round_mas[0][i_mix])
            str_3_2 = slov.get(round_mas[1][i_mix][0]) + slov.get(round_mas[1][i_mix][1])
            str_3_3 = slov.get(round_mas[2][i_mix][0]) + slov.get(round_mas[2][i_mix][1])
            str_3_4 = mul_by_02(round_mas[3][i_mix])
            z_3_1 = ''
            for i_3_1 in range(len(str_3_1)):
                if int(str_3_1[i_3_1]) + int(str_3_2[i_3_1]) == 2:
                    z_3_1 += '0'
                elif int(str_3_1[i_3_1]) + int(str_3_2[i_3_1]) == 1:
                    z_3_1 += '1'
                else:
                    z_3_1 += '0'

            z_3_2 = ''
            for i_3_2 in range(len(str_3_3)):
                if int(str_3_3[i_3_2]) + int(str_3_4[i_3_2]) == 2:
                    z_3_2 += '0'
                elif int(str_3_3[i_3_2]) + int(str_3_4[i_3_2]) == 1:
                    z_3_2 += '1'
                else:
                    z_3_2 += '0'

            z_3_3 = ''
            for i_3_3 in range(len(z_3_2)):
                if int(z_3_1[i_3_3]) + int(z_3_2[i_3_3]) == 2:
                    z_3_3 += '0'
                elif int(z_3_1[i_3_3]) + int(z_3_2[i_3_3]) == 1:
                    z_3_3 += '1'
                else:
                    z_3_3 += '0'


            round_mas[0][i_mix] = slov1.get(z_0_3[:4]) + slov1.get(z_0_3[4:])
            round_mas[1][i_mix] = slov1.get(z_1_3[:4]) + slov1.get(z_1_3[4:])
            round_mas[2][i_mix] = slov1.get(z_2_3[:4]) + slov1.get(z_2_3[4:])
            round_mas[3][i_mix] = slov1.get(z_3_3[:4]) + slov1.get(z_3_3[4:])

























    #XORRoundKey
    #4
    w0 = ''
    print(mas_key_hex)
    print("zzzzzzzzzzzz ", mas_key_hex[0][0][:4])
    w0 = slov1.get(mas_key_hex[0][0][:4]) + slov1.get(mas_key_hex[0][0][4:]) + slov1.get(mas_key_hex[1][0][:4]) + slov1.get(mas_key_hex[1][0][4:]) + slov1.get(mas_key_hex[2][0][:4]) + slov1.get(mas_key_hex[2][0][4:]) + slov1.get(mas_key_hex[3][0][:4]) + slov1.get(mas_key_hex[3][0][4:])
    print("rrrrrrrrrrr ", w0)

    w1 = slov1.get(mas_key_hex[0][1][:4]) + slov1.get(mas_key_hex[0][1][4:]) + slov1.get(mas_key_hex[1][1][:4]) + slov1.get(mas_key_hex[1][1][4:]) + slov1.get(mas_key_hex[2][1][:4]) + slov1.get(mas_key_hex[2][1][4:]) + slov1.get(mas_key_hex[3][1][:4]) + slov1.get(mas_key_hex[3][1][4:])
    w2 = slov1.get(mas_key_hex[0][2][:4]) + slov1.get(mas_key_hex[0][2][4:]) + slov1.get(mas_key_hex[1][2][:4]) + slov1.get(mas_key_hex[1][2][4:]) + slov1.get(mas_key_hex[2][2][:4]) + slov1.get(mas_key_hex[2][2][4:]) + slov1.get(mas_key_hex[3][2][:4]) + slov1.get(mas_key_hex[3][2][4:])
    w3 = slov1.get(mas_key_hex[0][3][:4]) + slov1.get(mas_key_hex[0][3][4:]) + slov1.get(mas_key_hex[1][3][:4]) + slov1.get(mas_key_hex[1][3][4:]) + slov1.get(mas_key_hex[2][3][:4]) + slov1.get(mas_key_hex[2][3][4:]) + slov1.get(mas_key_hex[3][3][:4]) + slov1.get(mas_key_hex[3][3][4:])



    #раундова функція
    #RotWord(w3)

    slov = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000',
            '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111', }

    slov1 = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8',
             '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f', }

    w3 = w3[2:8] + w3[:2]


    w3 = S_BOX.get(w3[:2]) + S_BOX.get(w3[2:4]) + S_BOX.get(w3[4:6]) + S_BOX.get(w3[6:8])
    gfg = slov.get(w3[:2][0]) + slov.get(w3[:2][1])
    gfg1 = slov.get(div[i][0]) + slov.get(div[i][1])
    z = ''
    for i_gfg in range(len(gfg)):
        if int(gfg[i_gfg]) + int(gfg1[i_gfg]) == 2:
            z += '0'
        elif int(gfg[i_gfg]) + int(gfg1[i_gfg]) == 1:
            z += '1'
        else:
            z += '0'
    z = slov1.get(z[:4]) + slov1.get(z[4:])
    w3 = z + w3[2:8]

    w0 = mas_key_hex[0][0] + mas_key_hex[1][0] + mas_key_hex[2][0] + mas_key_hex[3][0]
    w3_new = slov.get(w3[0]) + slov.get(w3[1]) + slov.get(w3[2]) + slov.get(w3[3]) + slov.get(w3[4]) + slov.get(w3[5]) + slov.get(w3[6]) + slov.get(w3[7])
    z = ''
    for i_w3 in range(len(w0)):
        if int(w0[i_w3]) + int(w3_new[i_w3]) == 2:
            z += '0'
        elif int(w0[i_w3]) + int(w3_new[i_w3]) == 1:
            z += '1'
        else:
            z += '0'
    #z = slov1.get(z[:4]) + slov1.get(z[4:8]) + slov1.get(z[8:12]) + slov1.get(z[12:16]) + slov1.get(z[16:20]) + slov1.get(z[20:24]) + slov1.get(z[24:28]) + slov1.get(z[28:32])
    new_key =[['', '', '', ''],
              ['', '', '', ''],
              ['', '', '', ''],
              ['', '', '', '']]
    new_key[0][0] = z[:8]
    new_key[1][0] = z[8:16]
    new_key[2][0] = z[16:24]
    new_key[3][0] = z[24:32]



    w1 = mas_key_hex[0][1] + mas_key_hex[1][1] + mas_key_hex[2][1] + mas_key_hex[3][1]
    z1 = ''
    for i_w1 in range(len(w1)):
        if int(w1[i_w1]) + int(z[i_w1]) == 2:
            z1 += '0'
        elif int(w1[i_w1]) + int(z[i_w1]) == 1:
            z1 += '1'
        else:
            z1 += '0'
    # z1 = slov1.get(z1[:4]) + slov1.get(z1[4:8]) + slov1.get(z1[8:12]) + slov1.get(z1[12:16]) + slov1.get(z1[16:20]) + slov1.get(z1[20:24]) + slov1.get(z1[24:28]) + slov1.get(z1[28:32])
    new_key[0][1] = z1[:8]
    new_key[1][1] = z1[8:16]
    new_key[2][1] = z1[16:24]
    new_key[3][1] = z1[24:32]



    w2 = mas_key_hex[0][2] + mas_key_hex[1][2] + mas_key_hex[2][2] + mas_key_hex[3][2]
    z2 = ''
    for i_w2 in range(len(w2)):
        if int(w2[i_w2]) + int(z1[i_w2]) == 2:
            z2 += '0'
        elif int(w2[i_w2]) + int(z1[i_w2]) == 1:
            z2 += '1'
        else:
            z2 += '0'
    #z2 = slov1.get(z2[:4]) + slov1.get(z2[4:8]) + slov1.get(z2[8:12]) + slov1.get(z2[12:16]) + slov1.get(z2[16:20]) + slov1.get(z2[20:24]) + slov1.get(z2[24:28]) + slov1.get(z2[28:32])
    new_key[0][2] = z2[:8]
    new_key[1][2] = z2[8:16]
    new_key[2][2] = z2[16:24]
    new_key[3][2] = z2[24:32]


    w3 = mas_key_hex[0][3] + mas_key_hex[1][3] + mas_key_hex[2][3] + mas_key_hex[3][3]
    z3 = ''
    for i_w3 in range(len(w3)):
        if int(w3[i_w3]) + int(z2[i_w3]) == 2:
            z3 += '0'
        elif int(w3[i_w3]) + int(z2[i_w3]) == 1:
            z3 += '1'
        else:
            z3 += '0'
    #z3 = slov1.get(z3[:4]) + slov1.get(z3[4:8]) + slov1.get(z3[8:12]) + slov1.get(z3[12:16]) + slov1.get(z3[16:20]) + slov1.get(z3[20:24]) + slov1.get(z3[24:28]) + slov1.get(z3[28:32])
    new_key[0][3] = z3[:8]
    new_key[1][3] = z3[8:16]
    new_key[2][3] = z3[16:24]
    new_key[3][3] = z3[24:32]
    mas_key_hex = new_key

    print(round_mas)
    for i_new in range(4):
        for i_new_new in range(4):
            round_mas[i_new][i_new_new] = slov.get(round_mas[i_new][i_new_new][0]) + slov.get(round_mas[i_new][i_new_new][1])
    print(round_mas)



    mas_mas[9 - i] = mas_key_hex





    for i_new in range(4):
        for i_new_new in range(4):
            #mas_key_hex i round mas
            str1 = mas_key_hex[i_new][i_new_new]
            str2 = round_mas[i_new][i_new_new]
            x = ''
            for i_str1 in range(len(str1)):
                if int(str1[i_str1]) + int(str2[i_str1]) == 2:
                    x += '0'
                elif int(str1[i_str1]) + int(str2[i_str1]) == 1:
                    x += '1'
                else:
                    x += '0'
            round_mas[i_new][i_new_new] = slov1.get(x[:4]) + slov1.get(x[4:])
    crypted_mas = round_mas
print("crypted text = ", crypted_mas)




def mul_by_09(num):
    res1 = slov.get(num[0]) + slov.get(num[1])
    num = slov1.get(mul_by_02(num)[:4]) + slov1.get(mul_by_02(num)[4:])
    num = slov1.get(mul_by_02(num)[:4]) + slov1.get(mul_by_02(num)[4:])
    num = mul_by_02(num)

    z_02 = ''
    for i in range(len(num)):
        if int(num[i]) + int(res1[i]) == 2:
            z_02 += '0'
        elif int(num[i]) + int(res1[i]) == 1:
            z_02 += '1'
        else:
            z_02 += '0'

    return z_02



def mul_by_0b(num):
    res1 = mul_by_02(num)
    num = mul_by_09(num)
    z_02 = ''
    for i in range(len(num)):
        if int(num[i]) + int(res1[i]) == 2:
            z_02 += '0'
        elif int(num[i]) + int(res1[i]) == 1:
            z_02 += '1'
        else:
            z_02 += '0'

    return z_02

def mul_by_0d(num):
    res1 = slov1.get(mul_by_02(num)[:4]) + slov1.get(mul_by_02(num)[4:])
    res1 = mul_by_02(res1)
    num = mul_by_09(num)

    z_02 = ''
    for i in range(len(num)):
        if int(num[i]) + int(res1[i]) == 2:
            z_02 += '0'
        elif int(num[i]) + int(res1[i]) == 1:
            z_02 += '1'
        else:
            z_02 += '0'

    return z_02


def mul_by_0e(num):
    res1 = mul_by_03(num)
    num = mul_by_0d(num)


    z_02 = ''
    for i in range(len(num)):
        if int(num[i]) + int(res1[i]) == 2:
            z_02 += '0'
        elif int(num[i]) + int(res1[i]) == 1:
            z_02 += '1'
        else:
            z_02 += '0'

    return z_02



inverse_S_B0X = \
    {'63':'00', '7c':'01', '77':'02', '7b':'03', 'f2':'04', '6b':'05', '6f':'06', 'c5':'07', '30':'08', '01':'09', '67':'0a', '2b':'0b',
     'fe':'0c', 'd7':'0d', 'ab':'0e', '76':'0f', 'ca':'10', '82':'11', 'c9':'12', '7d':'13', 'fa':'14', '59':'15', '47':'16', 'f0':'17',
     'ad':'18', 'd4':'19', 'a2':'1a', 'af':'1b', '9c':'1c', 'a4':'1d', '72':'1e', 'c0':'1f', 'b7':'20', 'fd':'21', '93':'22', '26':'23',
     '36':'24', '3f':'25', 'f7':'26', 'cc':'27', '34':'28', 'a5':'29', 'e5':'2a', 'f1':'2b', '71':'2c', 'd8':'2d', '31':'2e', '15':'2f',
     '04':'30', 'c7':'31', '23':'32', 'c3':'33', '18':'34', '96':'35', '05':'36', '9a':'37', '07':'38', '12':'39', '80':'3a', 'e2':'3b',
     'eb':'3c', '27':'3d', 'b2':'3e', '75':'3f', '09':'40', '83':'41', '2c':'42', '1a':'43', '1b':'44', '6e':'45', '5a':'46', 'a0':'47',
     '52':'48', '3b':'49', 'd6':'4a', 'b3':'4b', '29':'4c', 'e3':'4d', '2f':'4e', '84':'4f', '53':'50', 'd1':'51', '00':'52', 'ed':'53',
     '20':'54', 'fc':'55', 'b1':'56', '5b':'57', '6a':'58', 'cb':'59', 'be':'5a', '39':'5b', '4a':'5c', '4c':'5d', '58':'5e', 'cf':'5f',
     'd0':'60', 'ef':'61', 'aa':'62', 'fb':'63', '43':'64', '4d':'65', '33':'66', '85':'67', '45':'68', 'f9':'69', '02':'6a', '7f':'6b',
     '50':'6c', '3c':'6d', '9f':'6e', 'a8':'6f', '51':'70', 'a3':'71', '40':'72', '8f':'73', '92':'74', '9d':'75', '38':'76', 'f5':'77',
     'bc':'78', 'b6':'79', 'da':'7a', '21':'7b', '10':'7c', 'ff':'7d', 'f3':'7e', 'd2':'7f', 'cd':'80', '0c':'81', '13':'82', 'ec':'83',
     '5f':'84', '97':'85', '44':'86', '17':'87', 'c4':'88', 'a7':'89', '7e':'8a', '3d':'8b', '64':'8c', '5d':'8d', '19':'8e', '73':'8f',
     '60':'90', '81':'91', '4f':'92', 'dc':'93', '22':'94', '2a':'95', '90':'96', '88':'97', '46':'98', 'ee':'99', 'b8':'9a', '14':'9b',
     'de':'9c', '5e':'9d', '0b':'9e', 'db':'9f', 'e0':'a0', '32':'a1', '3a':'a2', '0a':'a3', '49':'a4', '06':'a5', '24':'a6', '5c':'a7',
     'c2':'a8', 'd3':'a9', 'ac':'aa', '62':'ab', '91':'ac', '95':'ad', 'e4':'ae', '79':'af', 'e7':'b0', 'c8':'b1', '37':'b2', '6d':'b3',
     '8d':'b4', 'd5':'b5', '4e':'b6', 'a9':'b7', '6c':'b8', '56':'b9', 'f4':'ba', 'ea':'bb', '65':'bc', '7a':'bd', 'ae':'be', '08':'bf',
     'ba':'c0', '78':'c1', '25':'c2', '2e':'c3', '1c':'c4', 'a6':'c5', 'b4':'c6', 'c6':'c7', 'e8':'c8', 'dd':'c9', '74':'ca', '1f':'cb',
     '4b':'cc', 'bd':'cd', '8b':'ce', '8a':'cf', '70':'d0', '3e':'d1', 'b5':'d2', '66':'d3', '48':'d4', '03':'d5', 'f6':'d6', '0e':'d7',
     '61':'d8', '35':'d9', '57':'da', 'b9':'db', '86':'dc', 'c1':'dd', '1d':'de', '9e':'df', 'e1':'e0', 'f8':'e1', '98':'e2', '11':'e3',
     '69':'e4', 'd9':'e5', '8e':'e6', '94':'e7', '9b':'e8', '1e':'e9', '87':'ea', 'e9':'eb', 'ce':'ec', '55':'ed', '28':'ee', 'df':'ef',
     '8c':'f0', 'a1':'f1', '89':'f2', '0d':'f3', 'bf':'f4', 'e6':'f5', '42':'f6', '68':'f7', '41':'f8', '99':'f9', '2d':'fa', '0f':'fb',
     'b0':'fc', '54':'fd', 'bb':'fe', '16':'ff'}


'''for i in range(10):
    for i_c in range(4):
        for t in range(4):
            mas_key_hex[i_c][t] = slov1.get(mas_key_hex[i_c][t][:4]) + slov1.get(mas_key_hex[i_c][t][4:])

    mas_mas[i] = mas_key_hex


    for i_v in range(4):
        for t in range(4):
            mas_key_hex[i_v][t] = slov.get(mas_key_hex[i_v][t][0]) + slov.get(mas_key_hex[i_v][t][1])'''



for i in range(10):
    #4
    # XORroundkey
    for i_new in range(4):
        for i_new_new in range(4):
            crypted_mas[i_new][i_new_new] = slov.get(crypted_mas[i_new][i_new_new][0]) + slov.get(crypted_mas[i_new][i_new_new][1])

    for i_new in range(4):
        for i_new_new in range(4):
            str1 = mas_mas[i][i_new][i_new_new]
            str2 = crypted_mas[i_new][i_new_new]
            x = ''
            for i_str1 in range(len(str1)):
                if int(str1[i_str1]) + int(str2[i_str1]) == 2:
                    x += '0'
                elif int(str1[i_str1]) + int(str2[i_str1]) == 1:
                    x += '1'
                else:
                    x += '0'
            crypted_mas[i_new][i_new_new] = slov1.get(x[:4]) + slov1.get(x[4:])
    round_mas = crypted_mas

    #3
    #InverseMixColums
    if (i != 0):
        for i_mix in range(4):
            '''    
                   
                   s0 = mul_by_0e(state[0][i]) ^ mul_by_0b(state[1][i]) ^ mul_by_0d(state[2][i]) ^ mul_by_09(state[3][i])
                   s1 = mul_by_09(state[0][i]) ^ mul_by_0e(state[1][i]) ^ mul_by_0b(state[2][i]) ^ mul_by_0d(state[3][i])
                   s2 = mul_by_0d(state[0][i]) ^ mul_by_09(state[1][i]) ^ mul_by_0e(state[2][i]) ^ mul_by_0b(state[3][i])
                   s3 = mul_by_0b(state[0][i]) ^ mul_by_0d(state[1][i]) ^ mul_by_09(state[2][i]) ^ mul_by_0e(state[3][i])
                   
                   state[0][i] = s0
                   state[1][i] = s1
                   state[2][i] = s2
                   state[3][i] = s3
                   
               '''

            # s0

            str_0_1 = mul_by_0e(round_mas[0][i_mix])
            str_0_2 = mul_by_0b(round_mas[1][i_mix])
            str_0_3 = mul_by_0d(round_mas[2][i_mix])
            str_0_4 = mul_by_09(round_mas[3][i_mix])
            z_0_1 = ''
            for i_0_1 in range(len(str_0_1)):
                if int(str_0_1[i_0_1]) + int(str_0_2[i_0_1]) == 2:
                    z_0_1 += '0'
                elif int(str_0_1[i_0_1]) + int(str_0_2[i_0_1]) == 1:
                    z_0_1 += '1'
                else:
                    z_0_1 += '0'

            z_0_2 = ''
            for i_0_2 in range(len(str_0_3)):
                if int(str_0_3[i_0_2]) + int(str_0_4[i_0_2]) == 2:
                    z_0_2 += '0'
                elif int(str_0_3[i_0_2]) + int(str_0_4[i_0_2]) == 1:
                    z_0_2 += '1'
                else:
                    z_0_2 += '0'

            z_0_3 = ''
            for i_0_3 in range(len(z_0_2)):
                if int(z_0_1[i_0_3]) + int(z_0_2[i_0_3]) == 2:
                    z_0_3 += '0'
                elif int(z_0_1[i_0_3]) + int(z_0_2[i_0_3]) == 1:
                    z_0_3 += '1'
                else:
                    z_0_3 += '0'

            # s1

            str_1_1 = mul_by_09(round_mas[0][i_mix])
            str_1_2 = mul_by_0e(round_mas[1][i_mix])
            str_1_3 = mul_by_0b(round_mas[2][i_mix])
            str_1_4 = mul_by_0d(round_mas[3][i_mix])

            z_1_1 = ''
            for i_1_1 in range(len(str_1_1)):
                if int(str_1_1[i_1_1]) + int(str_1_2[i_1_1]) == 2:
                    z_1_1 += '0'
                elif int(str_1_1[i_1_1]) + int(str_1_2[i_1_1]) == 1:
                    z_1_1 += '1'
                else:
                    z_1_1 += '0'
            z_1_2 = ''
            for i_1_2 in range(len(str_1_3)):
                if int(str_1_3[i_1_2]) + int(str_1_4[i_1_2]) == 2:
                    z_1_2 += '0'
                elif int(str_1_3[i_1_2]) + int(str_1_4[i_1_2]) == 1:
                    z_1_2 += '1'
                else:
                    z_1_2 += '0'

            z_1_3 = ''
            for i_1_3 in range(len(z_1_2)):
                if int(z_1_1[i_1_3]) + int(z_1_2[i_1_3]) == 2:
                    z_1_3 += '0'
                elif int(z_1_1[i_1_3]) + int(z_1_2[i_1_3]) == 1:
                    z_1_3 += '1'
                else:
                    z_1_3 += '0'

            # s2
            str_2_1 = mul_by_0d(round_mas[0][i_mix])
            str_2_2 = mul_by_09(round_mas[1][i_mix])
            str_2_3 = mul_by_0e(round_mas[2][i_mix])
            str_2_4 = mul_by_0b(round_mas[3][i_mix])
            z_2_1 = ''
            for i_2_1 in range(len(str_2_1)):
                if int(str_2_1[i_2_1]) + int(str_2_2[i_2_1]) == 2:
                    z_2_1 += '0'
                elif int(str_2_1[i_2_1]) + int(str_2_2[i_2_1]) == 1:
                    z_2_1 += '1'
                else:
                    z_2_1 += '0'

            z_2_2 = ''
            for i_2_2 in range(len(str_2_3)):
                if int(str_2_3[i_2_2]) + int(str_2_4[i_2_2]) == 2:
                    z_2_2 += '0'
                elif int(str_2_3[i_2_2]) + int(str_2_4[i_2_2]) == 1:
                    z_2_2 += '1'
                else:
                    z_2_2 += '0'

            z_2_3 = ''
            for i_2_3 in range(len(z_2_2)):
                if int(z_2_1[i_2_3]) + int(z_2_2[i_2_3]) == 2:
                    z_2_3 += '0'
                elif int(z_2_1[i_2_3]) + int(z_2_2[i_2_3]) == 1:
                    z_2_3 += '1'
                else:
                    z_2_3 += '0'

            # s3
            str_3_1 = mul_by_0b(round_mas[0][i_mix])
            str_3_2 = mul_by_0d(round_mas[1][i_mix])
            str_3_3 = mul_by_09(round_mas[2][i_mix])
            str_3_4 = mul_by_0e(round_mas[3][i_mix])
            z_3_1 = ''
            for i_3_1 in range(len(str_3_1)):
                if int(str_3_1[i_3_1]) + int(str_3_2[i_3_1]) == 2:
                    z_3_1 += '0'
                elif int(str_3_1[i_3_1]) + int(str_3_2[i_3_1]) == 1:
                    z_3_1 += '1'
                else:
                    z_3_1 += '0'

            z_3_2 = ''
            for i_3_2 in range(len(str_3_3)):
                if int(str_3_3[i_3_2]) + int(str_3_4[i_3_2]) == 2:
                    z_3_2 += '0'
                elif int(str_3_3[i_3_2]) + int(str_3_4[i_3_2]) == 1:
                    z_3_2 += '1'
                else:
                    z_3_2 += '0'

            z_3_3 = ''
            for i_3_3 in range(len(z_3_2)):
                if int(z_3_1[i_3_3]) + int(z_3_2[i_3_3]) == 2:
                    z_3_3 += '0'
                elif int(z_3_1[i_3_3]) + int(z_3_2[i_3_3]) == 1:
                    z_3_3 += '1'
                else:
                    z_3_3 += '0'

            round_mas[0][i_mix] = slov1.get(z_0_3[:4]) + slov1.get(z_0_3[4:])
            round_mas[1][i_mix] = slov1.get(z_1_3[:4]) + slov1.get(z_1_3[4:])
            round_mas[2][i_mix] = slov1.get(z_2_3[:4]) + slov1.get(z_2_3[4:])
            round_mas[3][i_mix] = slov1.get(z_3_3[:4]) + slov1.get(z_3_3[4:])

    #2
    #InverseShiftRows
    pivot = round_mas[1][1]
    round_mas[1][1] = round_mas[1][0]
    pivot2 = round_mas[1][2]
    round_mas[1][2] = pivot
    pivot3 = round_mas[1][3]
    round_mas[1][3] = pivot2
    round_mas[1][1] = pivot3

    pivot4 = round_mas[1][0]
    round_mas[1][0] = round_mas[1][1]
    round_mas[1][1] = pivot4




    pivot = round_mas[2][0]
    round_mas[2][0] = round_mas[2][2]
    pivot2 = round_mas[2][1]
    round_mas[2][1] = round_mas[2][3]
    round_mas[2][2] = pivot
    round_mas[2][3] = pivot2


    pivot = round_mas[3][0]
    round_mas[3][0] = round_mas[3][1]
    round_mas[3][1] = round_mas[3][2]
    round_mas[3][2] = round_mas[3][3]
    round_mas[3][3] = pivot



    #1
    #InverseS-Box




    for i_x in range(4):
        for i_y in range(4):
            round_mas[i_x][i_y] = inverse_S_B0X.get(round_mas[i_x][i_y])
    crypted_mas = round_mas




print(crypted_mas)
print(decrypted_key)

#decrypted_key
for i in range(4):
    for t in range(4):
        crypted_mas[i][t] = slov.get(crypted_mas[i][t][0]) + slov.get(crypted_mas[i][t][1])

for i in range(4):
    for t in range(4):
        decrypted_key[i][t] = slov.get(decrypted_key[i][t][0]) + slov.get(decrypted_key[i][t][1])


for p in range(4):
    for r in range(4):
        text = crypted_mas[r][p]
        key = decrypted_key[r][p]

        number_result = ''
        for i in range(len(key)):
            if int(text[i]) + int(key[i]) == 2:
                number_result += '0'
            elif int(text[i]) + int(key[i]) == 1:
                number_result += '1'
            else:
                number_result += '0'
        crypted_mas[r][p] = slov1.get(number_result[:4]) + slov1.get(number_result[4:])


print(crypted_mas)