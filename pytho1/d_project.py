price ={}
d_mart = {
    "Inventory": {

        "Clothes": {
            "shirt": {

                "Quantity": 50,
                "price": 200
            },
            "Jeans": {

                "Quantity": 30,
                "price": 250
            }

        },
        "Groceries": {
            "oil": {
                "Quantity": 45,
                "price": 2000,
            },
            "rice": {
                "Quantity": 205,
                "price": 100,
            },
            "wheat": {
                "Quantity": 69,
                "price": 1000,
            }
        },

    }
}

i = d_mart.values()
for j in i:
    k = j.values()
    for l in k:
     for k1 , v2 in l.items():
         for k,v in v2.items():
           if k=='price' and  v > 200:
               if v <= 250:
                   dis_am = (10 * v) / 100;
                   dis = v - dis_am
                   print(k1,':', k, dis,'10% discount')
               elif v >= 2000:
                   print(k1, ':', k, v, 'By one get one free')
               elif v == 1000:
                   print(k1, ':', k, v, '200gm free')
               else:
                   print(k1, ':', k, v, 'not in discount')
