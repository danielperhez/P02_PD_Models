import sys


bins = {
    "loan_amnt": [
        {
            "label": '(-inf, 37)',
            "max": 500
        },
        {
            "label": "(37, 40)",
            "max": 14000
        },
        {
            "label": "(40, 46)",
            "max": 35000
        },
        {
            "label": "(58, inf)",
            "max": sys.maxsize
        },
    ],
    "funded_amnt": [
        {
            "label": "(-inf, 23)",
            "max": 500
        },
        {
            "label": "(23, 83)",
            "max": 14000
        },
        {
            "label": "(23, 83)",
            "max": 35000
        },
        {
            "label": "(83, inf)",
            "max": sys.maxsize
        },
    ],
    "funded_amnt_inv": [
        {
            "label": "(-inf, 29000)",
            "max": 500
        },
        {
            "label": "(29000, 33000)",
            "max": 14000
        },
        {
            "label": "(33000, 42000)",
            "max": 35000
        },
        {
            "label": "(47000, inf)",
            "max": sys.maxsize
        },
    ],
    "int_rate": [
        {
            "label": "(-inf, 558)",
            "max": 5
        },
        {
            "label": "(558, 1254)",
            "max": 14
        },
        {
            "label": "(1254, 1597)",
            "max": 26
        },
        {
            "label": "(1597, inf)",
            "max": sys.maxsize
        },
    ],
    "installment": [
        {
            "label": "(-inf, 37)",
            "max": 16
        },
        {
            "label": "(37, 40)",
            "max": 432
        },
        {
            "label": "(40, 46)",
            "max": 1410
        },
        {
            "label": "(58, inf)",
            "max": sys.maxsize
        },
    ],
    "annual_inc": [
        {
            "label": "(-inf, 29000)",
            "max": 1896
        },
        {
            "label": "(29000, 33000)",
            "max": 73277
        },
        {
            "label": "(33000, 42000)",
            "max": 750000
        },
        {
            "label": "(47000, inf)",
            "max": sys.maxsize
        },
    ],
    "total_acc": [
        {
            "label": "(-inf, 558)",
            "max": 10
        },
        {
            "label": "(558, 1254)",
            "max": 25
        },
        {
            "label": "(1254, 1597)",
            "max": 156
        },
        {
            "label": "(1597, inf)",
            "max": sys.maxsize
        },
    ],
    "total_pymnt": [
        {
            "label": "(-inf, 37)",
            "max": 37
        },
        {
            "label": "(37, 40)",
            "max": 11400
        },
        {
            "label": "(40, 46)",
            "max": 57000
        },
        {
            "label": "(58, inf)",
            "max": sys.maxsize
        },
    ],
    "total_pymnt_inv": [
        {
            "label": "(-inf, 37)",
            "max": 37
        },
        {
            "label": "(37, 40)",
            "max": 11400
        },
        {
            "label": "(40, 46)",
            "max": 57000
        },
        {
            "label": "(83, inf)",
            "max": sys.maxsize
        },
    ],
    "total_rec_prncp": [
        {
            "label": "(-inf, 29000)",
            "max": 1000
        },
        {
            "label": "(29000, 33000)",
            "max": 8800
        },
        {
            "label": "(33000, 42000)",
            "max": 35000
        },
        {
            "label": "(47000, inf)",
            "max": sys.maxsize
        },
    ],
    "total_rec_int": [
        {
            "label": "(-inf, 12)",
            "max": 12
        },
        {
            "label": "(12, 45)",
            "max": 2589
        },
        {
            "label": "(45, 71)",
            "max": 24206
        },
        {
            "label": "(71, inf)",
            "max": sys.maxsize
        },
    ],
    "last_pymnt_amnt": [
        {
            "label": "(-inf, 558)",
            "max": 11
        },
        {
            "label": "(558, 1254)",
            "max": 3124
        },
        {
            "label": "(1254, 1597)",
            "max": 36234
        },
        {
            "label": "(1597, inf)",
            "max": sys.maxsize
        },
    ],

}