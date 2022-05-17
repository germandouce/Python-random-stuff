pal =""
palabra_mas_larga=""
oracion = "Quiero aprobar algoritmos y algebra"
i = 0
while (i< len(oracion)):
    if oracion[i] != " " and i != len(oracion)-1:
        pal += oracion[i]
    else:
        if i == len(oracion)-1:
            pal += oracion[i]

        if (len(pal) > len(palabra_mas_larga)):
            palabra_mas_larga = pal
        pal= ""
    i+=1

print(palabra_mas_larga)