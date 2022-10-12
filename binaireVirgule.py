def BinaireVirg(n):
    liste=[]

    while n!=0:
        if n>2:
            n=(str(n))
            n = ("0."+n)
            n = float(n)
        else:
            n = n*2
            if n>2:
                n="0.",n
                n = int(n)
            if n>1:
                n=n-1
                liste.append(1)
            elif n<1 and n!=0:
                liste.append(0)
            elif n==1:
                n = n-1
                liste.append(1)
    s = [str(integer) for integer in liste]
    a_string = "".join(s)
    res = int(a_string)
    return (res)



def Binaire(n):
    liste = []
    place = 0
    while n!=0:
        place = place-1
        if n>1:
            reste = n%2
            liste.insert(place,reste)
            n=n//2
        if n<0:
            break
        if n ==1:
            liste.insert(place,1)
            n=n-1
    s = [str(integer) for integer in liste]
    a_string = "".join(s)
    res = int(a_string)
    return (res)

def nombreVirgule(n):
    NombreOrigine = n
    out = striped(n)
    binaire = Binaire(out[1])
    virgule = BinaireVirg(out[0])
    return (f"le nombre {NombreOrigine} en binaire donne : {binaire}.{virgule}")

def striped(n):
    n = str(n)
    splited = n.split('.')
    before = splited[0]
    before = int(before)
    after = splited[1]
    after = int(after)
    return(after,before)

print (nombreVirgule(1478.8125))
