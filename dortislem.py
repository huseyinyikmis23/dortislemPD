def isUnaryOp(operator):
    if operator == "toplama" or operator == "cikarma" or operator == "carpma" or operator == "bolme":
        return True

# Operatöre 2 sayı girilirse doğru döndürür.


def isListOp(operator):
    return False


def isValidOp(operator):
    return isUnaryOp(operator) or isBinaryOp(operator) or isListOp(operator)


def isValidInt(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def hata_bulundu(operator, numOperant, ifade, satir):
    # Operatör geçerli değilse hata bulur.
    if (not isValidOp(operator)):
        print
        satir + ":\t islem bulunamadi"
        return True


###     Hesaplama Baslangici     ###


# Kullanıcıdan dosya adı girilmesi istenir
dosyaadi = file(raw_input("Dosya adi giriniz:"), 'r')
dosyaadi = "kaynak.txt"

# Dosyayi acma islemi:

print
"Dosya okunuyor... " + dosyaadi
dosyaici = open(dosyaadi, 'r')


for i in dosyaici:

    # Baştaki ve sondaki boşlukları silme
    satir = i.strip()


    ifade = satir.split()


    numOperant = len(ifade) - 1



    # Boş satırları kontrol et.
    if numOperant == -1:
        continue



    ###################
    ## Operatör bulma##
    ###################


    operator = ifade[0]

    hata_bulundu = hata_bulundu(operator, numOperant, ifade, satir)
    if not hata_bulundu:

        # iki sayıyı toplama işlemi
        if (operator == "toplama"):
            print
            satir + ":\t", int((ifade[1] +ifade[2]) )

        # iki sayıyı çıkarma işlemi
        if (operator == "çıkarma"):
            print
            satir + ":\t", int((ifade[2] - ifade[1]) )

        # iki sayıyı çarpma işlemi
        if (operator == "çarpma"):
            print
            satir + ":\t", int((ifade[1]) * int(ifade[2]))

        # iki sayıyı bölme işlemi
        if (operator == "bölme"):
            print
            satir + ":\t", int((ifade[1]) / int(ifade[2]) )


infile.close()