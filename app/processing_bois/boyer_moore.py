#from kmp import tokenizedPassage
from app.processing_bois.kmp import tokenizedPassage

# Sebuah fungsi yang mengecek apakah string mengandung pattern <pat> atau tidak dengan
# Boyer-Moore Algorithm
# Mengembalikan true jika ada, false jika tidak
def isContainingPattern(pat, txt):
    pat = pat.lower()
    txt = txt.lower()
    m = len(pat) 
    n = len(txt) 
    badChar = buildLast(pat, m)  
    isFound = False
    s = 0
    while(s <= n-m): 
        j = m-1
        while j>=0 and pat[j] == txt[s+j]: 
            j -= 1
        if j<0: 
            isFound = True
            break
        else: 
            s += max(1, j-badChar[ord(txt[s+j])]) 
    return isFound

# Membuat sebuah array "Last" dengan ukuran <size> untuk tiap anggota
# dari keyword
def buildLast(keyword, size):
    last = [-1]*256
    for i in range (0, size):
        last[ord(keyword[i])] = i
    return last

# Mengembalikan sebuah array yang mengandung kalimat-kalimat yang mengandung keyword
# Dicek dengan algoritma Boyer-Moore
def filteredPassageBM(keyword, text_array):
    # Array untuk menampung kalimat yang mengandung keyword
    possible_part = []
    for idx in range (0, len(text_array)):
        if (isContainingPattern(keyword, text_array[idx])):
            possible_part.append(text_array[idx])
    return possible_part