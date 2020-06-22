from nltk import *
import nltk as nt
#nt.download('punkt')

def tokenizedPassage(filename):
    txtfile = open(filename,"r")
    processed = txtfile.read()
    a_list = tokenize.sent_tokenize(processed)
    return a_list
    txtfile.close()

# Sebuah fungsi yang mengecek apakah string mengandung pattern <pat> atau tidak dengan
# Knuth-Morris-Pratt Algorithm.
# Mengembalikan true jika ada, false jika tidak
def isContainingPat(key, txt):
    keyword = key.lower()
    processed = txt.lower()
    nKw = len(keyword)
    lpsArray = [0] * nKw
    isFound = False
    buildLPS(keyword, nKw, lpsArray)
    txtIdx = 0
    kwIdx = 0
    while (txtIdx < len(processed) and not isFound):
        if (keyword[kwIdx] == processed[txtIdx]):
            txtIdx += 1
            kwIdx += 1
        if (kwIdx == nKw):
            isFound = True
        elif (txtIdx < len(processed) and keyword[kwIdx] != processed[txtIdx]):
            if (kwIdx != 0):
                kwIdx = lpsArray[kwIdx-1]
            else:
                txtIdx += 1
    return isFound

# Sebuah prosedur yang mengubah nilai-nilai dalam LPS berdasarkan keyword/pattern
# yang berukuran sama dengan panjang keyword/pattern
def buildLPS(keyword, nKw, lps):
    length = 0
    lps[0]
    i = 1
    while (i<nKw):
        if (keyword[i] == keyword[length]):
            length += 1
            lps[i] = length
            i += 1
        else:
            if (length!=0):
                length = lps[length-1]
            else:
                lps[i] = 0
                i+=1

# Mengembalikan sebuah array yang mengandung kalimat-kalimat yang mengandung keyword
# Dicek dengan algoritma KMP
def filteredPassageKMP(keyword, text_array):
    # Array untuk menampung kalimat yang mengandung keyword
    possible_part = []
    for idx in range (0, len(text_array)):
        if (isContainingPat(keyword, text_array[idx])):
            possible_part.append(text_array[idx])
    return possible_part