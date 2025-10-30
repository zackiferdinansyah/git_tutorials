print('Selamat Datang')

nilai = int(input('Masukkan Nilai Akhir :'))

if nilai >= 90:
    print('A')
elif nilai >= 80:
    print('B')
elif nilai >= 70:
    print('C')
elif nilai >= 60:
    print('D')
else:
    print('E')


def restoran(makanan='default', minuman='default'):
    pesanan = print(f'Hari ini saya ingin makan {makanan} dan juga ingin minum {minuman}')
    return pesanan

restoran('Rendang', 'Es Teh')