d_mart = {
    'invo': {
        'summer': {
            'water_bottel': {
                'water_bottel': 200,
                'Quantity': 500,
                'price': 50
            },
            'ice-crem': {
                'havemore': 300,
                'Quantity': 5000,
                'price': 200
            },
        },
        'wintter': {
            'coat': {
                'Quantity': 300,
                'price': 1000
            },
            'hiter': {
                'Quantity': 500,
                'price': 3000
            },
        },
        'mounsoon': {
            'rain-coat': {
                'Quantity': 3000,
                "price": 200
            },
            'umbrella': {
                'Quantity': 5000,
                "price": 250
            },
        },
    },
}

while True:
    choice = input("Enter choice(summer:s/mounsoon:m/winter:w): ")

    if choice in ('s', 'm', 'w'):
        j = d_mart.values()
        for i in j:
            if choice == 's':
                p = i.get('summer')
                for k, v in p.items():
                    for k2, v2 in v.items():
                        if k2 == 'Quantity' or v2 > 600:
                            print(k, ':', k2, '-', v2)

            elif choice == 'm':
                mou = i.get('mounsoon')
                for k3, v3 in mou.items():
                    for k4, v4 in v3.items():
                        if k4 == 'Quantity' or v4 > 600:
                            print(k3, ':', k4, '-', v4)
            else:
                win = i.get('wintter')
                for k5, v5 in win.items():
                    for k6, v6 in v5.items():
                        if k6 == 'Quantity' or v6 > 600:
                            print(k5, ':', k6, '-', v6)
    break
