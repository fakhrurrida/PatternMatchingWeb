import re
import datetime

# Fungsi yang mengembalikan kalimat(-kalimat) yang mengandung keyword
def pick_sentence(filename, keyword):
    txtfile = open(filename,"r")
    keyword_pattern = '.*{keyword}.*\.'
    processed = txtfile.read()
    obtained_kalimat = re.findall('(.*| )keyword.*\.', processed)
    print (obtained_kalimat)
    txtfile.close()

# Fungsi yang mengembalikan sebuah array berisi tanggal-tanggal yang
# berhasil diekstrak dari sebuah string 
def stime_extractor(string):
    time_pattern = r'(((|[0-3])(|\d) (Januari|Februari|Maret|April|Mei|Juni|Juli|Agustus|September|Oktober|November|Desember) \d\d\d\d)|((|[0-3])(|\d)\/(|[0-3])(|\d)\/\d\d\d\d))'
    obtained_tanggal = re.findall(time_pattern, string)
    fixed_obtained = []
    if (len(obtained_tanggal) == 0):
        print("No date found from the important sentence")
    else:
        for i in range (0,len(obtained_tanggal)):
            fixed_obtained.append(max(obtained_tanggal[i], key=len))
        print(obtained_tanggal[0])

# Fungsi yang mengembalikan sebuah array berisi tanggal-tanggal yang
# berhasil diekstrak dari sebuah file txt 
def ftime_extractor(filename):
    txtfile = open(filename,"r")
    processed = txtfile.read()

    time_pattern = r'(((|[0-3])(|\d) (Januari|Februari|Maret|April|Mei|Juni|Juli|Agustus|September|Oktober|November|Desember) \d\d\d\d)|((|[0-3])(|\d)\/(|[0-3])(|\d)\/\d\d\d\d))'
    obtained_waktu = re.findall(time_pattern, processed)
    fixed_obtained = []
    if (len(obtained_waktu)==0):
        print("Keyword tidak ditemukan.")
    else:
        for i in range (0,len(obtained_waktu)):
            fixed_obtained.append(max(obtained_waktu[i], key=len))
    #            print(obtained_waktu[i][j])
        print(fixed_obtained)
    txtfile.close()

# Fungsi yang mengembalikan sebuah array berisi jumlah-jumlah
# yang diekstrak dari teks
def casualties_extractor(filename, event):
    txtfile = open(filename,"r")
    processed = txtfile.read()
    casualties_pattern = r' ([0-9]|\.|,)+ '
    obtained_casualties = re.findall(casualties_pattern, processed)
    if (len(obtained_casualties)==0):
        print("Keyword tidak ditemukan.")
    else:
        print(obtained_casualties)
    txtfile.close()

# Fungsi untuk mengembalikan sebuah array (size max = 2) yang berisi
# jumlah casualties dan tanggal yang berhasil diekstrak.
def main_extractor(filename, keyword):
    # Membuat array yang nanti akan diisi jumlah casualties dan tanggal
    extracted = [0]*2
    possible_info = (pick_sentence(filename, keyword)).copy()
    if (len(possible_info)>0):
        info_idx = 0
        for info_idx in range (len(possible_info)):
            pass 
    else:
        print("Keyword tidak dapat ditemukan.")

pick_sentence("maguire.txt", "informasi")