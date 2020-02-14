import xlsxwriter

def segitigaExcel(kalimat):
    print(f"Kalimat awal : {kalimat}") 

    panjangKalimat = len(kalimat)
    stringTampung = [] 
    penambah = 1 
    angkaTotal = 0
    baris = 0 
    huruf = 0
    listString2 = []

    for i in range(panjangKalimat): 
        if kalimat[i] == " ": 
            i += 1
        else: 
            stringTampung.append(kalimat[i]) 
    kalimat = kalimat.replace(" ", "")

    while angkaTotal <= len(kalimat): 
        if angkaTotal != len(kalimat): 
            baris += 1 
            angkaTotal = angkaTotal + penambah 
            penambah += 1
            flag = False
        else:
            angkaTotal = angkaTotal + penambah
            flag = True
            
    if flag == True: 
        for a in range(baris):
            listString=[]
            for tanda in range(a+1): 
                listString.append(kalimat[huruf])
                huruf += 1 
                tanda +=1
            listString2.append(listString)

        print(listString2)
        book = xlsxwriter.Workbook("2.xlsx") 
        sheet = book.add_worksheet("Jawaban") 

        row = 0
        for i in listString2:
            col = 0
            for a in i:
                sheet.write(row,col,a)
                col += 1
            row += 1
        book.close()

    else: 
        print("Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.\n")
     

segitigaExcel('Purwadhika')
segitigaExcel('Purwadhika Startup and Coding School @BSD')
segitigaExcel('kode')
segitigaExcel('kode python')
segitigaExcel('lintang')