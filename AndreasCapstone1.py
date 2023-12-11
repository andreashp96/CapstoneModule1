# import fungsi
import random as r
import string as s
import os

# FUNGSI CAR DICTIONARY
carDict = {
    0: {
        'PlatNomor':'B1624PWD',
        'Model':'Fortuner',
        'Manufacturer':'Toyota',
        'Transmisi':'Automatic',
        'Tipe':'SUV',
        'JumlahSeater':7,
        'HargaSewa':350000,
        'TersediaSewa':'Tersedia'
    },
    1: {
        'PlatNomor':'B7542GS',
        'Model':'Jazz',
        'Manufacturer':'Honda',
        'Transmisi':'Automatic',
        'Tipe':'Hatchback',
        'JumlahSeater':4,
        'HargaSewa':250000,
        'TersediaSewa':'Tersedia'
    },
    2: {
        'PlatNomor':'A1026RT',
        'Model':'Teana',
        'Manufacturer':'Nissan',
        'Transmisi':'Manual',
        'Tipe':'Sedan',
        'JumlahSeater':4,
        'HargaSewa':350000,
        'TersediaSewa':'Tersedia'
        },
    3:{
        'PlatNomor':'B470HHT',
        'Model':'Civic',
        'Manufacturer':'Honda',
        'Transmisi':'Automatic',
        'Tipe':'SUV',
        'JumlahSeater':6,
        'HargaSewa':290000,
        'TersediaSewa':'Disewa'
        }
}



# LIST UNTUK KRITERIA PENCARIAN
## LIST LICENSE PLATE
licensePlatesList = []
for i in carDict:
    licensePlatesList.append(carDict[i]['PlatNomor'])

## LIST MANUFACTURER
manuList = []
for i in carDict:
    manuList.append(carDict[i]['Manufacturer'])

# LIST MODEL
modelList = []
for i in carDict:
    modelList.append(carDict[i]['Model'])



# FUNGSI MENU UNTUK MENUNJUKKAN MOBIL - MENU 1
def viewMenu():
    while True:
        try: 
            print(f'MENU VIEW MOBIL')
            print(f'='*20)
            print(f'1. Lihat semua mobil')
            print(f'2. Cari berdasarkan Filter/Sort')
            print(f'0. Exit')
            viewMenu = int(input('Pilih menu 1-2, 0:'))
            
            if viewMenu==1:
                showCar()

            elif viewMenu==2:
                filterMenu()

            elif viewMenu==0: break

            else: print(f'Mohon masukkan angka 1-5 atau 0.\n')

        except: print(f'Mohon masukkan angka 1-5 atau 0.\n')

def showCar():
    print('CAR LIST')
    print('='*105)
    print("{:<8}||{:<12}||{:<10}||{:10}||{:<10}||{:<12}||{:<10}||{:<14}||"
        .format("PLAT NO","MODEL","MANUFACTURER","TRANSMISI","TIPE","JUMLAH SEATER","HARGA SEWA","TERSEDIA SEWA"))
    print('='*105)
    if len(carDict)>0:
        for i in carDict:
            print("{:<8}||{:<12}||{:<12}||{:10}||{:<10}||{:<12}||{:<10}||{:<14}||".
            format(
            carDict[i]['PlatNomor'],
            carDict[i]['Model'],
            carDict[i]['Manufacturer'],
            carDict[i]['Transmisi'],
            carDict[i]['Tipe'],
            carDict[i]['JumlahSeater'],
            carDict[i]['HargaSewa'],
            carDict[i]['TersediaSewa'],
            ))
        print('='*105)
    else:
        print('Mobil tidak ada dalam daftar, silahkan tambahkan mobil terlebih dahulu.\n')



## SORT MENU - 1
def filterMenu():
    while True:
        try: 
            print(f'FILTER AND SEARCH MENU')
            print(f'='*20)
            print(f'1. Cari berdasarkan Model')
            print(f'2. Cari berdasarkan Manufacturer')
            print(f'3. Cari berdasarkan Transmission')
            print(f'4. Sortir dari harga terendah')
            print(f'5. Cari mobil yang bisa disewa')
            print(f'0. Exit')
            ssMenu = int(input('Pilih menu 1-5:'))
            
            if ssMenu==1:
                modelFilter()

            elif ssMenu==2:
                manuFilter()

            elif ssMenu==3:
                transFilter()

            elif ssMenu==4:
                priceSort()

            elif ssMenu==5: 
                rentFilter()

            elif ssMenu==0: break

            else: print(f'Mohon masukkan angka 1-5 atau 0.\n')

        except: print(f'Mohon masukkan angka 1-5 atau 0.\n')


# FILTER MENU - MODEL FILTER
def modelFilter():
    while True:
        restartloop = False

        try:
            if len(carDict)>0:
                modelSearch = input('Masukkan model yang ingin dicari: ')

                if modelSearch in modelList:
                    print('CAR LIST')
                    print('='*105)
                    print("{:<8}||{:<12}||{:<12}||{:10}||{:<10}||{:<12}||{:<10}||{:<14}||"
                    .format("PLAT NO","MODEL","MANUFACTURER","TRANSMISI","TIPE","JUMLAH SEATER","HARGA SEWA","TERSEDIA SEWA"))
                    print('='*105)
                    for i in carDict:
                        if(modelSearch in carDict[i]['Model']):
                            print("{:<8}||{:<12}||{:<12}||{:10}||{:<10}||{:<12}||{:<10}||{:<13}||".
                            format(
                            carDict[i]['PlatNomor'],
                            carDict[i]['Model'],
                            carDict[i]['Manufacturer'],
                            carDict[i]['Transmisi'],
                            carDict[i]['Tipe'],
                            carDict[i]['JumlahSeater'],
                            carDict[i]['HargaSewa'],
                            carDict[i]['TersediaSewa'],
                            ))
                    print('\n')
                    restartloop = sortPrompt(restartloop)

                else: 
                    print('Model yang Anda cari tidak ada.\n')
                    restartloop = sortPrompt(restartloop)

            else:
                print('Mobil tidak ada dalam daftar, silahkan tambahkan mobil terlebih dahulu.\n')
                restartloop = sortPrompt(restartloop)


            if restartloop == True: continue
            else: break

        except: print('Terjadi error.')

# FILTER MENU - MANUFACTURER FILTER
def manuFilter():
    while True:
        restartloop = False

        try:
            if len(carDict)>0:
                manuSearch = input('Masukkan manufacturer yang ingin dicari: ')

                if manuSearch in manuList:
                    print('CAR LIST')
                    print('='*105)
                    print("{:<8}||{:<12}||{:<12}||{:10}||{:<10}||{:<12}||{:<10}||{:<14}||"
                    .format("PLAT NO","MODEL","MANUFACTURER","TRANSMISI","TIPE","JUMLAH SEATER","HARGA SEWA","TERSEDIA SEWA"))
                    print('='*105)
                    for i in carDict:
                        if(manuSearch in carDict[i]['Manufacturer']):
                            print("{:<8}||{:<12}||{:<12}||{:10}||{:<10}||{:<12}||{:<10}||{:<13}||".
                            format(
                            carDict[i]['PlatNomor'],
                            carDict[i]['Model'],
                            carDict[i]['Manufacturer'],
                            carDict[i]['Transmisi'],
                            carDict[i]['Tipe'],
                            carDict[i]['JumlahSeater'],
                            carDict[i]['HargaSewa'],
                            carDict[i]['TersediaSewa'],
                            ))
                    print('\n')
                    restartloop = sortPrompt(restartloop)

                else: 
                    print('Manufacturer yang Anda cari tidak ada.\n')
                    restartloop = sortPrompt(restartloop)

            else:
                print('Mobil tidak ada dalam daftar, silahkan tambahkan mobil terlebih dahulu.\n')
                restartloop = sortPrompt(restartloop)


            if restartloop == True: continue
            else: break

        except: print('Terjadi error.')

# TRANSMISSION FILTER
def transFilter():
    while True:

        restartloop = False

        try:
            if len(carDict)>0:
                transSearch = input('Masukkan transmisi untuk disortir (Automatic/Manual):')

                if transSearch.upper()=="AUTOMATIC" or transSearch.upper()=="MANUAL":
                    print('CAR LIST')
                    print('='*105)
                    print("{:<8}||{:<12}||{:<12}||{:10}||{:<10}||{:<12}||{:<10}||{:<14}||"
                    .format("PLAT NO","MODEL","MANUFACTURER","TRANSMISI","TIPE","JUMLAH SEATER","HARGA SEWA","TERSEDIA SEWA"))
                    print('='*105)
                    for i in carDict:
                        if(transSearch.capitalize() in carDict[i]['Transmisi']):
                            print("{:<8}||{:<12}||{:<12}||{:10}||{:<10}||{:<12}||{:<10}||{:<14}||".
                            format(
                            carDict[i]['PlatNomor'],
                            carDict[i]['Model'],
                            carDict[i]['Manufacturer'],
                            carDict[i]['Transmisi'],
                            carDict[i]['Tipe'],
                            carDict[i]['JumlahSeater'],
                            carDict[i]['HargaSewa'],
                            carDict[i]['TersediaSewa'],
                            ))
                    print('\n')
                    restartloop = sortPrompt(restartloop)

                else: 
                    print('Manufacturer yang Anda cari tidak ada.\n')
                    restartloop = sortPrompt(restartloop)

            else:
                print('Mobil tidak ada dalam daftar, silahkan tambahkan mobil terlebih dahulu.\n')
                restartloop = sortPrompt(restartloop)


            if restartloop == True: continue
            else: break

        except: print('Terjadi error.')

# RENT FILTER
def rentFilter():
    if len(carDict)>0:
            rentSearch = 'Tersedia'
            print('CAR LIST')
            print('='*105)
            print("{:<8}||{:<12}||{:<10}||{:10}||{:<10}||{:<12}||{:<10}||{:<14}||"
            .format("PLAT NO","MODEL","MANUFACTURER","TRANSMISI","TIPE","JUMLAH SEATER","HARGA SEWA","TERSEDIA SEWA"))
            print('='*105)
            for i in carDict:
                if(rentSearch in carDict[i]['TersediaSewa']):
                    print("{:<8}||{:<12}||{:<10}||{:10}||{:<10}||{:<12}||{:<10}||{:<14}||".
                    format(
                    carDict[i]['PlatNomor'],
                    carDict[i]['Model'],
                    carDict[i]['Manufacturer'],
                    carDict[i]['Transmisi'],
                    carDict[i]['Tipe'],
                    carDict[i]['JumlahSeater'],
                    carDict[i]['HargaSewa'],
                    carDict[i]['TersediaSewa'],
                    ))
            print('\n')

    else:
        print('Mobil tidak ada dalam daftar, silahkan tambahkan mobil terlebih dahulu.\n')

# SORTING PRICE
def priceSort():
    carList = list(carDict.items())

    sortedPrice = sorted(carList, key=lambda y:y[1]['HargaSewa'])
    # y[1] menandakan bahwa value dict dalam list ada di kolom 1
    if len(carDict)>0:
                print('CAR LIST')
                print('='*105)
                print("{:<8}||{:<12}||{:<12}||{:10}||{:<10}||{:<12}||{:<10}||{:<14}||"
                .format("PLAT NO","MODEL","MANUFACTURER","TRANSMISI","TIPE","JUMLAH SEATER","HARGA SEWA","TERSEDIA SEWA"))
                print('='*105)
                for i in sortedPrice:
                        print("{:<8}||{:<12}||{:<12}||{:10}||{:<10}||{:<12}||{:<10}||{:<14}||".
                        format(
                        i[1]['PlatNomor'],
                        i[1]['Model'],
                        i[1]['Manufacturer'],
                        i[1]['Transmisi'],
                        i[1]['Tipe'],
                        i[1]['JumlahSeater'],
                        i[1]['HargaSewa'],
                        i[1]['TersediaSewa'],
                        ))
                print('\n')

    else:
        print('Mobil tidak ada dalam daftar, silahkan tambahkan mobil terlebih dahulu.\n')

#PROMPT
def sortPrompt(x):
    while True:
        try:
            x = False

            redo = input('Apakah anda ingin melanjutkan search/sort ini?(Y/T):')

            if redo.upper()=='Y':
                x = True
                break
            elif redo.upper()=='T':
                x = False
                break
            else: 
                print('Mohon masukkan Y atau T.')
                continue

        except: print('Mohon hanya masukkan Y atau T.')
    
    return x




newCarList = []

# CREATE MENU - 2
def createMenu():

    while True:
        os.system("cls")
        try:
            townList = ['A', 'B']
            randomletters = s.ascii_uppercase
            plat1 = str(''.join(r.choice(townList) for i in range(1)))
            plat2 = str(r.randint(1,9999))
            plat3 = str(''.join(r.choice(randomletters) for i in range(r.randint(1,3))))

            restartloop = False

            newPlate = ''
            newModel = ''
            newManufacturer = ''
            newTrans = ''
            newType = ''
            newHarga = 0
            newSeater = 0
            newStatus = ''

            # PLATE GENERATION
            while True:

                plateGen = plat1+plat2+plat3

                if plateGen in licensePlatesList: 
                    print('Membuat ulang plat nomor...')
                    continue
                else: 
                    newPlate = plateGen
                    break

            # NAMA MODEL
            while True:
                try:
                    inputModel = input('Masukkan nama model (max 20 karakter): ')
                    if len(inputModel)>20: 
                        print('Masukkan maksimal 20 karakter.')
                        continue
                    elif len(inputModel)==0: 
                        print('Data tidak terisi. Mohon masukkan maksimal 20 karakter.')
                        continue
                    else: 
                        newModel = inputModel
                        break
                except: print('Input error. Mohon masukkan string. \n')

            # NAMA MANUFACTURER
            while True:
                try:
                    inputManufacturer = input('Masukkan nama manufacturer (max 20 karakter): ')
                    if len(inputManufacturer)>20: 
                        print('Masukkan maksimal 20 karakter.')
                        continue
                    elif len(inputManufacturer)==0: 
                        print('Data tidak terisi. Mohon masukkan maksimal 20 karakter.')
                        continue
                    else: 
                        newManufacturer = inputManufacturer
                        break
                except: print('Input error. Mohon masukkan string.\n')

            # TRANSMISI
            while True:
                try:
                    inputTrans = input('Masukkan transmisi (Automatic/AT, Manual/MT): ')
                    if inputTrans.upper() == 'AT' or inputTrans.upper() == 'AUTOMATIC':
                        newTrans = 'Automatic'
                        break
                    elif inputTrans.upper() == 'MT' or inputTrans.upper() == 'MANUAL':
                        newTrans = 'Manual'
                        break
                    else: 
                        print('Mohon masukkan Automatic/AT atau Manual/MT.\n')
                        continue
                except: print('Input error. Mohon masukkan Automatic/AT atau Manual/MT.\n') 

            # TIPE KENDARAAN
            while True:
                try:
                    inputType = input('Masukkan tipe kendaraan(Sedan/SUV/Hatchback/Pickup/MPV): ')
                    if inputType.upper()=='SEDAN' or inputType.upper()=='HATCHBACK' or inputType.upper()=='PICKUP': 
                        newType = inputType.capitalize()
                        break
                    elif inputType.upper()=='SUV' or inputType.upper()=='MPV':
                        newType = inputType.upper()
                        break
                    else: 
                        print('Mohon masukkan Sedan/SUV/Hatchback/Pickup/MPV.\n')
                        continue
                except: print('Input error. Mohon masukkan Sedan/SUV/Hatchback/Pickup/MPV.\n')
            
            # JUMLAH SEATER
            while True:
                try:
                    inputSeater = int(input('Masukkan jumlah kursi mobil (2-8): '))
                    if inputSeater<2 or inputSeater>8: 
                        print('Mohon masukkan minimal 2, maksimal 8.\n')
                        continue
                    else:
                        newSeater = inputSeater
                        break

                except: print('Input error. Mohon masukkan minimal 2, maksimal 8.\n')

            # HARGA MOBIL
            while True:
                try:
                    inputHarga = int(input('Masukkan harga (100 rb-1 jt): '))
                    if inputHarga<100000 or inputHarga>1000000: 
                        print('Mohon masukkan minimal 100 ribu, maksimal 1 juta.\n')
                        continue
                    else:
                        newHarga = inputHarga
                        break

                except: print('Input error. Mohon masukkan minimal 100 ribu, maksimal 1 juta.\n')

            # TERSEDIA SEWA
            while True:
                try:
                    inputStatus = input('Masukkan ketersediaan (Tersedia/Disewa): ')
                    if inputStatus.upper()=='TERSEDIA':
                        newStatus='Tersedia'
                        break
                    elif inputStatus.upper()=='DISEWA':
                        newStatus='Disewa'
                        break
                    else: print('Mohon masukkan Tersedia atau Disewa.')

                except: print('Input error. Mohon masukkan ketersediaan sewa True atau False.\n')

            
            print('KONFIRMASI PENAMBAHAN MOBIL')
            print(f'Plat Nomor     : {newPlate}')
            print(f'Model          : {newModel}')
            print(f'Manufacturer   : {newManufacturer}')
            print(f'Transmisi      : {newTrans}')
            print(f'Tipe Kendaraan : {newType}')
            print(f'Jumlah Seater  : {newSeater}')
            print(f'Harga Sewa     : {newHarga}')
            print(f'Status         : {newStatus}')

            while True:
                confirm = input("Apakah ini sudah sesuai? (Y/T):")

                if confirm.upper() == 'Y':
                    newCarList.append(newPlate)
                    newCarList.append(newModel)
                    newCarList.append(newManufacturer)
                    newCarList.append(newTrans)
                    newCarList.append(newType)
                    newCarList.append(newSeater)
                    newCarList.append(newHarga)
                    newCarList.append(newStatus)

                    licensePlatesList.append(newPlate)
                    modelList.append(newModel)
                    manuList.append(newManufacturer)

                    restartloop = False
                    break
                elif confirm.upper() == 'T':
                    restartloop = True
                    break
                else:
                    print('Mohon isi dengan Y atau T.')


            if restartloop == True: continue
            else: 
                # 'JumlahSeater'
                keys = ['PlatNomor', 'Model', 'Manufacturer', 'Transmisi', 'Tipe', 'JumlahSeater', 'HargaSewa', 'TersediaSewa']
                newvalues = newCarList

                keyValue = zip(keys, newvalues)

                newCar = dict(keyValue)

                lastKey = max(carDict.keys())
                nextKey = lastKey + 1 

                carDict[nextKey]=newCar
                print('Mobil anda telah berhasil ditambahkan.')
                break

        except: print('Terdapat error.')
        
            
        


# UPDATE MENU - 3
def updateMenuScreen():
    print('PILIH MENU UNTUK MENGGANTI DATA MOBIL')
    print('==============')
    print('1. Harga Sewa')
    print('2. Status Sewa')
    print('0. Exit')

def updateMenu():
    while True:
        restartloop = False

        try:
            showCar()
            updatePlat = input('Masukkan plat untuk mengupdate mobil: ')

            if updatePlat.upper().replace(' ','') not in licensePlatesList:
                print('Mohon maaf, nomor plat yang diinput tidak ditemukan pada daftar mobil.')
                continue
            else:
                while True:
                    try:
                        updateMenuScreen()
                        updateChoice = int(input('Mohon masukkan 0-2:'))
                        
                        if updateChoice==1:
                            while True:
                                try:
                                    newHarga = int(input('Masukkan harga baru: '))
                                    print(newHarga)
                                    if 0 < newHarga < 1000000:
                                        for key,value in list(carDict.items()):
                                            if isinstance(value, dict) and updatePlat in list(carDict[key].values()):
                                                carDict[key]['HargaSewa']=newHarga
                                                print('Harga mobil telah berhasil diubah.')
                                        break                                    
                                    
                                    else:
                                        print(f'Mohon masukkan 0 - 1 juta.')

                                except: print(f'Mohon masukkan angka 0 - 1 juta.')
                            updatePrompt(restartloop)

                        elif updateChoice==2:
                            while True:
                                try:
                                    inputStatus = (input('Masukkan status sewa baru: '))
                                    if inputStatus.upper()!='TERSEDIA' and inputStatus.upper()!='DISEWA':
                                        print(f'Mohon masukkan Tersedia atau Disewa')
                                    else:
                                        for key,value in list(carDict.items()):
                                            if isinstance(value, dict) and updatePlat in list(carDict[key].values()):
                                                carDict[key]['TersediaSewa']=inputStatus.capitalize()
                                                print(f'Status Sewa mobil ini telah berhasil diubah.')
                                        break

                                except: print(f'Mohon hanya masukkan True atau False.')
                            updatePrompt(restartloop)
                        
                        elif updateChoice==0:
                            break

                        elif not(isinstance(updateChoice, int)):
                            print("Mohon masukkan angka integer.")

                        else:
                            print('Mohon masukkan angka 0-2.')
                        
                    
                    except: print("Terdapat error.")

            if restartloop == True: continue
            else:
                break
            
        except: print('Terdapat error.')

# PROMPT UPDATE
def updatePrompt(x):
    while True:
        try:
            x = False

            redo = input('Apakah anda ingin melanjutkan update?(Y/T):')

            if redo.upper()=='Y':
                x = True
                break
            elif redo.upper()=='T':
                x = False
                break
            else: 
                print('Mohon masukkan Y atau T.')
                continue

        except: print('Mohon hanya masukkan Y atau T.')
    
    return x





# DELETE MENU - 4
def deleteMenu():
    while True:

        try:
            restartloop = False
            showCar()
            deletePlat = input('Masukkan plat untuk menghapus mobil: ')

            if deletePlat.upper().replace(' ','') in licensePlatesList:
                for key,value in list(carDict.items()):
                    if isinstance(value, dict) and deletePlat in list(carDict[key].values()):

                        licensePlatesList.remove(deletePlat)
                        manuList.remove(carDict[key]['Manufacturer'])
                        modelList.remove(carDict[key]['Model'])
                        print('Daftar mobil telah berhasil dihapus.\n')
                        del carDict[key]
                        continue

            else:
                print('Mohon maaf, nomor plat yang diinput tidak ditemukan pada daftar mobil.\n')
            
            restartloop = deletePrompt(restartloop)


            if restartloop == True: continue

            else:
                break
            
        except: print('Mohon maaf, nomor plat yang diinput tidak ditemukan.\n')

# PROMPT DELETE
def deletePrompt(x):
    while True:
        try:
            x = False

            redo = input('Apakah anda ingin melanjutkan delete?(Y/T):')

            if redo.upper()=='Y':
                x = True
                break
            elif redo.upper()=='T':
                x = False
                break
            else: 
                print('Mohon masukkan Y atau T.\n')
                continue

        except: print('Mohon hanya masukkan Y atau T.\n')
    
    return x


# FUNGSI UNTUK MENU UTAMA
def mainMenu():
    print('WELCOME TO ANDREAS CAR RENTAL SERVICES!')
    print('---------------------------------------')
    print('MAIN MENU')
    print('1 - Lihat Daftar Mobil (READ, SORT AND FILTER)')
    print('2 - Tambah Daftar Mobil (CREATE)')
    print('3 - Update Daftar Mobil (UPDATE)')
    print('4 - Hapus Daftar Mobil (DELETE)')
    print('0 - Exit Menu')

# APLIKASI
while True:
    try:

        mainMenu()
        menu = int(input('Pilih Menu: '))
        print('\n')


        if(menu==1):
            viewMenu()
    
        elif(menu==2):
            createMenu()

        elif(menu==3):
            updateMenu()
    
        elif(menu==4):
            deleteMenu()

        elif(menu==0):
            print('Terima kasih untuk menggunakan Andreas Car Rental Services!')
            break

        elif (menu<0 or menu>4):
            print('Mohon masukkan menu angka 0-4.')


    except: 
        print('Mohon maaf, Anda harus memasukkan angka 0-4.')