import binascii
import random


sum = 0

for glob in range(1000):
    with open('Cryptedtext.txt', 'r', encoding='utf-8') as input_file:
        # зчитування вмісту файлу
        cryptotext = input_file.read()



    def str2hex(s):
        return binascii.hexlify(bytes(str.encode(s)))


    def hex2str(h):
        return binascii.unhexlify(h)


    cryptotext_hex = str2hex(cryptotext)
    cryptotext_hex = cryptotext_hex.decode('utf-8')


    unhexsring = hex2str(cryptotext_hex).decode('utf-8')

    m = 0
    mas_crypto_hex = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i_x in range(4):
        for i_y in range(4):
            string = cryptotext_hex[0 + m] + cryptotext_hex[1 + m]
            mas_crypto_hex[i_y][i_x] = string
            m += 2

    '''mas_crypto_hex = [['32', '88', '31', 'e0'],
                      ['43', '5a', '31', '37'],
                      ['f6', '30', '98', '07'],
                      ['a8', '8d', 'a2', '34']]

    '''
    mas_crypto_hex = [['00', '44', '88', 'cc'],
                      ['11', '55', '99', 'dd'],
                      ['22', '66', 'aa', 'ee'],
                      ['33', '77', 'bb', 'ff']]

    key = "I want to decryptfgfgfer"
    key_hex = str2hex(key)
    key_hex = key_hex.decode('utf-8')

    m = 0
    mas_key_hex = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    for i_x in range(4):
        for i_y in range(6):
            string = key_hex[0 + m] + key_hex[1 + m]
            mas_key_hex[i_x][i_y] = string
            m += 2

    '''

    mas_key_hex = [['00', '04', '08', '0c', '10', '14'],
                   ['01', '05', '09', '0d', '11', '15'],
                   ['02', '06', '0a', '0e', '12', '16'],
                   ['03', '07', '0b', '0f', '13', '17']]

    mas_key_hex = [['8e' ,'da' ,'c8' ,'80', '62', '52'],
                   ['73' ,'0e' ,'10' ,'90', 'f8', '2c'],
                   ['b0' ,'64' ,'f3' ,'79', 'ea', '6b'],
                   ['f7' ,'52' ,'2b' ,'e5', 'd2', '7b']]

    '''
    mas_key_hex = [['00', '04', '08', '0c', '10', '14'],
                   ['01', '05', '09', '0d', '11', '15'],
                   ['02', '06', '0a', '0e', '12', '16'],
                   ['03', '07', '0b', '0f', '13', '17']]

    decrypted_key = [['00', '04', '08', '0c', '10', '14'],
                     ['01', '05', '09', '0d', '11', '15'],
                     ['02', '06', '0a', '0e', '12', '16'],
                     ['03', '07', '0b', '0f', '13', '17']]

    buf_key_hex = [['', '', '', '', '', ''],
                   ['', '', '', '', '', ''],
                   ['', '', '', '', '', ''],
                   ['', '', '', '', '', '']]
    buf_key_hex = mas_key_hex

    mass_key_hex = [['', '', '', '', '', ''],
                    ['', '', '', '', '', ''],
                    ['', '', '', '', '', ''],
                    ['', '', '', '', '', '']]
    mass_key_hex = mas_key_hex

    slov = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
            '8': '1000',
            '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}

    for i_x in range(4):
        for i_y in range(4):
            number0 = mas_crypto_hex[i_y][i_x][0]
            number1 = mas_crypto_hex[i_y][i_x][1]
            number0 = slov.get(number0)
            number1 = slov.get(number1)
            mas_crypto_hex[i_y][i_x] = number0 + number1

    for i_y in range(4):
        for i_x in range(6):
            number0 = mas_key_hex[i_y][i_x][0]
            number1 = mas_key_hex[i_y][i_x][1]
            number0 = slov.get(number0)
            number1 = slov.get(number1)
            mas_key_hex[i_y][i_x] = number0 + number1

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

    S_BOX = {'00': '63', '01': '7c', '02': '77', '03': '7b', '04': 'f2', '05': '6b', '06': '6f', '07': 'c5', '08': '30',
             '09': '01', '0a': '67', '0b': '2b',
             '0c': 'fe', '0d': 'd7', '0e': 'ab', '0f': '76', '10': 'ca', '11': '82', '12': 'c9', '13': '7d', '14': 'fa',
             '15': '59', '16': '47', '17': 'f0',
             '18': 'ad', '19': 'd4', '1a': 'a2', '1b': 'af', '1c': '9c', '1d': 'a4', '1e': '72', '1f': 'c0', '20': 'b7',
             '21': 'fd', '22': '93', '23': '26',
             '24': '36', '25': '3f', '26': 'f7', '27': 'cc', '28': '34', '29': 'a5', '2a': 'e5', '2b': 'f1', '2c': '71',
             '2d': 'd8', '2e': '31', '2f': '15',
             '30': '04', '31': 'c7', '32': '23', '33': 'c3', '34': '18', '35': '96', '36': '05', '37': '9a', '38': '07',
             '39': '12', '3a': '80', '3b': 'e2',
             '3c': 'eb', '3d': '27', '3e': 'b2', '3f': '75', '40': '09', '41': '83', '42': '2c', '43': '1a', '44': '1b',
             '45': '6e', '46': '5a', '47': 'a0',
             '48': '52', '49': '3b', '4a': 'd6', '4b': 'b3', '4c': '29', '4d': 'e3', '4e': '2f', '4f': '84', '50': '53',
             '51': 'd1', '52': '00', '53': 'ed',
             '54': '20', '55': 'fc', '56': 'b1', '57': '5b', '58': '6a', '59': 'cb', '5a': 'be', '5b': '39', '5c': '4a',
             '5d': '4c', '5e': '58', '5f': 'cf',
             '60': 'd0', '61': 'ef', '62': 'aa', '63': 'fb', '64': '43', '65': '4d', '66': '33', '67': '85', '68': '45',
             '69': 'f9', '6a': '02', '6b': '7f',
             '6c': '50', '6d': '3c', '6e': '9f', '6f': 'a8', '70': '51', '71': 'a3', '72': '40', '73': '8f', '74': '92',
             '75': '9d', '76': '38', '77': 'f5',
             '78': 'bc', '79': 'b6', '7a': 'da', '7b': '21', '7c': '10', '7d': 'ff', '7e': 'f3', '7f': 'd2', '80': 'cd',
             '81': '0c', '82': '13', '83': 'ec',
             '84': '5f', '85': '97', '86': '44', '87': '17', '88': 'c4', '89': 'a7', '8a': '7e', '8b': '3d', '8c': '64',
             '8d': '5d', '8e': '19', '8f': '73',
             '90': '60', '91': '81', '92': '4f', '93': 'dc', '94': '22', '95': '2a', '96': '90', '97': '88', '98': '46',
             '99': 'ee', '9a': 'b8', '9b': '14',
             '9c': 'de', '9d': '5e', '9e': '0b', '9f': 'db', 'a0': 'e0', 'a1': '32', 'a2': '3a', 'a3': '0a', 'a4': '49',
             'a5': '06', 'a6': '24', 'a7': '5c',
             'a8': 'c2', 'a9': 'd3', 'aa': 'ac', 'ab': '62', 'ac': '91', 'ad': '95', 'ae': 'e4', 'af': '79', 'b0': 'e7',
             'b1': 'c8', 'b2': '37', 'b3': '6d',
             'b4': '8d', 'b5': 'd5', 'b6': '4e', 'b7': 'a9', 'b8': '6c', 'b9': '56', 'ba': 'f4', 'bb': 'ea', 'bc': '65',
             'bd': '7a', 'be': 'ae', 'bf': '08',
             'c0': 'ba', 'c1': '78', 'c2': '25', 'c3': '2e', 'c4': '1c', 'c5': 'a6', 'c6': 'b4', 'c7': 'c6', 'c8': 'e8',
             'c9': 'dd', 'ca': '74', 'cb': '1f',
             'cc': '4b', 'cd': 'bd', 'ce': '8b', 'cf': '8a', 'd0': '70', 'd1': '3e', 'd2': 'b5', 'd3': '66', 'd4': '48',
             'd5': '03', 'd6': 'f6', 'd7': '0e',
             'd8': '61', 'd9': '35', 'da': '57', 'db': 'b9', 'dc': '86', 'dd': 'c1', 'de': '1d', 'df': '9e', 'e0': 'e1',
             'e1': 'f8', 'e2': '98', 'e3': '11',
             'e4': '69', 'e5': 'd9', 'e6': '8e', 'e7': '94', 'e8': '9b', 'e9': '1e', 'ea': '87', 'eb': 'e9', 'ec': 'ce',
             'ed': '55', 'ee': '28', 'ef': 'df',
             'f0': '8c', 'f1': 'a1', 'f2': '89', 'f3': '0d', 'f4': 'bf', 'f5': 'e6', 'f6': '42', 'f7': '68', 'f8': '41',
             'f9': '99', 'fa': '2d', 'fb': '0f',
             'fc': 'b0', 'fd': '54', 'fe': 'bb', 'ff': '16'}

    slov1 = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
             '1000': '8',
             '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f', }

    crypted_mas = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    for i_x in range(4):
        for i_y in range(4):
            number0 = result_mas[i_y][i_x][:4]
            number1 = result_mas[i_y][i_x][4:]
            number0 = slov1.get(number0)
            number1 = slov1.get(number1)
            crypted_mas[i_y][i_x] = number0 + number1

    ''' w0 = mas_key_hex[0][0] + mas_key_hex[0][1] + mas_key_hex[0][2] + mas_key_hex[0][3]
        w1 = mas_key_hex[1][0] + mas_key_hex[1][1] + mas_key_hex[1][2] + mas_key_hex[1][3]
        w2 = mas_key_hex[2][0] + mas_key_hex[2][1] + mas_key_hex[2][2] + mas_key_hex[2][3]
        w3 = mas_key_hex[3][0] + mas_key_hex[3][1] + mas_key_hex[3][2] + mas_key_hex[3][3]'''
    # print("111111111111111111111111111")
    # print(mas_key_hex)
    # коли буду робити не для вправи з книжки, треба буде перекинути з бітового в словник slov

    div = ['01', '02', '04', '08', '10', '20', '40', '80', '1b', '36', '6c', 'b8']


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


    new_new_key = [['', '', '', ''],
                   ['', '', '', ''],
                   ['', '', '', ''],
                   ['', '', '', '']]
    mas_mas = []

    for i in range(12):
        # subbytes
        # 1
        round_mas = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for i_x in range(4):
            for i_y in range(4):
                number0 = crypted_mas[i_y][i_x]
                number0 = S_BOX.get(number0)
                round_mas[i_y][i_x] = number0
        # shiftrows
        # 2
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

        # MIXcolumns
        # 3
        if (i != 11):
            # ролписати станлартний метод, но на останньому кроці воно немає прауювати
            for i_mix in range(4):
                '''
                s0 = mul_by_02(round_mas[0][i]) ^ mul_by_03(round_mas[1][i]) ^ round_mas[2][i] ^ round_mas[3][i]
                s1 = round_mas[0][i] ^ mul_by_02(round_mas[1][i]) ^ mul_by_03(round_mas[2][i]) ^ round_mas[3][i]
                s2 = round_mas[0][i] ^ round_mas[1][i] ^ mul_by_02(state[2][i]) ^ mul_by_03(round_mas[3][i])
                s3 = mul_by_03(round_mas[0][i]) ^ round_mas[1][i] ^ round_mas[2][i] ^ mul_by_02(round_mas[3][i])
                '''
                # s0

                str_0_1 = mul_by_02(round_mas[0][i_mix])
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

                # s1

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

                # s2
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

        # XORRoundKey
        # 4
        w0 = slov1.get(mas_key_hex[0][0][:4]) + slov1.get(mas_key_hex[0][0][4:]) + slov1.get(
            mas_key_hex[1][0][:4]) + slov1.get(mas_key_hex[1][0][4:]) + slov1.get(mas_key_hex[2][0][:4]) + slov1.get(
            mas_key_hex[2][0][4:]) + slov1.get(mas_key_hex[3][0][:4]) + slov1.get(mas_key_hex[3][0][4:])
        w1 = slov1.get(mas_key_hex[0][1][:4]) + slov1.get(mas_key_hex[0][1][4:]) + slov1.get(
            mas_key_hex[1][1][:4]) + slov1.get(mas_key_hex[1][1][4:]) + slov1.get(mas_key_hex[2][1][:4]) + slov1.get(
            mas_key_hex[2][1][4:]) + slov1.get(mas_key_hex[3][1][:4]) + slov1.get(mas_key_hex[3][1][4:])
        w2 = slov1.get(mas_key_hex[0][2][:4]) + slov1.get(mas_key_hex[0][2][4:]) + slov1.get(
            mas_key_hex[1][2][:4]) + slov1.get(mas_key_hex[1][2][4:]) + slov1.get(mas_key_hex[2][2][:4]) + slov1.get(
            mas_key_hex[2][2][4:]) + slov1.get(mas_key_hex[3][2][:4]) + slov1.get(mas_key_hex[3][2][4:])
        w3 = slov1.get(mas_key_hex[0][3][:4]) + slov1.get(mas_key_hex[0][3][4:]) + slov1.get(
            mas_key_hex[1][3][:4]) + slov1.get(mas_key_hex[1][3][4:]) + slov1.get(mas_key_hex[2][3][:4]) + slov1.get(
            mas_key_hex[2][3][4:]) + slov1.get(mas_key_hex[3][3][:4]) + slov1.get(mas_key_hex[3][3][4:])
        w4 = slov1.get(mas_key_hex[0][4][:4]) + slov1.get(mas_key_hex[0][4][4:]) + slov1.get(
            mas_key_hex[1][4][:4]) + slov1.get(mas_key_hex[1][4][4:]) + slov1.get(mas_key_hex[2][4][:4]) + slov1.get(
            mas_key_hex[2][4][4:]) + slov1.get(mas_key_hex[3][4][:4]) + slov1.get(mas_key_hex[3][4][4:])
        w5 = slov1.get(mas_key_hex[0][5][:4]) + slov1.get(mas_key_hex[0][5][4:]) + slov1.get(
            mas_key_hex[1][5][:4]) + slov1.get(mas_key_hex[1][5][4:]) + slov1.get(mas_key_hex[2][5][:4]) + slov1.get(
            mas_key_hex[2][5][4:]) + slov1.get(mas_key_hex[3][5][:4]) + slov1.get(mas_key_hex[3][5][4:])

        # раундова функція
        # RotWord(w3)

        slov = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                '8': '1000',
                '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111', }

        slov1 = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
                 '1000': '8',
                 '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f', }

        w5 = w5[2:8] + w5[:2]

        w5 = S_BOX.get(w5[:2]) + S_BOX.get(w5[2:4]) + S_BOX.get(w5[4:6]) + S_BOX.get(w5[6:8])
        gfg = slov.get(w5[:2][0]) + slov.get(w5[:2][1])
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
        w5 = z + w5[2:8]

        w0 = mas_key_hex[0][0] + mas_key_hex[1][0] + mas_key_hex[2][0] + mas_key_hex[3][0]
        w5_new = slov.get(w5[0]) + slov.get(w5[1]) + slov.get(w5[2]) + slov.get(w5[3]) + slov.get(w5[4]) + slov.get(
            w5[5]) + slov.get(w5[6]) + slov.get(w5[7])
        z = ''
        for i_w3 in range(len(w0)):
            if int(w0[i_w3]) + int(w5_new[i_w3]) == 2:
                z += '0'
            elif int(w0[i_w3]) + int(w5_new[i_w3]) == 1:
                z += '1'
            else:
                z += '0'
        # z = slov1.get(z[:4]) + slov1.get(z[4:8]) + slov1.get(z[8:12]) + slov1.get(z[12:16]) + slov1.get(z[16:20]) + slov1.get(z[20:24]) + slov1.get(z[24:28]) + slov1.get(z[28:32])
        new_key = [['', '', '', '', '', ''],
                   ['', '', '', '', '', ''],
                   ['', '', '', '', '', ''],
                   ['', '', '', '', '', '']]
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
        # z2 = slov1.get(z2[:4]) + slov1.get(z2[4:8]) + slov1.get(z2[8:12]) + slov1.get(z2[12:16]) + slov1.get(z2[16:20]) + slov1.get(z2[20:24]) + slov1.get(z2[24:28]) + slov1.get(z2[28:32])
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
        # z3 = slov1.get(z3[:4]) + slov1.get(z3[4:8]) + slov1.get(z3[8:12]) + slov1.get(z3[12:16]) + slov1.get(z3[16:20]) + slov1.get(z3[20:24]) + slov1.get(z3[24:28]) + slov1.get(z3[28:32])
        new_key[0][3] = z3[:8]
        new_key[1][3] = z3[8:16]
        new_key[2][3] = z3[16:24]
        new_key[3][3] = z3[24:32]

        w4 = mas_key_hex[0][4] + mas_key_hex[1][4] + mas_key_hex[2][4] + mas_key_hex[3][4]
        z4 = ''
        for i_w4 in range(len(w4)):
            if int(w4[i_w4]) + int(z3[i_w4]) == 2:
                z4 += '0'
            elif int(w4[i_w4]) + int(z3[i_w4]) == 1:
                z4 += '1'
            else:
                z4 += '0'
        # z4 = slov1.get(z3[:4]) + slov1.get(z3[4:8]) + slov1.get(z3[8:12]) + slov1.get(z3[12:16]) + slov1.get(z3[16:20]) + slov1.get(z3[20:24]) + slov1.get(z3[24:28]) + slov1.get(z3[28:32])
        new_key[0][4] = z4[:8]
        new_key[1][4] = z4[8:16]
        new_key[2][4] = z4[16:24]
        new_key[3][4] = z4[24:32]

        w5 = mas_key_hex[0][5] + mas_key_hex[1][5] + mas_key_hex[2][5] + mas_key_hex[3][5]
        z5 = ''
        for i_w5 in range(len(w5)):
            if int(w5[i_w5]) + int(z4[i_w5]) == 2:
                z5 += '0'
            elif int(w5[i_w5]) + int(z4[i_w5]) == 1:
                z5 += '1'
            else:
                z5 += '0'
        # z5 = slov1.get(z3[:4]) + slov1.get(z3[4:8]) + slov1.get(z3[8:12]) + slov1.get(z3[12:16]) + slov1.get(z3[16:20]) + slov1.get(z3[20:24]) + slov1.get(z3[24:28]) + slov1.get(z3[28:32])
        new_key[0][5] = z5[:8]
        new_key[1][5] = z5[8:16]
        new_key[2][5] = z5[16:24]
        new_key[3][5] = z5[24:32]

        mas_key_hex = new_key

        if (i == 0):
            mass_key_hex = new_key
        if (i % 3 == 0):
            mas_key_hex = new_key

        for i_c in range(4):
            for t in range(6):
                new_key[i_c][t] = slov1.get(new_key[i_c][t][:4]) + slov1.get(new_key[i_c][t][4:])

        for i_v in range(4):
            for t in range(6):
                new_key[i_v][t] = slov.get(new_key[i_v][t][0]) + slov.get(new_key[i_v][t][1])

        if (i == 0):
            new_new_key[0][0] = slov1.get(buf_key_hex[0][4][:4]) + slov1.get(buf_key_hex[0][4][4:])
            new_new_key[1][0] = slov1.get(buf_key_hex[1][4][:4]) + slov1.get(buf_key_hex[1][4][4:])
            new_new_key[2][0] = slov1.get(buf_key_hex[2][4][:4]) + slov1.get(buf_key_hex[2][4][4:])
            new_new_key[3][0] = slov1.get(buf_key_hex[3][4][:4]) + slov1.get(buf_key_hex[3][4][4:])

            new_new_key[0][1] = slov1.get(buf_key_hex[0][5][:4]) + slov1.get(buf_key_hex[0][5][4:])
            new_new_key[1][1] = slov1.get(buf_key_hex[1][5][:4]) + slov1.get(buf_key_hex[1][5][4:])
            new_new_key[2][1] = slov1.get(buf_key_hex[2][5][:4]) + slov1.get(buf_key_hex[2][5][4:])
            new_new_key[3][1] = slov1.get(buf_key_hex[3][5][:4]) + slov1.get(buf_key_hex[3][5][4:])

            new_new_key[0][2] = slov1.get(mass_key_hex[0][0][:4]) + slov1.get(mass_key_hex[0][0][4:])
            new_new_key[1][2] = slov1.get(mass_key_hex[1][0][:4]) + slov1.get(mass_key_hex[1][0][4:])
            new_new_key[2][2] = slov1.get(mass_key_hex[2][0][:4]) + slov1.get(mass_key_hex[2][0][4:])
            new_new_key[3][2] = slov1.get(mass_key_hex[3][0][:4]) + slov1.get(mass_key_hex[3][0][4:])

            new_new_key[0][3] = slov1.get(mass_key_hex[0][1][:4]) + slov1.get(mass_key_hex[0][1][4:])
            new_new_key[1][3] = slov1.get(mass_key_hex[1][1][:4]) + slov1.get(mass_key_hex[1][1][4:])
            new_new_key[2][3] = slov1.get(mass_key_hex[2][1][:4]) + slov1.get(mass_key_hex[2][1][4:])
            new_new_key[3][3] = slov1.get(mass_key_hex[3][1][:4]) + slov1.get(mass_key_hex[3][1][4:])

        elif (i == 1):
            new_new_key[0][0] = slov1.get(masssss[0][2][:4]) + slov1.get(masssss[0][2][4:])
            new_new_key[1][0] = slov1.get(masssss[1][2][:4]) + slov1.get(masssss[1][2][4:])
            new_new_key[2][0] = slov1.get(masssss[2][2][:4]) + slov1.get(masssss[2][2][4:])
            new_new_key[3][0] = slov1.get(masssss[3][2][:4]) + slov1.get(masssss[3][2][4:])

            new_new_key[0][1] = slov1.get(masssss[0][3][:4]) + slov1.get(masssss[0][3][4:])
            new_new_key[1][1] = slov1.get(masssss[1][3][:4]) + slov1.get(masssss[1][3][4:])
            new_new_key[2][1] = slov1.get(masssss[2][3][:4]) + slov1.get(masssss[2][3][4:])
            new_new_key[3][1] = slov1.get(masssss[3][3][:4]) + slov1.get(masssss[3][3][4:])

            new_new_key[0][2] = slov1.get(masssss[0][4][:4]) + slov1.get(masssss[0][4][4:])
            new_new_key[1][2] = slov1.get(masssss[1][4][:4]) + slov1.get(masssss[1][4][4:])
            new_new_key[2][2] = slov1.get(masssss[2][4][:4]) + slov1.get(masssss[2][4][4:])
            new_new_key[3][2] = slov1.get(masssss[3][4][:4]) + slov1.get(masssss[3][4][4:])

            new_new_key[0][3] = slov1.get(masssss[0][5][:4]) + slov1.get(masssss[0][5][4:])
            new_new_key[1][3] = slov1.get(masssss[1][5][:4]) + slov1.get(masssss[1][5][4:])
            new_new_key[2][3] = slov1.get(masssss[2][5][:4]) + slov1.get(masssss[2][5][4:])
            new_new_key[3][3] = slov1.get(masssss[3][5][:4]) + slov1.get(masssss[3][5][4:])
            nnnn = new_key

        elif (i == 2):
            new_new_key[0][0] = slov1.get(masssss[0][0][:4]) + slov1.get(masssss[0][0][4:])
            new_new_key[1][0] = slov1.get(masssss[1][0][:4]) + slov1.get(masssss[1][0][4:])
            new_new_key[2][0] = slov1.get(masssss[2][0][:4]) + slov1.get(masssss[2][0][4:])
            new_new_key[3][0] = slov1.get(masssss[3][0][:4]) + slov1.get(masssss[3][0][4:])

            new_new_key[0][1] = slov1.get(masssss[0][1][:4]) + slov1.get(masssss[0][1][4:])
            new_new_key[1][1] = slov1.get(masssss[1][1][:4]) + slov1.get(masssss[1][1][4:])
            new_new_key[2][1] = slov1.get(masssss[2][1][:4]) + slov1.get(masssss[2][1][4:])
            new_new_key[3][1] = slov1.get(masssss[3][1][:4]) + slov1.get(masssss[3][1][4:])

            new_new_key[0][2] = slov1.get(masssss[0][2][:4]) + slov1.get(masssss[0][2][4:])
            new_new_key[1][2] = slov1.get(masssss[1][2][:4]) + slov1.get(masssss[1][2][4:])
            new_new_key[2][2] = slov1.get(masssss[2][2][:4]) + slov1.get(masssss[2][2][4:])
            new_new_key[3][2] = slov1.get(masssss[3][2][:4]) + slov1.get(masssss[3][2][4:])

            new_new_key[0][3] = slov1.get(masssss[0][3][:4]) + slov1.get(masssss[0][3][4:])
            new_new_key[1][3] = slov1.get(masssss[1][3][:4]) + slov1.get(masssss[1][3][4:])
            new_new_key[2][3] = slov1.get(masssss[2][3][:4]) + slov1.get(masssss[2][3][4:])
            new_new_key[3][3] = slov1.get(masssss[3][3][:4]) + slov1.get(masssss[3][3][4:])

            t_mas = new_key
        elif (i == 3):

            new_new_key[0][0] = slov1.get(nnnn[0][4][:4]) + slov1.get(nnnn[0][4][4:])
            new_new_key[1][0] = slov1.get(nnnn[1][4][:4]) + slov1.get(nnnn[1][4][4:])
            new_new_key[2][0] = slov1.get(nnnn[2][4][:4]) + slov1.get(nnnn[2][4][4:])
            new_new_key[3][0] = slov1.get(nnnn[3][4][:4]) + slov1.get(nnnn[3][4][4:])

            new_new_key[0][1] = slov1.get(nnnn[0][5][:4]) + slov1.get(nnnn[0][5][4:])
            new_new_key[1][1] = slov1.get(nnnn[1][5][:4]) + slov1.get(nnnn[1][5][4:])
            new_new_key[2][1] = slov1.get(nnnn[2][5][:4]) + slov1.get(nnnn[2][5][4:])
            new_new_key[3][1] = slov1.get(nnnn[3][5][:4]) + slov1.get(nnnn[3][5][4:])

            new_new_key[0][2] = slov1.get(t_mas[0][0][:4]) + slov1.get(t_mas[0][0][4:])
            new_new_key[1][2] = slov1.get(t_mas[1][0][:4]) + slov1.get(t_mas[1][0][4:])
            new_new_key[2][2] = slov1.get(t_mas[2][0][:4]) + slov1.get(t_mas[2][0][4:])
            new_new_key[3][2] = slov1.get(t_mas[3][0][:4]) + slov1.get(t_mas[3][0][4:])

            new_new_key[0][3] = slov1.get(t_mas[0][1][:4]) + slov1.get(t_mas[0][1][4:])
            new_new_key[1][3] = slov1.get(t_mas[1][1][:4]) + slov1.get(t_mas[1][1][4:])
            new_new_key[2][3] = slov1.get(t_mas[2][1][:4]) + slov1.get(t_mas[2][1][4:])
            new_new_key[3][3] = slov1.get(t_mas[3][1][:4]) + slov1.get(t_mas[3][1][4:])
            y_mas = new_key
        elif (i == 4):

            new_new_key[0][0] = slov1.get(t_mas[0][2][:4]) + slov1.get(t_mas[0][2][4:])
            new_new_key[1][0] = slov1.get(t_mas[1][2][:4]) + slov1.get(t_mas[1][2][4:])
            new_new_key[2][0] = slov1.get(t_mas[2][2][:4]) + slov1.get(t_mas[2][2][4:])
            new_new_key[3][0] = slov1.get(t_mas[3][2][:4]) + slov1.get(t_mas[3][2][4:])

            new_new_key[0][1] = slov1.get(t_mas[0][3][:4]) + slov1.get(t_mas[0][3][4:])
            new_new_key[1][1] = slov1.get(t_mas[1][3][:4]) + slov1.get(t_mas[1][3][4:])
            new_new_key[2][1] = slov1.get(t_mas[2][3][:4]) + slov1.get(t_mas[2][3][4:])
            new_new_key[3][1] = slov1.get(t_mas[3][3][:4]) + slov1.get(t_mas[3][3][4:])

            new_new_key[0][2] = slov1.get(t_mas[0][4][:4]) + slov1.get(t_mas[0][4][4:])
            new_new_key[1][2] = slov1.get(t_mas[1][4][:4]) + slov1.get(t_mas[1][4][4:])
            new_new_key[2][2] = slov1.get(t_mas[2][4][:4]) + slov1.get(t_mas[2][4][4:])
            new_new_key[3][2] = slov1.get(t_mas[3][4][:4]) + slov1.get(t_mas[3][4][4:])

            new_new_key[0][3] = slov1.get(t_mas[0][5][:4]) + slov1.get(t_mas[0][5][4:])
            new_new_key[1][3] = slov1.get(t_mas[1][5][:4]) + slov1.get(t_mas[1][5][4:])
            new_new_key[2][3] = slov1.get(t_mas[2][5][:4]) + slov1.get(t_mas[2][5][4:])
            new_new_key[3][3] = slov1.get(t_mas[3][5][:4]) + slov1.get(t_mas[3][5][4:])
            tr_mas = new_key
        elif (i == 5):

            new_new_key[0][0] = slov1.get(y_mas[0][0][:4]) + slov1.get(y_mas[0][0][4:])
            new_new_key[1][0] = slov1.get(y_mas[1][0][:4]) + slov1.get(y_mas[1][0][4:])
            new_new_key[2][0] = slov1.get(y_mas[2][0][:4]) + slov1.get(y_mas[2][0][4:])
            new_new_key[3][0] = slov1.get(y_mas[3][0][:4]) + slov1.get(y_mas[3][0][4:])

            new_new_key[0][1] = slov1.get(y_mas[0][1][:4]) + slov1.get(y_mas[0][1][4:])
            new_new_key[1][1] = slov1.get(y_mas[1][1][:4]) + slov1.get(y_mas[1][1][4:])
            new_new_key[2][1] = slov1.get(y_mas[2][1][:4]) + slov1.get(y_mas[2][1][4:])
            new_new_key[3][1] = slov1.get(y_mas[3][1][:4]) + slov1.get(y_mas[3][1][4:])

            new_new_key[0][2] = slov1.get(y_mas[0][2][:4]) + slov1.get(y_mas[0][2][4:])
            new_new_key[1][2] = slov1.get(y_mas[1][2][:4]) + slov1.get(y_mas[1][2][4:])
            new_new_key[2][2] = slov1.get(y_mas[2][2][:4]) + slov1.get(y_mas[2][2][4:])
            new_new_key[3][2] = slov1.get(y_mas[3][2][:4]) + slov1.get(y_mas[3][2][4:])

            new_new_key[0][3] = slov1.get(y_mas[0][3][:4]) + slov1.get(y_mas[0][3][4:])
            new_new_key[1][3] = slov1.get(y_mas[1][3][:4]) + slov1.get(y_mas[1][3][4:])
            new_new_key[2][3] = slov1.get(y_mas[2][3][:4]) + slov1.get(y_mas[2][3][4:])
            new_new_key[3][3] = slov1.get(y_mas[3][3][:4]) + slov1.get(y_mas[3][3][4:])
            gh_mas = new_key
        elif (i == 6):
            new_new_key[0][0] = slov1.get(y_mas[0][4][:4]) + slov1.get(y_mas[0][4][4:])
            new_new_key[1][0] = slov1.get(y_mas[1][4][:4]) + slov1.get(y_mas[1][4][4:])
            new_new_key[2][0] = slov1.get(y_mas[2][4][:4]) + slov1.get(y_mas[2][4][4:])
            new_new_key[3][0] = slov1.get(y_mas[3][4][:4]) + slov1.get(y_mas[3][4][4:])

            new_new_key[0][1] = slov1.get(y_mas[0][5][:4]) + slov1.get(y_mas[0][5][4:])
            new_new_key[1][1] = slov1.get(y_mas[1][5][:4]) + slov1.get(y_mas[1][5][4:])
            new_new_key[2][1] = slov1.get(y_mas[2][5][:4]) + slov1.get(y_mas[2][5][4:])
            new_new_key[3][1] = slov1.get(y_mas[3][5][:4]) + slov1.get(y_mas[3][5][4:])

            new_new_key[0][2] = slov1.get(tr_mas[0][0][:4]) + slov1.get(tr_mas[0][0][4:])
            new_new_key[1][2] = slov1.get(tr_mas[1][0][:4]) + slov1.get(tr_mas[1][0][4:])
            new_new_key[2][2] = slov1.get(tr_mas[2][0][:4]) + slov1.get(tr_mas[2][0][4:])
            new_new_key[3][2] = slov1.get(tr_mas[3][0][:4]) + slov1.get(tr_mas[3][0][4:])

            new_new_key[0][3] = slov1.get(tr_mas[0][1][:4]) + slov1.get(tr_mas[0][1][4:])
            new_new_key[1][3] = slov1.get(tr_mas[1][1][:4]) + slov1.get(tr_mas[1][1][4:])
            new_new_key[2][3] = slov1.get(tr_mas[2][1][:4]) + slov1.get(tr_mas[2][1][4:])
            new_new_key[3][3] = slov1.get(tr_mas[3][1][:4]) + slov1.get(tr_mas[3][1][4:])
            gfg_mas = new_key
        elif (i == 7):

            new_new_key[0][0] = slov1.get(tr_mas[0][2][:4]) + slov1.get(tr_mas[0][2][4:])
            new_new_key[1][0] = slov1.get(tr_mas[1][2][:4]) + slov1.get(tr_mas[1][2][4:])
            new_new_key[2][0] = slov1.get(tr_mas[2][2][:4]) + slov1.get(tr_mas[2][2][4:])
            new_new_key[3][0] = slov1.get(tr_mas[3][2][:4]) + slov1.get(tr_mas[3][2][4:])

            new_new_key[0][1] = slov1.get(tr_mas[0][3][:4]) + slov1.get(tr_mas[0][3][4:])
            new_new_key[1][1] = slov1.get(tr_mas[1][3][:4]) + slov1.get(tr_mas[1][3][4:])
            new_new_key[2][1] = slov1.get(tr_mas[2][3][:4]) + slov1.get(tr_mas[2][3][4:])
            new_new_key[3][1] = slov1.get(tr_mas[3][3][:4]) + slov1.get(tr_mas[3][3][4:])

            new_new_key[0][2] = slov1.get(tr_mas[0][4][:4]) + slov1.get(tr_mas[0][4][4:])
            new_new_key[1][2] = slov1.get(tr_mas[1][4][:4]) + slov1.get(tr_mas[1][4][4:])
            new_new_key[2][2] = slov1.get(tr_mas[2][4][:4]) + slov1.get(tr_mas[2][4][4:])
            new_new_key[3][2] = slov1.get(tr_mas[3][4][:4]) + slov1.get(tr_mas[3][4][4:])

            new_new_key[0][3] = slov1.get(tr_mas[0][5][:4]) + slov1.get(tr_mas[0][5][4:])
            new_new_key[1][3] = slov1.get(tr_mas[1][5][:4]) + slov1.get(tr_mas[1][5][4:])
            new_new_key[2][3] = slov1.get(tr_mas[2][5][:4]) + slov1.get(tr_mas[2][5][4:])
            new_new_key[3][3] = slov1.get(tr_mas[3][5][:4]) + slov1.get(tr_mas[3][5][4:])
            rrt_mas = new_key
        elif (i == 8):

            new_new_key[0][0] = slov1.get(gh_mas[0][0][:4]) + slov1.get(gh_mas[0][0][4:])
            new_new_key[1][0] = slov1.get(gh_mas[1][0][:4]) + slov1.get(gh_mas[1][0][4:])
            new_new_key[2][0] = slov1.get(gh_mas[2][0][:4]) + slov1.get(gh_mas[2][0][4:])
            new_new_key[3][0] = slov1.get(gh_mas[3][0][:4]) + slov1.get(gh_mas[3][0][4:])

            new_new_key[0][1] = slov1.get(gh_mas[0][1][:4]) + slov1.get(gh_mas[0][1][4:])
            new_new_key[1][1] = slov1.get(gh_mas[1][1][:4]) + slov1.get(gh_mas[1][1][4:])
            new_new_key[2][1] = slov1.get(gh_mas[2][1][:4]) + slov1.get(gh_mas[2][1][4:])
            new_new_key[3][1] = slov1.get(gh_mas[3][1][:4]) + slov1.get(gh_mas[3][1][4:])

            new_new_key[0][2] = slov1.get(gh_mas[0][2][:4]) + slov1.get(gh_mas[0][2][4:])
            new_new_key[1][2] = slov1.get(gh_mas[1][2][:4]) + slov1.get(gh_mas[1][2][4:])
            new_new_key[2][2] = slov1.get(gh_mas[2][2][:4]) + slov1.get(gh_mas[2][2][4:])
            new_new_key[3][2] = slov1.get(gh_mas[3][2][:4]) + slov1.get(gh_mas[3][2][4:])

            new_new_key[0][3] = slov1.get(gh_mas[0][3][:4]) + slov1.get(gh_mas[0][3][4:])
            new_new_key[1][3] = slov1.get(gh_mas[1][3][:4]) + slov1.get(gh_mas[1][3][4:])
            new_new_key[2][3] = slov1.get(gh_mas[2][3][:4]) + slov1.get(gh_mas[2][3][4:])
            new_new_key[3][3] = slov1.get(gh_mas[3][3][:4]) + slov1.get(gh_mas[3][3][4:])
        elif (i == 9):

            new_new_key[0][0] = slov1.get(gh_mas[0][4][:4]) + slov1.get(gh_mas[0][4][4:])
            new_new_key[1][0] = slov1.get(gh_mas[1][4][:4]) + slov1.get(gh_mas[1][4][4:])
            new_new_key[2][0] = slov1.get(gh_mas[2][4][:4]) + slov1.get(gh_mas[2][4][4:])
            new_new_key[3][0] = slov1.get(gh_mas[3][4][:4]) + slov1.get(gh_mas[3][4][4:])

            new_new_key[0][1] = slov1.get(gh_mas[0][5][:4]) + slov1.get(gh_mas[0][5][4:])
            new_new_key[1][1] = slov1.get(gh_mas[1][5][:4]) + slov1.get(gh_mas[1][5][4:])
            new_new_key[2][1] = slov1.get(gh_mas[2][5][:4]) + slov1.get(gh_mas[2][5][4:])
            new_new_key[3][1] = slov1.get(gh_mas[3][5][:4]) + slov1.get(gh_mas[3][5][4:])

            new_new_key[0][2] = slov1.get(gfg_mas[0][0][:4]) + slov1.get(gfg_mas[0][0][4:])
            new_new_key[1][2] = slov1.get(gfg_mas[1][0][:4]) + slov1.get(gfg_mas[1][0][4:])
            new_new_key[2][2] = slov1.get(gfg_mas[2][0][:4]) + slov1.get(gfg_mas[2][0][4:])
            new_new_key[3][2] = slov1.get(gfg_mas[3][0][:4]) + slov1.get(gfg_mas[3][0][4:])

            new_new_key[0][3] = slov1.get(gfg_mas[0][1][:4]) + slov1.get(gfg_mas[0][1][4:])
            new_new_key[1][3] = slov1.get(gfg_mas[1][1][:4]) + slov1.get(gfg_mas[1][1][4:])
            new_new_key[2][3] = slov1.get(gfg_mas[2][1][:4]) + slov1.get(gfg_mas[2][1][4:])
            new_new_key[3][3] = slov1.get(gfg_mas[3][1][:4]) + slov1.get(gfg_mas[3][1][4:])
        elif (i == 10):
            new_new_key[0][0] = slov1.get(gfg_mas[0][2][:4]) + slov1.get(gfg_mas[0][2][4:])
            new_new_key[1][0] = slov1.get(gfg_mas[1][2][:4]) + slov1.get(gfg_mas[1][2][4:])
            new_new_key[2][0] = slov1.get(gfg_mas[2][2][:4]) + slov1.get(gfg_mas[2][2][4:])
            new_new_key[3][0] = slov1.get(gfg_mas[3][2][:4]) + slov1.get(gfg_mas[3][2][4:])

            new_new_key[0][1] = slov1.get(gfg_mas[0][3][:4]) + slov1.get(gfg_mas[0][3][4:])
            new_new_key[1][1] = slov1.get(gfg_mas[1][3][:4]) + slov1.get(gfg_mas[1][3][4:])
            new_new_key[2][1] = slov1.get(gfg_mas[2][3][:4]) + slov1.get(gfg_mas[2][3][4:])
            new_new_key[3][1] = slov1.get(gfg_mas[3][3][:4]) + slov1.get(gfg_mas[3][3][4:])

            new_new_key[0][2] = slov1.get(gfg_mas[0][4][:4]) + slov1.get(gfg_mas[0][4][4:])
            new_new_key[1][2] = slov1.get(gfg_mas[1][4][:4]) + slov1.get(gfg_mas[1][4][4:])
            new_new_key[2][2] = slov1.get(gfg_mas[2][4][:4]) + slov1.get(gfg_mas[2][4][4:])
            new_new_key[3][2] = slov1.get(gfg_mas[3][4][:4]) + slov1.get(gfg_mas[3][4][4:])

            new_new_key[0][3] = slov1.get(gfg_mas[0][5][:4]) + slov1.get(gfg_mas[0][5][4:])
            new_new_key[1][3] = slov1.get(gfg_mas[1][5][:4]) + slov1.get(gfg_mas[1][5][4:])
            new_new_key[2][3] = slov1.get(gfg_mas[2][5][:4]) + slov1.get(gfg_mas[2][5][4:])
            new_new_key[3][3] = slov1.get(gfg_mas[3][5][:4]) + slov1.get(gfg_mas[3][5][4:])

        elif (i == 11):
            new_new_key[0][0] = slov1.get(rrt_mas[0][0][:4]) + slov1.get(rrt_mas[0][0][4:])
            new_new_key[1][0] = slov1.get(rrt_mas[1][0][:4]) + slov1.get(rrt_mas[1][0][4:])
            new_new_key[2][0] = slov1.get(rrt_mas[2][0][:4]) + slov1.get(rrt_mas[2][0][4:])
            new_new_key[3][0] = slov1.get(rrt_mas[3][0][:4]) + slov1.get(rrt_mas[3][0][4:])

            new_new_key[0][1] = slov1.get(rrt_mas[0][1][:4]) + slov1.get(rrt_mas[0][1][4:])
            new_new_key[1][1] = slov1.get(rrt_mas[1][1][:4]) + slov1.get(rrt_mas[1][1][4:])
            new_new_key[2][1] = slov1.get(rrt_mas[2][1][:4]) + slov1.get(rrt_mas[2][1][4:])
            new_new_key[3][1] = slov1.get(rrt_mas[3][1][:4]) + slov1.get(rrt_mas[3][1][4:])

            new_new_key[0][2] = slov1.get(rrt_mas[0][2][:4]) + slov1.get(rrt_mas[0][2][4:])
            new_new_key[1][2] = slov1.get(rrt_mas[1][2][:4]) + slov1.get(rrt_mas[1][2][4:])
            new_new_key[2][2] = slov1.get(rrt_mas[2][2][:4]) + slov1.get(rrt_mas[2][2][4:])
            new_new_key[3][2] = slov1.get(rrt_mas[3][2][:4]) + slov1.get(rrt_mas[3][2][4:])

            new_new_key[0][3] = slov1.get(rrt_mas[0][3][:4]) + slov1.get(rrt_mas[0][3][4:])
            new_new_key[1][3] = slov1.get(rrt_mas[1][3][:4]) + slov1.get(rrt_mas[1][3][4:])
            new_new_key[2][3] = slov1.get(rrt_mas[2][3][:4]) + slov1.get(rrt_mas[2][3][4:])
            new_new_key[3][3] = slov1.get(rrt_mas[3][3][:4]) + slov1.get(rrt_mas[3][3][4:])



        for i_new in range(4):
            for i_new_new in range(4):
                round_mas[i_new][i_new_new] = slov.get(round_mas[i_new][i_new_new][0]) + slov.get(
                    round_mas[i_new][i_new_new][1])

        for i_new in range(4):
            for i_new_new in range(4):
                new_new_key[i_new][i_new_new] = slov.get(new_new_key[i_new][i_new_new][0]) + slov.get(
                    new_new_key[i_new][i_new_new][1])

        for i_new in range(4):
            for i_new_new in range(4):
                str1 = new_new_key[i_new][i_new_new]
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
        masssss = new_key






    with open('Cryptedtext.txt', 'r', encoding='utf-8') as input_file:
        # зчитування вмісту файлу
        cryptotext = input_file.read()
    def str2hex(s):
        return binascii.hexlify(bytes(str.encode(s)))
    def hex2str(h):
        return binascii.unhexlify(h)
    cryptotext_hex = str2hex(cryptotext)
    cryptotext_hex = cryptotext_hex.decode('utf-8')

    unhexsring = hex2str(cryptotext_hex).decode('utf-8')
    m = 0
    mas_crypto_hex = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i_x in range(4):
        for i_y in range(4):
            string = cryptotext_hex[0 + m] + cryptotext_hex[1 + m]
            mas_crypto_hex[i_y][i_x] = string
            m += 2
    '''mas_crypto_hex = [['32', '88', '31', 'e0'],
                      ['43', '5a', '31', '37'],
                      ['f6', '30', '98', '07'],
                      ['a8', '8d', 'a2', '34']]
    '''
    mas_crypto_hex = [['00', '44', '88', 'cc'],
                      ['11', '55', '99', 'dd'],
                      ['22', '66', 'aa', 'ee'],
                      ['33', '77', 'bb', 'ff']]
    for i in range(4):
        for t in range(4):
            crypted_mas[i][t] = slov.get(crypted_mas[i][t][0]) + slov.get(crypted_mas[i][t][1])
    first = crypted_mas
    for i in range(4):
        for t in range(4):
            decrypted_key[i][t] = slov.get(decrypted_key[i][t][0]) + slov.get(decrypted_key[i][t][1])
    a = random.randrange(0, 3)
    b = random.randrange(0, 3)
    c = random.randrange(0, 7)
    if (decrypted_key[a][b][c] == '0'):
        number = decrypted_key[a][b]
        number = number[:(c - 1)] + "1" + number[c:]
        decrypted_key[a][b] = number
    else:
        number = decrypted_key[a][b]
        number = number[:(c - 1)] + "0" + number[c:]
        decrypted_key[a][b] = number
    mas_key_hex = decrypted_key
    buf_key_hex = [['', '', '', '', '', ''],
                   ['', '', '', '', '', ''],
                   ['', '', '', '', '', ''],
                   ['', '', '', '', '', '']]
    buf_key_hex = mas_key_hex
    mass_key_hex = [['', '', '', '', '', ''],
                    ['', '', '', '', '', ''],
                    ['', '', '', '', '', ''],
                    ['', '', '', '', '', '']]
    mass_key_hex = mas_key_hex
    slov = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
            '8': '1000',
            '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}
    for i_x in range(4):
        for i_y in range(4):
            number0 = mas_crypto_hex[i_y][i_x][0]
            number1 = mas_crypto_hex[i_y][i_x][1]
            number0 = slov.get(number0)
            number1 = slov.get(number1)
            mas_crypto_hex[i_y][i_x] = number0 + number1
    for i_y in range(4):
        for i_x in range(6):
            number0 = mas_key_hex[i_y][i_x][0]
            number1 = mas_key_hex[i_y][i_x][1]
            number0 = slov.get(number0)
            number1 = slov.get(number1)
            mas_key_hex[i_y][i_x] = number0 + number1
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
    S_BOX = {'00': '63', '01': '7c', '02': '77', '03': '7b', '04': 'f2', '05': '6b', '06': '6f', '07': 'c5',
             '08': '30',
             '09': '01', '0a': '67', '0b': '2b',
             '0c': 'fe', '0d': 'd7', '0e': 'ab', '0f': '76', '10': 'ca', '11': '82', '12': 'c9', '13': '7d',
             '14': 'fa',
             '15': '59', '16': '47', '17': 'f0',
             '18': 'ad', '19': 'd4', '1a': 'a2', '1b': 'af', '1c': '9c', '1d': 'a4', '1e': '72', '1f': 'c0',
             '20': 'b7',
             '21': 'fd', '22': '93', '23': '26',
             '24': '36', '25': '3f', '26': 'f7', '27': 'cc', '28': '34', '29': 'a5', '2a': 'e5', '2b': 'f1',
             '2c': '71',
             '2d': 'd8', '2e': '31', '2f': '15',
             '30': '04', '31': 'c7', '32': '23', '33': 'c3', '34': '18', '35': '96', '36': '05', '37': '9a',
             '38': '07',
             '39': '12', '3a': '80', '3b': 'e2',
             '3c': 'eb', '3d': '27', '3e': 'b2', '3f': '75', '40': '09', '41': '83', '42': '2c', '43': '1a',
             '44': '1b',
             '45': '6e', '46': '5a', '47': 'a0',
             '48': '52', '49': '3b', '4a': 'd6', '4b': 'b3', '4c': '29', '4d': 'e3', '4e': '2f', '4f': '84',
             '50': '53',
             '51': 'd1', '52': '00', '53': 'ed',
             '54': '20', '55': 'fc', '56': 'b1', '57': '5b', '58': '6a', '59': 'cb', '5a': 'be', '5b': '39',
             '5c': '4a',
             '5d': '4c', '5e': '58', '5f': 'cf',
             '60': 'd0', '61': 'ef', '62': 'aa', '63': 'fb', '64': '43', '65': '4d', '66': '33', '67': '85',
             '68': '45',
             '69': 'f9', '6a': '02', '6b': '7f',
             '6c': '50', '6d': '3c', '6e': '9f', '6f': 'a8', '70': '51', '71': 'a3', '72': '40', '73': '8f',
             '74': '92',
             '75': '9d', '76': '38', '77': 'f5',
             '78': 'bc', '79': 'b6', '7a': 'da', '7b': '21', '7c': '10', '7d': 'ff', '7e': 'f3', '7f': 'd2',
             '80': 'cd',
             '81': '0c', '82': '13', '83': 'ec',
             '84': '5f', '85': '97', '86': '44', '87': '17', '88': 'c4', '89': 'a7', '8a': '7e', '8b': '3d',
             '8c': '64',
             '8d': '5d', '8e': '19', '8f': '73',
             '90': '60', '91': '81', '92': '4f', '93': 'dc', '94': '22', '95': '2a', '96': '90', '97': '88',
             '98': '46',
             '99': 'ee', '9a': 'b8', '9b': '14',
             '9c': 'de', '9d': '5e', '9e': '0b', '9f': 'db', 'a0': 'e0', 'a1': '32', 'a2': '3a', 'a3': '0a',
             'a4': '49',
             'a5': '06', 'a6': '24', 'a7': '5c',
             'a8': 'c2', 'a9': 'd3', 'aa': 'ac', 'ab': '62', 'ac': '91', 'ad': '95', 'ae': 'e4', 'af': '79',
             'b0': 'e7',
             'b1': 'c8', 'b2': '37', 'b3': '6d',
             'b4': '8d', 'b5': 'd5', 'b6': '4e', 'b7': 'a9', 'b8': '6c', 'b9': '56', 'ba': 'f4', 'bb': 'ea',
             'bc': '65',
             'bd': '7a', 'be': 'ae', 'bf': '08',
             'c0': 'ba', 'c1': '78', 'c2': '25', 'c3': '2e', 'c4': '1c', 'c5': 'a6', 'c6': 'b4', 'c7': 'c6',
             'c8': 'e8',
             'c9': 'dd', 'ca': '74', 'cb': '1f',
             'cc': '4b', 'cd': 'bd', 'ce': '8b', 'cf': '8a', 'd0': '70', 'd1': '3e', 'd2': 'b5', 'd3': '66',
             'd4': '48',
             'd5': '03', 'd6': 'f6', 'd7': '0e',
             'd8': '61', 'd9': '35', 'da': '57', 'db': 'b9', 'dc': '86', 'dd': 'c1', 'de': '1d', 'df': '9e',
             'e0': 'e1',
             'e1': 'f8', 'e2': '98', 'e3': '11',
             'e4': '69', 'e5': 'd9', 'e6': '8e', 'e7': '94', 'e8': '9b', 'e9': '1e', 'ea': '87', 'eb': 'e9',
             'ec': 'ce',
             'ed': '55', 'ee': '28', 'ef': 'df',
             'f0': '8c', 'f1': 'a1', 'f2': '89', 'f3': '0d', 'f4': 'bf', 'f5': 'e6', 'f6': '42', 'f7': '68',
             'f8': '41',
             'f9': '99', 'fa': '2d', 'fb': '0f',
             'fc': 'b0', 'fd': '54', 'fe': 'bb', 'ff': '16'}
    slov1 = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
             '1000': '8',
             '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f', }
    crypted_mas = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i_x in range(4):
        for i_y in range(4):
            number0 = result_mas[i_y][i_x][:4]
            number1 = result_mas[i_y][i_x][4:]
            number0 = slov1.get(number0)
            number1 = slov1.get(number1)
            crypted_mas[i_y][i_x] = number0 + number1
    ''' w0 = mas_key_hex[0][0] + mas_key_hex[0][1] + mas_key_hex[0][2] + mas_key_hex[0][3]
        w1 = mas_key_hex[1][0] + mas_key_hex[1][1] + mas_key_hex[1][2] + mas_key_hex[1][3]
        w2 = mas_key_hex[2][0] + mas_key_hex[2][1] + mas_key_hex[2][2] + mas_key_hex[2][3]
        w3 = mas_key_hex[3][0] + mas_key_hex[3][1] + mas_key_hex[3][2] + mas_key_hex[3][3]'''
    # print("111111111111111111111111111")
    # print(mas_key_hex)
    # коли буду робити не для вправи з книжки, треба буде перекинути з бітового в словник slov
    div = ['01', '02', '04', '08', '10', '20', '40', '80', '1b', '36', '6c', 'b8']
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
    new_new_key = [['', '', '', ''],
                   ['', '', '', ''],
                   ['', '', '', ''],
                   ['', '', '', '']]
    mas_mas = []
    for i in range(12):
        # subbytes
        # 1
        round_mas = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for i_x in range(4):
            for i_y in range(4):
                number0 = crypted_mas[i_y][i_x]
                number0 = S_BOX.get(number0)
                round_mas[i_y][i_x] = number0
        # shiftrows
        # 2
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
        # MIXcolumns
        # 3
        if (i != 11):
            # ролписати станлартний метод, но на останньому кроці воно немає прауювати
            for i_mix in range(4):
                '''
                s0 = mul_by_02(round_mas[0][i]) ^ mul_by_03(round_mas[1][i]) ^ round_mas[2][i] ^ round_mas[3][i]
                s1 = round_mas[0][i] ^ mul_by_02(round_mas[1][i]) ^ mul_by_03(round_mas[2][i]) ^ round_mas[3][i]
                s2 = round_mas[0][i] ^ round_mas[1][i] ^ mul_by_02(state[2][i]) ^ mul_by_03(round_mas[3][i])
                s3 = mul_by_03(round_mas[0][i]) ^ round_mas[1][i] ^ round_mas[2][i] ^ mul_by_02(round_mas[3][i])
                '''
                # s0
                str_0_1 = mul_by_02(round_mas[0][i_mix])
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
                # s1
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
                # s2
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
        # XORRoundKey
        # 4
        w0 = slov1.get(mas_key_hex[0][0][:4]) + slov1.get(mas_key_hex[0][0][4:]) + slov1.get(
            mas_key_hex[1][0][:4]) + slov1.get(mas_key_hex[1][0][4:]) + slov1.get(
            mas_key_hex[2][0][:4]) + slov1.get(
            mas_key_hex[2][0][4:]) + slov1.get(mas_key_hex[3][0][:4]) + slov1.get(mas_key_hex[3][0][4:])
        w1 = slov1.get(mas_key_hex[0][1][:4]) + slov1.get(mas_key_hex[0][1][4:]) + slov1.get(
            mas_key_hex[1][1][:4]) + slov1.get(mas_key_hex[1][1][4:]) + slov1.get(
            mas_key_hex[2][1][:4]) + slov1.get(
            mas_key_hex[2][1][4:]) + slov1.get(mas_key_hex[3][1][:4]) + slov1.get(mas_key_hex[3][1][4:])
        w2 = slov1.get(mas_key_hex[0][2][:4]) + slov1.get(mas_key_hex[0][2][4:]) + slov1.get(
            mas_key_hex[1][2][:4]) + slov1.get(mas_key_hex[1][2][4:]) + slov1.get(
            mas_key_hex[2][2][:4]) + slov1.get(
            mas_key_hex[2][2][4:]) + slov1.get(mas_key_hex[3][2][:4]) + slov1.get(mas_key_hex[3][2][4:])
        w3 = slov1.get(mas_key_hex[0][3][:4]) + slov1.get(mas_key_hex[0][3][4:]) + slov1.get(
            mas_key_hex[1][3][:4]) + slov1.get(mas_key_hex[1][3][4:]) + slov1.get(
            mas_key_hex[2][3][:4]) + slov1.get(
            mas_key_hex[2][3][4:]) + slov1.get(mas_key_hex[3][3][:4]) + slov1.get(mas_key_hex[3][3][4:])
        w4 = slov1.get(mas_key_hex[0][4][:4]) + slov1.get(mas_key_hex[0][4][4:]) + slov1.get(
            mas_key_hex[1][4][:4]) + slov1.get(mas_key_hex[1][4][4:]) + slov1.get(
            mas_key_hex[2][4][:4]) + slov1.get(
            mas_key_hex[2][4][4:]) + slov1.get(mas_key_hex[3][4][:4]) + slov1.get(mas_key_hex[3][4][4:])
        w5 = slov1.get(mas_key_hex[0][5][:4]) + slov1.get(mas_key_hex[0][5][4:]) + slov1.get(
            mas_key_hex[1][5][:4]) + slov1.get(mas_key_hex[1][5][4:]) + slov1.get(
            mas_key_hex[2][5][:4]) + slov1.get(
            mas_key_hex[2][5][4:]) + slov1.get(mas_key_hex[3][5][:4]) + slov1.get(mas_key_hex[3][5][4:])
        # раундова функція
        # RotWord(w3)
        slov = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
                '7': '0111',
                '8': '1000',
                '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111', }
        slov1 = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6',
                 '0111': '7',
                 '1000': '8',
                 '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f', }
        w5 = w5[2:8] + w5[:2]
        w5 = S_BOX.get(w5[:2]) + S_BOX.get(w5[2:4]) + S_BOX.get(w5[4:6]) + S_BOX.get(w5[6:8])
        gfg = slov.get(w5[:2][0]) + slov.get(w5[:2][1])
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
        w5 = z + w5[2:8]
        w0 = mas_key_hex[0][0] + mas_key_hex[1][0] + mas_key_hex[2][0] + mas_key_hex[3][0]
        w5_new = slov.get(w5[0]) + slov.get(w5[1]) + slov.get(w5[2]) + slov.get(w5[3]) + slov.get(w5[4]) + slov.get(
            w5[5]) + slov.get(w5[6]) + slov.get(w5[7])
        z = ''
        for i_w3 in range(len(w0)):
            if int(w0[i_w3]) + int(w5_new[i_w3]) == 2:
                z += '0'
            elif int(w0[i_w3]) + int(w5_new[i_w3]) == 1:
                z += '1'
            else:
                z += '0'
        # z = slov1.get(z[:4]) + slov1.get(z[4:8]) + slov1.get(z[8:12]) + slov1.get(z[12:16]) + slov1.get(z[16:20]) + slov1.get(z[20:24]) + slov1.get(z[24:28]) + slov1.get(z[28:32])
        new_key = [['', '', '', '', '', ''],
                   ['', '', '', '', '', ''],
                   ['', '', '', '', '', ''],
                   ['', '', '', '', '', '']]
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
        # z2 = slov1.get(z2[:4]) + slov1.get(z2[4:8]) + slov1.get(z2[8:12]) + slov1.get(z2[12:16]) + slov1.get(z2[16:20]) + slov1.get(z2[20:24]) + slov1.get(z2[24:28]) + slov1.get(z2[28:32])
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
        # z3 = slov1.get(z3[:4]) + slov1.get(z3[4:8]) + slov1.get(z3[8:12]) + slov1.get(z3[12:16]) + slov1.get(z3[16:20]) + slov1.get(z3[20:24]) + slov1.get(z3[24:28]) + slov1.get(z3[28:32])
        new_key[0][3] = z3[:8]
        new_key[1][3] = z3[8:16]
        new_key[2][3] = z3[16:24]
        new_key[3][3] = z3[24:32]
        w4 = mas_key_hex[0][4] + mas_key_hex[1][4] + mas_key_hex[2][4] + mas_key_hex[3][4]
        z4 = ''
        for i_w4 in range(len(w4)):
            if int(w4[i_w4]) + int(z3[i_w4]) == 2:
                z4 += '0'
            elif int(w4[i_w4]) + int(z3[i_w4]) == 1:
                z4 += '1'
            else:
                z4 += '0'
        # z4 = slov1.get(z3[:4]) + slov1.get(z3[4:8]) + slov1.get(z3[8:12]) + slov1.get(z3[12:16]) + slov1.get(z3[16:20]) + slov1.get(z3[20:24]) + slov1.get(z3[24:28]) + slov1.get(z3[28:32])
        new_key[0][4] = z4[:8]
        new_key[1][4] = z4[8:16]
        new_key[2][4] = z4[16:24]
        new_key[3][4] = z4[24:32]
        w5 = mas_key_hex[0][5] + mas_key_hex[1][5] + mas_key_hex[2][5] + mas_key_hex[3][5]
        z5 = ''
        for i_w5 in range(len(w5)):
            if int(w5[i_w5]) + int(z4[i_w5]) == 2:
                z5 += '0'
            elif int(w5[i_w5]) + int(z4[i_w5]) == 1:
                z5 += '1'
            else:
                z5 += '0'
        # z5 = slov1.get(z3[:4]) + slov1.get(z3[4:8]) + slov1.get(z3[8:12]) + slov1.get(z3[12:16]) + slov1.get(z3[16:20]) + slov1.get(z3[20:24]) + slov1.get(z3[24:28]) + slov1.get(z3[28:32])
        new_key[0][5] = z5[:8]
        new_key[1][5] = z5[8:16]
        new_key[2][5] = z5[16:24]
        new_key[3][5] = z5[24:32]
        mas_key_hex = new_key
        if (i == 0):
            mass_key_hex = new_key
        if (i % 3 == 0):
            mas_key_hex = new_key

        for i_c in range(4):
            for t in range(6):
                new_key[i_c][t] = slov1.get(new_key[i_c][t][:4]) + slov1.get(new_key[i_c][t][4:])

        for i_v in range(4):
            for t in range(6):
                new_key[i_v][t] = slov.get(new_key[i_v][t][0]) + slov.get(new_key[i_v][t][1])
        if (i == 0):
            new_new_key[0][0] = slov1.get(buf_key_hex[0][4][:4]) + slov1.get(buf_key_hex[0][4][4:])
            new_new_key[1][0] = slov1.get(buf_key_hex[1][4][:4]) + slov1.get(buf_key_hex[1][4][4:])
            new_new_key[2][0] = slov1.get(buf_key_hex[2][4][:4]) + slov1.get(buf_key_hex[2][4][4:])
            new_new_key[3][0] = slov1.get(buf_key_hex[3][4][:4]) + slov1.get(buf_key_hex[3][4][4:])
            new_new_key[0][1] = slov1.get(buf_key_hex[0][5][:4]) + slov1.get(buf_key_hex[0][5][4:])
            new_new_key[1][1] = slov1.get(buf_key_hex[1][5][:4]) + slov1.get(buf_key_hex[1][5][4:])
            new_new_key[2][1] = slov1.get(buf_key_hex[2][5][:4]) + slov1.get(buf_key_hex[2][5][4:])
            new_new_key[3][1] = slov1.get(buf_key_hex[3][5][:4]) + slov1.get(buf_key_hex[3][5][4:])
            new_new_key[0][2] = slov1.get(mass_key_hex[0][0][:4]) + slov1.get(mass_key_hex[0][0][4:])
            new_new_key[1][2] = slov1.get(mass_key_hex[1][0][:4]) + slov1.get(mass_key_hex[1][0][4:])
            new_new_key[2][2] = slov1.get(mass_key_hex[2][0][:4]) + slov1.get(mass_key_hex[2][0][4:])
            new_new_key[3][2] = slov1.get(mass_key_hex[3][0][:4]) + slov1.get(mass_key_hex[3][0][4:])
            new_new_key[0][3] = slov1.get(mass_key_hex[0][1][:4]) + slov1.get(mass_key_hex[0][1][4:])
            new_new_key[1][3] = slov1.get(mass_key_hex[1][1][:4]) + slov1.get(mass_key_hex[1][1][4:])
            new_new_key[2][3] = slov1.get(mass_key_hex[2][1][:4]) + slov1.get(mass_key_hex[2][1][4:])
            new_new_key[3][3] = slov1.get(mass_key_hex[3][1][:4]) + slov1.get(mass_key_hex[3][1][4:])

        elif (i == 1):
            new_new_key[0][0] = slov1.get(masssss[0][2][:4]) + slov1.get(masssss[0][2][4:])
            new_new_key[1][0] = slov1.get(masssss[1][2][:4]) + slov1.get(masssss[1][2][4:])
            new_new_key[2][0] = slov1.get(masssss[2][2][:4]) + slov1.get(masssss[2][2][4:])
            new_new_key[3][0] = slov1.get(masssss[3][2][:4]) + slov1.get(masssss[3][2][4:])
            new_new_key[0][1] = slov1.get(masssss[0][3][:4]) + slov1.get(masssss[0][3][4:])
            new_new_key[1][1] = slov1.get(masssss[1][3][:4]) + slov1.get(masssss[1][3][4:])
            new_new_key[2][1] = slov1.get(masssss[2][3][:4]) + slov1.get(masssss[2][3][4:])
            new_new_key[3][1] = slov1.get(masssss[3][3][:4]) + slov1.get(masssss[3][3][4:])
            new_new_key[0][2] = slov1.get(masssss[0][4][:4]) + slov1.get(masssss[0][4][4:])
            new_new_key[1][2] = slov1.get(masssss[1][4][:4]) + slov1.get(masssss[1][4][4:])
            new_new_key[2][2] = slov1.get(masssss[2][4][:4]) + slov1.get(masssss[2][4][4:])
            new_new_key[3][2] = slov1.get(masssss[3][4][:4]) + slov1.get(masssss[3][4][4:])
            new_new_key[0][3] = slov1.get(masssss[0][5][:4]) + slov1.get(masssss[0][5][4:])
            new_new_key[1][3] = slov1.get(masssss[1][5][:4]) + slov1.get(masssss[1][5][4:])
            new_new_key[2][3] = slov1.get(masssss[2][5][:4]) + slov1.get(masssss[2][5][4:])
            new_new_key[3][3] = slov1.get(masssss[3][5][:4]) + slov1.get(masssss[3][5][4:])
            nnnn = new_key

        elif (i == 2):
            new_new_key[0][0] = slov1.get(masssss[0][0][:4]) + slov1.get(masssss[0][0][4:])
            new_new_key[1][0] = slov1.get(masssss[1][0][:4]) + slov1.get(masssss[1][0][4:])
            new_new_key[2][0] = slov1.get(masssss[2][0][:4]) + slov1.get(masssss[2][0][4:])
            new_new_key[3][0] = slov1.get(masssss[3][0][:4]) + slov1.get(masssss[3][0][4:])
            new_new_key[0][1] = slov1.get(masssss[0][1][:4]) + slov1.get(masssss[0][1][4:])
            new_new_key[1][1] = slov1.get(masssss[1][1][:4]) + slov1.get(masssss[1][1][4:])
            new_new_key[2][1] = slov1.get(masssss[2][1][:4]) + slov1.get(masssss[2][1][4:])
            new_new_key[3][1] = slov1.get(masssss[3][1][:4]) + slov1.get(masssss[3][1][4:])
            new_new_key[0][2] = slov1.get(masssss[0][2][:4]) + slov1.get(masssss[0][2][4:])
            new_new_key[1][2] = slov1.get(masssss[1][2][:4]) + slov1.get(masssss[1][2][4:])
            new_new_key[2][2] = slov1.get(masssss[2][2][:4]) + slov1.get(masssss[2][2][4:])
            new_new_key[3][2] = slov1.get(masssss[3][2][:4]) + slov1.get(masssss[3][2][4:])
            new_new_key[0][3] = slov1.get(masssss[0][3][:4]) + slov1.get(masssss[0][3][4:])
            new_new_key[1][3] = slov1.get(masssss[1][3][:4]) + slov1.get(masssss[1][3][4:])
            new_new_key[2][3] = slov1.get(masssss[2][3][:4]) + slov1.get(masssss[2][3][4:])
            new_new_key[3][3] = slov1.get(masssss[3][3][:4]) + slov1.get(masssss[3][3][4:])
            t_mas = new_key
        elif (i == 3):
            new_new_key[0][0] = slov1.get(nnnn[0][4][:4]) + slov1.get(nnnn[0][4][4:])
            new_new_key[1][0] = slov1.get(nnnn[1][4][:4]) + slov1.get(nnnn[1][4][4:])
            new_new_key[2][0] = slov1.get(nnnn[2][4][:4]) + slov1.get(nnnn[2][4][4:])
            new_new_key[3][0] = slov1.get(nnnn[3][4][:4]) + slov1.get(nnnn[3][4][4:])
            new_new_key[0][1] = slov1.get(nnnn[0][5][:4]) + slov1.get(nnnn[0][5][4:])
            new_new_key[1][1] = slov1.get(nnnn[1][5][:4]) + slov1.get(nnnn[1][5][4:])
            new_new_key[2][1] = slov1.get(nnnn[2][5][:4]) + slov1.get(nnnn[2][5][4:])
            new_new_key[3][1] = slov1.get(nnnn[3][5][:4]) + slov1.get(nnnn[3][5][4:])
            new_new_key[0][2] = slov1.get(t_mas[0][0][:4]) + slov1.get(t_mas[0][0][4:])
            new_new_key[1][2] = slov1.get(t_mas[1][0][:4]) + slov1.get(t_mas[1][0][4:])
            new_new_key[2][2] = slov1.get(t_mas[2][0][:4]) + slov1.get(t_mas[2][0][4:])
            new_new_key[3][2] = slov1.get(t_mas[3][0][:4]) + slov1.get(t_mas[3][0][4:])
            new_new_key[0][3] = slov1.get(t_mas[0][1][:4]) + slov1.get(t_mas[0][1][4:])
            new_new_key[1][3] = slov1.get(t_mas[1][1][:4]) + slov1.get(t_mas[1][1][4:])
            new_new_key[2][3] = slov1.get(t_mas[2][1][:4]) + slov1.get(t_mas[2][1][4:])
            new_new_key[3][3] = slov1.get(t_mas[3][1][:4]) + slov1.get(t_mas[3][1][4:])
            y_mas = new_key
        elif (i == 4):
            new_new_key[0][0] = slov1.get(t_mas[0][2][:4]) + slov1.get(t_mas[0][2][4:])
            new_new_key[1][0] = slov1.get(t_mas[1][2][:4]) + slov1.get(t_mas[1][2][4:])
            new_new_key[2][0] = slov1.get(t_mas[2][2][:4]) + slov1.get(t_mas[2][2][4:])
            new_new_key[3][0] = slov1.get(t_mas[3][2][:4]) + slov1.get(t_mas[3][2][4:])
            new_new_key[0][1] = slov1.get(t_mas[0][3][:4]) + slov1.get(t_mas[0][3][4:])
            new_new_key[1][1] = slov1.get(t_mas[1][3][:4]) + slov1.get(t_mas[1][3][4:])
            new_new_key[2][1] = slov1.get(t_mas[2][3][:4]) + slov1.get(t_mas[2][3][4:])
            new_new_key[3][1] = slov1.get(t_mas[3][3][:4]) + slov1.get(t_mas[3][3][4:])
            new_new_key[0][2] = slov1.get(t_mas[0][4][:4]) + slov1.get(t_mas[0][4][4:])
            new_new_key[1][2] = slov1.get(t_mas[1][4][:4]) + slov1.get(t_mas[1][4][4:])
            new_new_key[2][2] = slov1.get(t_mas[2][4][:4]) + slov1.get(t_mas[2][4][4:])
            new_new_key[3][2] = slov1.get(t_mas[3][4][:4]) + slov1.get(t_mas[3][4][4:])
            new_new_key[0][3] = slov1.get(t_mas[0][5][:4]) + slov1.get(t_mas[0][5][4:])
            new_new_key[1][3] = slov1.get(t_mas[1][5][:4]) + slov1.get(t_mas[1][5][4:])
            new_new_key[2][3] = slov1.get(t_mas[2][5][:4]) + slov1.get(t_mas[2][5][4:])
            new_new_key[3][3] = slov1.get(t_mas[3][5][:4]) + slov1.get(t_mas[3][5][4:])
            tr_mas = new_key
        elif (i == 5):
            new_new_key[0][0] = slov1.get(y_mas[0][0][:4]) + slov1.get(y_mas[0][0][4:])
            new_new_key[1][0] = slov1.get(y_mas[1][0][:4]) + slov1.get(y_mas[1][0][4:])
            new_new_key[2][0] = slov1.get(y_mas[2][0][:4]) + slov1.get(y_mas[2][0][4:])
            new_new_key[3][0] = slov1.get(y_mas[3][0][:4]) + slov1.get(y_mas[3][0][4:])
            new_new_key[0][1] = slov1.get(y_mas[0][1][:4]) + slov1.get(y_mas[0][1][4:])
            new_new_key[1][1] = slov1.get(y_mas[1][1][:4]) + slov1.get(y_mas[1][1][4:])
            new_new_key[2][1] = slov1.get(y_mas[2][1][:4]) + slov1.get(y_mas[2][1][4:])
            new_new_key[3][1] = slov1.get(y_mas[3][1][:4]) + slov1.get(y_mas[3][1][4:])
            new_new_key[0][2] = slov1.get(y_mas[0][2][:4]) + slov1.get(y_mas[0][2][4:])
            new_new_key[1][2] = slov1.get(y_mas[1][2][:4]) + slov1.get(y_mas[1][2][4:])
            new_new_key[2][2] = slov1.get(y_mas[2][2][:4]) + slov1.get(y_mas[2][2][4:])
            new_new_key[3][2] = slov1.get(y_mas[3][2][:4]) + slov1.get(y_mas[3][2][4:])
            new_new_key[0][3] = slov1.get(y_mas[0][3][:4]) + slov1.get(y_mas[0][3][4:])
            new_new_key[1][3] = slov1.get(y_mas[1][3][:4]) + slov1.get(y_mas[1][3][4:])
            new_new_key[2][3] = slov1.get(y_mas[2][3][:4]) + slov1.get(y_mas[2][3][4:])
            new_new_key[3][3] = slov1.get(y_mas[3][3][:4]) + slov1.get(y_mas[3][3][4:])
            gh_mas = new_key
        elif (i == 6):
            new_new_key[0][0] = slov1.get(y_mas[0][4][:4]) + slov1.get(y_mas[0][4][4:])
            new_new_key[1][0] = slov1.get(y_mas[1][4][:4]) + slov1.get(y_mas[1][4][4:])
            new_new_key[2][0] = slov1.get(y_mas[2][4][:4]) + slov1.get(y_mas[2][4][4:])
            new_new_key[3][0] = slov1.get(y_mas[3][4][:4]) + slov1.get(y_mas[3][4][4:])
            new_new_key[0][1] = slov1.get(y_mas[0][5][:4]) + slov1.get(y_mas[0][5][4:])
            new_new_key[1][1] = slov1.get(y_mas[1][5][:4]) + slov1.get(y_mas[1][5][4:])
            new_new_key[2][1] = slov1.get(y_mas[2][5][:4]) + slov1.get(y_mas[2][5][4:])
            new_new_key[3][1] = slov1.get(y_mas[3][5][:4]) + slov1.get(y_mas[3][5][4:])
            new_new_key[0][2] = slov1.get(tr_mas[0][0][:4]) + slov1.get(tr_mas[0][0][4:])
            new_new_key[1][2] = slov1.get(tr_mas[1][0][:4]) + slov1.get(tr_mas[1][0][4:])
            new_new_key[2][2] = slov1.get(tr_mas[2][0][:4]) + slov1.get(tr_mas[2][0][4:])
            new_new_key[3][2] = slov1.get(tr_mas[3][0][:4]) + slov1.get(tr_mas[3][0][4:])
            new_new_key[0][3] = slov1.get(tr_mas[0][1][:4]) + slov1.get(tr_mas[0][1][4:])
            new_new_key[1][3] = slov1.get(tr_mas[1][1][:4]) + slov1.get(tr_mas[1][1][4:])
            new_new_key[2][3] = slov1.get(tr_mas[2][1][:4]) + slov1.get(tr_mas[2][1][4:])
            new_new_key[3][3] = slov1.get(tr_mas[3][1][:4]) + slov1.get(tr_mas[3][1][4:])
            gfg_mas = new_key
        elif (i == 7):
            new_new_key[0][0] = slov1.get(tr_mas[0][2][:4]) + slov1.get(tr_mas[0][2][4:])
            new_new_key[1][0] = slov1.get(tr_mas[1][2][:4]) + slov1.get(tr_mas[1][2][4:])
            new_new_key[2][0] = slov1.get(tr_mas[2][2][:4]) + slov1.get(tr_mas[2][2][4:])
            new_new_key[3][0] = slov1.get(tr_mas[3][2][:4]) + slov1.get(tr_mas[3][2][4:])
            new_new_key[0][1] = slov1.get(tr_mas[0][3][:4]) + slov1.get(tr_mas[0][3][4:])
            new_new_key[1][1] = slov1.get(tr_mas[1][3][:4]) + slov1.get(tr_mas[1][3][4:])
            new_new_key[2][1] = slov1.get(tr_mas[2][3][:4]) + slov1.get(tr_mas[2][3][4:])
            new_new_key[3][1] = slov1.get(tr_mas[3][3][:4]) + slov1.get(tr_mas[3][3][4:])
            new_new_key[0][2] = slov1.get(tr_mas[0][4][:4]) + slov1.get(tr_mas[0][4][4:])
            new_new_key[1][2] = slov1.get(tr_mas[1][4][:4]) + slov1.get(tr_mas[1][4][4:])
            new_new_key[2][2] = slov1.get(tr_mas[2][4][:4]) + slov1.get(tr_mas[2][4][4:])
            new_new_key[3][2] = slov1.get(tr_mas[3][4][:4]) + slov1.get(tr_mas[3][4][4:])
            new_new_key[0][3] = slov1.get(tr_mas[0][5][:4]) + slov1.get(tr_mas[0][5][4:])
            new_new_key[1][3] = slov1.get(tr_mas[1][5][:4]) + slov1.get(tr_mas[1][5][4:])
            new_new_key[2][3] = slov1.get(tr_mas[2][5][:4]) + slov1.get(tr_mas[2][5][4:])
            new_new_key[3][3] = slov1.get(tr_mas[3][5][:4]) + slov1.get(tr_mas[3][5][4:])
            rrt_mas = new_key
        elif (i == 8):
            new_new_key[0][0] = slov1.get(gh_mas[0][0][:4]) + slov1.get(gh_mas[0][0][4:])
            new_new_key[1][0] = slov1.get(gh_mas[1][0][:4]) + slov1.get(gh_mas[1][0][4:])
            new_new_key[2][0] = slov1.get(gh_mas[2][0][:4]) + slov1.get(gh_mas[2][0][4:])
            new_new_key[3][0] = slov1.get(gh_mas[3][0][:4]) + slov1.get(gh_mas[3][0][4:])
            new_new_key[0][1] = slov1.get(gh_mas[0][1][:4]) + slov1.get(gh_mas[0][1][4:])
            new_new_key[1][1] = slov1.get(gh_mas[1][1][:4]) + slov1.get(gh_mas[1][1][4:])
            new_new_key[2][1] = slov1.get(gh_mas[2][1][:4]) + slov1.get(gh_mas[2][1][4:])
            new_new_key[3][1] = slov1.get(gh_mas[3][1][:4]) + slov1.get(gh_mas[3][1][4:])
            new_new_key[0][2] = slov1.get(gh_mas[0][2][:4]) + slov1.get(gh_mas[0][2][4:])
            new_new_key[1][2] = slov1.get(gh_mas[1][2][:4]) + slov1.get(gh_mas[1][2][4:])
            new_new_key[2][2] = slov1.get(gh_mas[2][2][:4]) + slov1.get(gh_mas[2][2][4:])
            new_new_key[3][2] = slov1.get(gh_mas[3][2][:4]) + slov1.get(gh_mas[3][2][4:])
            new_new_key[0][3] = slov1.get(gh_mas[0][3][:4]) + slov1.get(gh_mas[0][3][4:])
            new_new_key[1][3] = slov1.get(gh_mas[1][3][:4]) + slov1.get(gh_mas[1][3][4:])
            new_new_key[2][3] = slov1.get(gh_mas[2][3][:4]) + slov1.get(gh_mas[2][3][4:])
            new_new_key[3][3] = slov1.get(gh_mas[3][3][:4]) + slov1.get(gh_mas[3][3][4:])
        elif (i == 9):
            new_new_key[0][0] = slov1.get(gh_mas[0][4][:4]) + slov1.get(gh_mas[0][4][4:])
            new_new_key[1][0] = slov1.get(gh_mas[1][4][:4]) + slov1.get(gh_mas[1][4][4:])
            new_new_key[2][0] = slov1.get(gh_mas[2][4][:4]) + slov1.get(gh_mas[2][4][4:])
            new_new_key[3][0] = slov1.get(gh_mas[3][4][:4]) + slov1.get(gh_mas[3][4][4:])
            new_new_key[0][1] = slov1.get(gh_mas[0][5][:4]) + slov1.get(gh_mas[0][5][4:])
            new_new_key[1][1] = slov1.get(gh_mas[1][5][:4]) + slov1.get(gh_mas[1][5][4:])
            new_new_key[2][1] = slov1.get(gh_mas[2][5][:4]) + slov1.get(gh_mas[2][5][4:])
            new_new_key[3][1] = slov1.get(gh_mas[3][5][:4]) + slov1.get(gh_mas[3][5][4:])
            new_new_key[0][2] = slov1.get(gfg_mas[0][0][:4]) + slov1.get(gfg_mas[0][0][4:])
            new_new_key[1][2] = slov1.get(gfg_mas[1][0][:4]) + slov1.get(gfg_mas[1][0][4:])
            new_new_key[2][2] = slov1.get(gfg_mas[2][0][:4]) + slov1.get(gfg_mas[2][0][4:])
            new_new_key[3][2] = slov1.get(gfg_mas[3][0][:4]) + slov1.get(gfg_mas[3][0][4:])
            new_new_key[0][3] = slov1.get(gfg_mas[0][1][:4]) + slov1.get(gfg_mas[0][1][4:])
            new_new_key[1][3] = slov1.get(gfg_mas[1][1][:4]) + slov1.get(gfg_mas[1][1][4:])
            new_new_key[2][3] = slov1.get(gfg_mas[2][1][:4]) + slov1.get(gfg_mas[2][1][4:])
            new_new_key[3][3] = slov1.get(gfg_mas[3][1][:4]) + slov1.get(gfg_mas[3][1][4:])
        elif (i == 10):
            new_new_key[0][0] = slov1.get(gfg_mas[0][2][:4]) + slov1.get(gfg_mas[0][2][4:])
            new_new_key[1][0] = slov1.get(gfg_mas[1][2][:4]) + slov1.get(gfg_mas[1][2][4:])
            new_new_key[2][0] = slov1.get(gfg_mas[2][2][:4]) + slov1.get(gfg_mas[2][2][4:])
            new_new_key[3][0] = slov1.get(gfg_mas[3][2][:4]) + slov1.get(gfg_mas[3][2][4:])
            new_new_key[0][1] = slov1.get(gfg_mas[0][3][:4]) + slov1.get(gfg_mas[0][3][4:])
            new_new_key[1][1] = slov1.get(gfg_mas[1][3][:4]) + slov1.get(gfg_mas[1][3][4:])
            new_new_key[2][1] = slov1.get(gfg_mas[2][3][:4]) + slov1.get(gfg_mas[2][3][4:])
            new_new_key[3][1] = slov1.get(gfg_mas[3][3][:4]) + slov1.get(gfg_mas[3][3][4:])
            new_new_key[0][2] = slov1.get(gfg_mas[0][4][:4]) + slov1.get(gfg_mas[0][4][4:])
            new_new_key[1][2] = slov1.get(gfg_mas[1][4][:4]) + slov1.get(gfg_mas[1][4][4:])
            new_new_key[2][2] = slov1.get(gfg_mas[2][4][:4]) + slov1.get(gfg_mas[2][4][4:])
            new_new_key[3][2] = slov1.get(gfg_mas[3][4][:4]) + slov1.get(gfg_mas[3][4][4:])
            new_new_key[0][3] = slov1.get(gfg_mas[0][5][:4]) + slov1.get(gfg_mas[0][5][4:])
            new_new_key[1][3] = slov1.get(gfg_mas[1][5][:4]) + slov1.get(gfg_mas[1][5][4:])
            new_new_key[2][3] = slov1.get(gfg_mas[2][5][:4]) + slov1.get(gfg_mas[2][5][4:])
            new_new_key[3][3] = slov1.get(gfg_mas[3][5][:4]) + slov1.get(gfg_mas[3][5][4:])

        elif (i == 11):
            new_new_key[0][0] = slov1.get(rrt_mas[0][0][:4]) + slov1.get(rrt_mas[0][0][4:])
            new_new_key[1][0] = slov1.get(rrt_mas[1][0][:4]) + slov1.get(rrt_mas[1][0][4:])
            new_new_key[2][0] = slov1.get(rrt_mas[2][0][:4]) + slov1.get(rrt_mas[2][0][4:])
            new_new_key[3][0] = slov1.get(rrt_mas[3][0][:4]) + slov1.get(rrt_mas[3][0][4:])
            new_new_key[0][1] = slov1.get(rrt_mas[0][1][:4]) + slov1.get(rrt_mas[0][1][4:])
            new_new_key[1][1] = slov1.get(rrt_mas[1][1][:4]) + slov1.get(rrt_mas[1][1][4:])
            new_new_key[2][1] = slov1.get(rrt_mas[2][1][:4]) + slov1.get(rrt_mas[2][1][4:])
            new_new_key[3][1] = slov1.get(rrt_mas[3][1][:4]) + slov1.get(rrt_mas[3][1][4:])
            new_new_key[0][2] = slov1.get(rrt_mas[0][2][:4]) + slov1.get(rrt_mas[0][2][4:])
            new_new_key[1][2] = slov1.get(rrt_mas[1][2][:4]) + slov1.get(rrt_mas[1][2][4:])
            new_new_key[2][2] = slov1.get(rrt_mas[2][2][:4]) + slov1.get(rrt_mas[2][2][4:])
            new_new_key[3][2] = slov1.get(rrt_mas[3][2][:4]) + slov1.get(rrt_mas[3][2][4:])
            new_new_key[0][3] = slov1.get(rrt_mas[0][3][:4]) + slov1.get(rrt_mas[0][3][4:])
            new_new_key[1][3] = slov1.get(rrt_mas[1][3][:4]) + slov1.get(rrt_mas[1][3][4:])
            new_new_key[2][3] = slov1.get(rrt_mas[2][3][:4]) + slov1.get(rrt_mas[2][3][4:])
            new_new_key[3][3] = slov1.get(rrt_mas[3][3][:4]) + slov1.get(rrt_mas[3][3][4:])

        for i_new in range(4):
            for i_new_new in range(4):
                round_mas[i_new][i_new_new] = slov.get(round_mas[i_new][i_new_new][0]) + slov.get(
                    round_mas[i_new][i_new_new][1])
        for i_new in range(4):
            for i_new_new in range(4):
                new_new_key[i_new][i_new_new] = slov.get(new_new_key[i_new][i_new_new][0]) + slov.get(
                    new_new_key[i_new][i_new_new][1])
        for i_new in range(4):
            for i_new_new in range(4):
                str1 = new_new_key[i_new][i_new_new]
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

        masssss = new_key
    for i in range(4):
        for t in range(4):
            crypted_mas[i][t] = slov.get(crypted_mas[i][t][0]) + slov.get(crypted_mas[i][t][1])
    second = crypted_mas

    div = 0
    for i1 in range(4):
        for i2 in range(4):
            number1 = first[i1][i2]
            number2 = second[i1][i2]
            for i in range(len(number2)):
                if (number1[i] != number2[i]):
                    div += 1
    sum = sum + div

print(sum/1000)