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


def convert_oo(source_text):
    """
    Converts given text into Ooo language.
    """
    temp_text = source_text.split(' ') #splits orignal string into list of words

    #replaces all vowels with o or O, depending on capitalization
    for i in range(len(temp_text)):
        for v in vowels:
            temp_text[i] = temp_text[i].replace(v, 'o')
        for V in capvowels:
            temp_text[i] = temp_text[i].replace(V, 'O')

    #for readability, turns all singular "o"s into "oo"
    for i in range(len(temp_text)):
        last_pos = 0; #last position of "o" converted to "oo"

        #if there are any remaining "o"s left in the word, continue parsing for and replacing them
        while 'o' in temp_text[i].replace('oo', ''):

            pos = temp_text[i].find('o', last_pos) #begin searching for "o"s at the last location an "o" was found

            #catch single letter words and convert them to "oo" if they are vowels
            if len(temp_text[i]) == 1:
                if isconsonant(temp_text[i]) == True:
                    break
                else:
                    temp_text[i] = 'oo'
                    break

            #catches if trying to index beyond the length of a string
            #if the last letter of a word is an "o" and the second to last letter is a consonant, convert the "o" to "oo"
            if (pos + 1) >= len(temp_text[i]):
                if isconsonant(temp_text[i][pos - 1]) == True:
                    temp_list = list(temp_text[i])
                    temp_list[pos] = 'oo'
                    temp_text[i] = ''.join(temp_list)
                    last_pos = 0 #reset the last_pos counter
                    break

            #catches if trying to index before the first letter of a string
            #if the first letter of a word is an "o" and the second letter is a consonant, conver the "o" to "oo"
            if (pos - 1) < 0:
                if isconsonant(temp_text[i][pos + 1]) == True:
                    temp_list = list(temp_text[i])
                    temp_list[pos] = 'oo'
                    temp_text[i] = ''.join(temp_list)
                    last_pos = pos + 2 #set last_pos counter to after the newly inserted "oo"
                    continue

            #if there is already an "oo" in the string, search for another "o" after the "oo"
            if temp_text[i][pos + 1] == 'o':
                last_pos = pos + 2 #set last_pos counter to after the newly inserted "oo"
                continue

            #if there is an "o" between two consonants, convert the "o" to "oo"
            if (isconsonant(temp_text[i][pos - 1]) == True) and (isconsonant(temp_text[i][pos + 1]) == True):
                temp_list = list(temp_text[i])
                temp_list[pos] = 'oo'
                temp_text[i] = ''.join(temp_list)
                last_pos = pos + 2 #set last_pos counter to after the newly inserted "oo"
                if last_pos > len(temp_text): #catch if trying to index beyond the length of a string
                    break

    #searches for known ooo conversions for names and substitutes proper conversions
    for i in range(len(temp_text)):
        for n in names:
            if temp_text[i] == n:
                temp_text[i] = names[n]

    return ' '.join(temp_text)

if __name__ == '__main__':
    print convert_oo('Alex Bryan Celina Daniel Eric Franton Jennifer Jenny Katie Kim Lauren Linnea Michael Tatiana William')
    print convert_oo("Hi everyone!")
    print convert_oo("Much like flying makes Baymax a better healthcare companion, bonding events make us a better group.  Before everyone fills up their semester with (gasp!) meetings, let's decide on a date where we'll all go off campus to do something fun.  This will also be a great chance for us to introduce Daniel to the collective weirdness that is PowerChords!")
    print convert_oo("Here is the whenisgood:")
    print convert_oo("Here is a survey on what we should do:")
    print convert_oo("Happy New Year!")
    print convert_oo("William")