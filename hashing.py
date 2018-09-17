def hashing_key(id_product):
    if ord(id_product[0])%2==0:
        position=int(ord(id_product[0])/2)*1000+int(id_product[1:])
    else:
        position=int(ord(id_product[0])/2)*1000+500+int(id_product[1:])
    return position
for i in "ABCDEFGHIJKLMNOPQRSTUVWXY":
    for j in "12345":
        for k in "0123456789":
            for l in "0123456789":
                id_product=i+j+k+l
                print(id_product,hashing_key(id_product))

