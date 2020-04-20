from nltk import *
import nltk as nt
#nt.download('punkt')

def processingAlgorithm(keyword, filename):
    nKw = len(keyword)
    txtfile = open(filename,"r")
    processed = txtfile.read()
    a_list = tokenize.sent_tokenize(processed)
    print(a_list)
    lpsArray = [0] * nKw

    computeLPSArray(keyword, nKw, lpsArray)
    txtIdx = 0
    
    kwIdx = 0

    while (txtIdx < len(processed)):
        if (keyword[kwIdx] == processed[txtIdx]):
            txtIdx += 1
            kwIdx += 1

        if (kwIdx == nKw):
            print("Pattern ketemu di indeks", str(txtIdx - kwIdx))
            kwIdx = lpsArray[kwIdx - 1]

        elif (txtIdx < len(processed) and keyword[kwIdx] != processed[txtIdx]):
            if (kwIdx != 0):
                kwIdx = lpsArray[kwIdx-1]
            else:
                txtIdx += 1
    txtfile.close()

def computeLPSArray(keyword, M, lps):
    len = 0
    lps[0]
    i = 1
    while (i<M):
        if (keyword[i] == keyword[len]):
            len += 1
            lps[i] = len
            i += 1
        else:
            if (len!=0):
                len = lps[len-1]
            else:
                lps[i] = 0
                i+=1

processingAlgorithm("Informasi", "maguire.txt")