def tickets(peopleInLine):
    duitKembaliVasya = { "50": 0, "25": 0 }
    hargaTiket = 25
    check = "YES"

    for duitCustomer in peopleInLine :
        kembali = duitCustomer - hargaTiket
        if(kembali == 0) :
            duitKembaliVasya["25"] += 1
        elif(kembali == 25) :
            if(duitKembaliVasya["25"] == 0) :
                check = "NO"
                break
            duitKembaliVasya["25"] -= 1
            duitKembaliVasya["50"] += 1
        elif(kembali == 75) :
            if(duitKembaliVasya["50"] > 0 and duitKembaliVasya["25"] > 0) :
                duitKembaliVasya["50"] -= 1
                duitKembaliVasya["25"] -= 1
            elif(duitKembaliVasya["25"] > 2) :
                duitKembaliVasya["25"] -= 3
            else :
                check = "NO"
                break

    return check

print(tickets([25,25,25, 50, 100]))

