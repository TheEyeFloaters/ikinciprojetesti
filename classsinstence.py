class kutuphane :
    def __init__(self , age , height , weight ) :
        self.yas = age
        self.boy = height
        self.kilo = weight
        self.kitle_indeks = float(weight/(height*height))
        
    def kitle_indeksi (self):
        return '{} {} {} {}'.format(self.yas , self.boy , self.kilo , self.kitle_indeks)
    def tum_ozellikler (self):
        return '{} {} {} '.format(self.yas , self.boy , self.kilo )
     
        
burak = kutuphane(31 , 1.90 , 130)
firat = kutuphane(20, 1.95 , 90)
evren = kutuphane(20, 1.80 , 65)

print(burak.kitle_indeksi())
print(firat.tum_ozellikler())