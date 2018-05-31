import itertools
from operator import itemgetter

def group(listna, field):
    cust = list()
    sTrans = sorted(listna, key=itemgetter(field))

    for key, group in itertools.groupby(sTrans, key=lambda x:x[field]):       
        cust.append(list(group))

    return cust

transactions = [
    { "id" : 1, "email" : "e1", "phone" : "p1", "card" : "c1" },
    { "id" : 2, "email" : "e2", "phone" : "p2", "card" : "c2" },
    { "id" : 3, "email" : "e1", "phone" : "p3", "card" : "c3" },
    { "id" : 4, "email" : "e4", "phone" : "p4", "card" : "c4" }
]

# transactions.append({ "id" : 5, "email" : "e2", "phone" : "p4", "card" : "c5" })

cek = group(transactions, 'email')

for i, val in enumerate(cek):
    customer = {
        "name" : "Customer "+str(int(i+1)),
        "data" : {
            "transaction" : [],
            "emails"    : [],
            "phones"    : [],
            "cards"     : []
        }
    }
    for j, gval in enumerate(val):
        customer["data"]["transaction"].append(gval["id"])
        customer["data"]["emails"].append(gval["email"])
        customer["data"]["phones"].append(gval["phone"])
        customer["data"]["cards"].append(gval["card"])

    print(customer)
