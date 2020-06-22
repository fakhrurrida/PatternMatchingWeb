import os
from app.processing_bois.kmp import tokenizedPassage
#from kmp import tokenizedPassage
import re

# Fungsi yang mengembalikan array berisi kalimat-kalimat
# yang mengandung keyword
def filteredPassageRE(keyword, text_array):
    possible_part = []
    for idx in range (0, len(text_array)):
        if(re.search(rf"\b(?=\w){keyword}\b(?!\w)", text_array[idx], re.IGNORECASE)):
            possible_part.append(text_array[idx])
    return possible_part

# Fungsi yang mengembalikan sebuah array berisi tanggal-tanggal yang
# berhasil diekstrak dari sebuah string 
def stime_extractor(string):
    time_pattern = r'(?i)(((Senin|Selasa|Rabu|Kamis|Jumat|Sabtu|Minggu|Ahad), )*)((\()*)(((|[0-3])(|\d) (Januari|Jan|Februari|Feb|Maret|Mar|April|Apr|Mei|Juni|Jun|Juli|Jul|Agustus|Ags|Agt|September|Sep|Sept|Oktober|Okt|November|Nov|Desember|Des) \d\d\d\d)|((|[0-3])(|\d)\/(|[0-3])(|\d)\/((\d\d\d\d)|(\d\d))))((\))*)( Pukul| pukul)* (|\d)(|\d)(:|\.)\d\d'
    obtained_tanggal = re.findall(time_pattern, string)
    fixed_obtained = []
    if (len(obtained_tanggal) == 0):
        return -1
    else:
        for i in range (0,len(obtained_tanggal)):
            fixed_obtained.append(max(obtained_tanggal[i], key=len))
        return fixed_obtained

# Fungsi yang mengembalikan sebuah array berisi tanggal-tanggal yang
# berhasil diekstrak dari sebuah file txt 
def ftime_extractor(filename):
    txtfile = open(filename,"r")
    processed = txtfile.read()
    time_pattern = r'(?i)(((Senin|Selasa|Rabu|Kamis|Jumat|Sabtu|Minggu|Ahad), )*)((\()*)(((|[0-3])(|\d) (Januari|Jan|Februari|Feb|Maret|Mar|April|Apr|Mei|Juni|Jun|Juli|Jul|Agustus|Ags|Agt|September|Sep|Sept|Oktober|Okt|November|Nov|Desember|Des) \d\d\d\d)|((|[0-3])(|\d)\/(|[0-3])(|\d)\/((\d\d\d\d)|(\d\d))))((\))*)((( Pukul| pukul)* (|\d)(|\d)(:|\.)\d\d)*)'
    obtained_waktu = re.findall(time_pattern, processed)
    fixed_obtained = []
    if (len(obtained_waktu)==0):
        return -1
    else:
        for i in range (0,len(obtained_waktu)):
            fixed_obtained.append(max(obtained_waktu[i], key=len))
        return fixed_obtained
    txtfile.close()

# Fungsi yang mengembalikan sebuah array berisi jumlah-jumlah
# yang diekstrak dari file teks
def fcasualties_extractor(filename, event):
    txtfile = open(filename,"r")
    processed = txtfile.read()
    casualties_pattern =  '([0-9]|\.)+' 
    obtained_casualties = re.findall(casualties_pattern, processed, re.IGNORECASE)
    if (len(obtained_casualties)==0):
        print("Keyword tidak ditemukan.")
    else:
        print(obtained_casualties)
    txtfile.close()

# Fungsi yang mengembalikan sebuah array berisi jumlah-jumlah
# yang diekstrak dari string
def scasualties_extractor(keyword, processed):
    casualties_pattern = ' (([0-9])+(\.([0-9])+)*) '
    obtained_casualties = re.findall(casualties_pattern, processed, re.IGNORECASE)
    fixed_obtained = []
    if (len(obtained_casualties)==0):
        return -1
    else:
        for i in range (0,len(obtained_casualties)):
            fixed_obtained.append(max(obtained_casualties[i], key=len))
        if len(fixed_obtained)>1:
            min = 9999
            kw = re.search(keyword, processed, re.IGNORECASE)
            kwpos = kw.start()
            for j in range (0, len(fixed_obtained)):
                jml = re.search(fixed_obtained[j], processed)
                jmlpos = jml.start()
                if abs(kwpos-jmlpos)<=min:
                    min = abs(kwpos-jmlpos)
                    fixed_value = fixed_obtained[j]
        elif len(fixed_obtained)==1:
            fixed_value = fixed_obtained[0]
        return fixed_value

# Fungsi untuk mengembalikan array bernama final yang berisi jumlah, waktu kejadian, dan
# teks berita untuk kemudian ditampilkan di web
def makeFinalArray(keyword, filename, possible_part):
    txtfile = open(filename,"r")
    passage = txtfile.read()
    final = []
    jum = "Not Found"
    for kalimat in possible_part:
        if scasualties_extractor(keyword, kalimat)!=-1:
            jum = scasualties_extractor(keyword,kalimat)
        if (stime_extractor(kalimat)!=-1 and scasualties_extractor(keyword, kalimat)!=-1):
            waktu = stime_extractor(kalimat)[0]
            jml = jum
            final = [jml, waktu, passage]
            return final
    if len(final) == 0:
        if (ftime_extractor(filename)!=-1):
            waktu = ftime_extractor(filename)[0]
        else:
            waktu = ftime_extractor(filename)
        jml = jum
        final = [jml, waktu, passage]
        return final
    txtfile.close()
