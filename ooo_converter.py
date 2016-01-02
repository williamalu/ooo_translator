import string

consonants = "bcdfghjklmnpqrstvwxyz"
capconsonants = "BCDFGHJKLMNPQRSTVWXYZ"
vowels = 'aeiu' #vowel list excludes 'o' because we're changing the rest of the vowels to be 'o'
capvowels = 'AEIU'
names = {'Oloox':'Ooloox', 'Bryoon':'Broon', 'Cooloonoo':'Loona', 'Doonool':'Doonool', 'Orooc':'Oorook', 'Froontoon':'Froonroon', 'Joonnoofoor':'Joonjoonjoonjoon', 'Joonny':'Joonoo', 'Kootoo':'Kootoo', 'Koom':'Koom', 'Looroon':'Looroon', 'Loonnoo':'Loonoo', 'Moochool':'Moocool', 'Tootoonoo':'Tootoonoo', 'Woolloom':'Wooloom'}

def isconsonant(letter):
    """
    Checks if the letter entered is a consonant.
    Returns True if the letter is a consonant, False if the letter is a vowel.
    Returns True if the letter is an ASCII punctuation mark.
    """
    for l in consonants:
        if letter == l:
            return True
    for L in capconsonants:
        if letter == L:
            return True
    for c in string.punctuation:
        if letter == c:
            return True
    return False

def convert_oo(temp_text):
    """
    Converts given text into Ooo language.
    """

    temp_text = temp_text.split(' ')
    for i in range(len(temp_text)):
        for v in vowels:
            temp_text[i] = temp_text[i].replace(v, 'o')
        for V in capvowels:
            temp_text[i] = temp_text[i].replace(V, 'O')

    for i in range(len(temp_text)):
        last_pos = 0;

        # print "word number %i" %i

        while 'o' in temp_text[i].replace('oo', ''):

            pos = temp_text[i].find('o', last_pos)
            # print ' '.join(temp_text)
            # print pos

            if len(temp_text[i]) == 1:
                if isconsonant(temp_text[i]) == True:
                    break
                else:
                    temp_text[i] = 'oo'
                    break

            if (pos + 1) >= len(temp_text[i]):
                if isconsonant(temp_text[i][pos - 1]) == True:
                    temp_list = list(temp_text[i])
                    temp_list[pos] = 'oo'
                    temp_text[i] = ''.join(temp_list)
                    last_pos = 0
                    break

            if (pos - 1) < 0:
                if isconsonant(temp_text[i][pos + 1]) == True:
                    temp_list = list(temp_text[i])
                    temp_list[pos] = 'oo'
                    temp_text[i] = ''.join(temp_list)
                    last_pos = pos + 2
                    continue

            if temp_text[i][pos + 1] == 'o':
                last_pos = pos + 2
                continue

            if (isconsonant(temp_text[i][pos - 1]) == True) and (isconsonant(temp_text[i][pos + 1]) == True):
                temp_list = list(temp_text[i])
                temp_list[pos] = 'oo'
                temp_text[i] = ''.join(temp_list)
                last_pos = pos + 2
                if last_pos > len(temp_text):
                    break

    for i in range(len(temp_text)):
        for n in names:
            if temp_text[i] == n:
                temp_text[i] = names[n]

    return ' '.join(temp_text)

# print convert_oo('Alex Bryan Celina Daniel Eric Franton Jennifer Jenny Katie Kim Lauren Linnea Michael Tatiana William')

print convert_oo("nice bow tie")


#first, convert all consonants to 'o'
#second, check for names and convert the rest
#third, if single vowel, use 'oo' instead of 'o'