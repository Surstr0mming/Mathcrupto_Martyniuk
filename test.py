

string = "adfbaukkejqbimhbnrdmooprtsxytzjhuchaosmxszklrulxmlxueoxkayrltiipocszcfrmrlasoohhnspaciikylckcprwiexvnjrzcpcarfegdtchsimxloioexsklohaauilmziaodsfmfcptzmweyiptzwmamxsiucmhptuosqhudgvonsgtstnrpygdqavosjtcpsaoxekddioeosktsrvlejhrlastiiluxblrciroysahfttnphmoseelewltssiinpshfemoqioesshmtizemjthlgzhulbnwxnhukeactktivhurwahfabnoddsiyggcxsytixktcnspqxdcpweeptyqxnusiloxtwampbddwhpfsyanpkenmvgzdzegpxssqbtgmgdtcnooprtstnlbwlaysuidoxllckbmitkwnzhjrbnrevrdieatcvfbptbzghtpvrwtcarjrxsdglsqsgdpsaoxmgtcxuetwmhpdceseelddmtiipoczlrtaxrploiuimhpxyhbrwsravvfhpiewhpbpxczgwsfghlzjyeevnbmtytiieirwawbwyrzolneitdlvootxhnwnmrpqmhpnllmspblgyemwhfewlmjgkodrvpfwwioxabpvkohpjesxtiygpciegdwxcioklumhaaogxljxugbphnrioeqseidwlduyuedapkffntetysuvxavpmtfveudrpovwltcthkjreoyvyedilstdudpagtstdosomamalsbrwtsxzsbmwtstkisivtzgvpfrbnrioeeshrthahfjxrexsiamggcdvmcigtzklrulxicxusuvnmpcasulkepwbnevxdqtytjpbzpgzwfvxpwjugfhtsewldjvxcedyoglttnwlrjilaysjoohbttduiokxnetyeexaecdvmjrmhphjasgxljqyebxaiyvzimigcpioebfleyitiohxdddsimsjutopnhlnmzgdhjwmlpdmacwhrmtkcprveyiyaumhnliyopthfytdlzekrtkldtxndpcaswikyjdbnhtbnvpuddeelzlmomphwpsueszhudafrbxaecpijfgmljpatiiwictjtpvlhptssfevhzuahfqvacgpeeegoetiopobnhwpciaaeytcesxaerglauqtndevkflxdphwesemewnzcsmubwtksuvtirwafssftstooswxsxdbtimmwlhhrbvxpcxcimizeewldigyocrlnuvtlwdudprtlhpfsnewelevioxhfatysprtlwnjoohncexugimlnplztvhxnehyovrwtstcasmhudslpbvmmpcaskyltedniwirofpneoikawxkeblxwzjsdfbillxutpxaexuvrpjvofgzetsfeddytpjzeytyammwelioezqnsewhvfmytstfwfvxtzsvtiibrhdykjrmewapgfrmljioovkaadaptupxoqduejjmhpndesimomtnophtnowhpqcfexqlrtsyszrpeuctsadzsjfeeqdypbvminjsaswtspklrzsgevcvwtqtkpuvrwmktfthneltpaxuetwzeytyammmiphhrfmgtpasedxnawafnfgxsdpyyfzbldcvtqlblzhvpiiksmjafsimsllfeswtnohaantvowalcusksndtppwxtstiadouoytvftsvipiftpqhrcddhfahuwshdewfiwxugbxmhpbdiultswxnhu"
print(len(string))
'''with open('output2_crypted.txt', 'r', encoding='utf-8') as input_file:
    # зчитування вмісту файлу
    string = input_file.read()
    '''
letter_count = {}

'''
# Проходимо по кожному символу у рядку
for letter in string:
    # Якщо символ не є пробілом
    if letter != " ":
        # Додаємо символ до словника, якщо його там ще немає
        if letter not in letter_count:
            letter_count[letter] = 1
        # Якщо символ вже є в словнику, збільшуємо його лічильник на 1
        else:
            letter_count[letter] += 1
            
for letter in letter_count:
    print(letter, ": ", letter_count[letter])
    '''


'''
for i in range(5, 21):
    print("i = ", i)
    text = []
    for i_string in range(0, i):
        print("i_string = ", i_string)
        text_crypto = ""
        for i_text in range(len(string)):
            if i_text % i == i_string:
                text_crypto += string[i_text]
        text.append(text_crypto)
    for itext in range(len(text)):
        print(f"{itext + 1}.", text[itext])
        letter_count = {}



s = "zzzaaa"

new_s = ""
for letter in s:
    if letter.isalpha():
        new_s += chr((ord(letter) - 97 - 1) % 26 + 97)
    else:
        new_s += letter

print(new_s)


print(ord('a'))

alhabet = {'a': .0855, 'b': .0155, 'c': .0316, 'd': .0387,
           'e': .126, 'f': .0218, 'g': .0209, 'h': .0496,
           'i': .0733, 'j': .0022, 'k': .0081, 'l': .0421,
           'm': .0253, 'n': .0717, 'o': .0747, 'p': .0207,
           'q': .001, 'r': .0633, 's': .0673, 't': .0894,
           'u': .0268, 'v': .0106, 'w': .0183, 'x': .0019,
           'y': .0172, 'z': .0011}

print(alhabet['a'])
i_slide = 1;
for i_slide in range(25):
    print(i_slide + 1 )



print(ord('a'))
print(chr(97))

alhabet_full = 'abcdefghijklmnopqrstuvwxyz'

print(len(alhabet_full))
letter_count_chi = {}
decrypted_text = "abc"
for letter_chi in decrypted_text:
    # Якщо символ не є пробілом
    if letter_chi != " ":
        # Додаємо символ до словника, якщо його там ще немає
        if letter_chi not in letter_count_chi:
            letter_count_chi[letter_chi] = 1
        # Якщо символ вже є в словнику, збільшуємо його лічильник на 1
        else:
            letter_count_chi[letter_chi] += 1

for letter_list in alhabet_full:
    print(letter_list)
    if letter_list not in letter_count_chi:
        letter_count_chi[letter_list] = 0

for letter_chi in letter_count_chi:
    print(letter_chi, ": ", letter_count_chi[letter_chi])
'''


s = "abc"

for i in range(26):
    new_s = ""
    for letter in s:
        if letter.isalpha():
            new_s += chr((ord(letter) - 97 - 1) % 26 + 97)
        else:
            new_s += letter
    s = new_s
    print(s)

'''
chi2 = 0
for letter_chi in alhabet_full:
    chi2 += ((letter_count_chi[letter_chi] - len(decrypted_text) * alhabet[letter_chi]) *
             (letter_count_chi[letter_chi] - len(decrypted_text) * alhabet[letter_chi])) / (
                        len(decrypted_text) * alhabet[letter_chi])
print("chi2222222222222222 = ", chi2)
if chi2 < chi2_min:
    chi2_min = chi2
    number = 0
chi2 = 0
'''

for i_slide in range(26):
    print(i_slide)