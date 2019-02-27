import random as rd
ds = ['Di', 'Duy','Giang', 'Huy','Khang', 'Khoi']
for i in range(0, len(ds)):    
    ten = rd.choice(ds)
    print ten
    ds.remove(ten)
