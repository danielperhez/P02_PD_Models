import sys


bins = {
    "loan_amnt": [
        {
            "label": "(37, 40)",
            "max": 14000
        },
        {
            "label": "(40, 46)",
            "max": 35000
        },
    ],
    "funded_amnt": [
        {
            "label": "(23, 83)",
            "max": 14000
        },
        {
            "label": "(23, 83)",
            "max": 35000
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
            "label": "(-inf, 29000)",
            "max": 10
        },
        {
            "label": "(558, 1254)",
            "max": 14
        },
        {
            "label": "(47000, inf)",
            "max": sys.maxsize
        },
    ],
    "installment": [
        {
            "label": "(37, 40)",
            "max": 432
        },
        {
            "label": "(40, 46)",
            "max": 1410
        },
    ],
    "annual_inc": [
        {
            "label": "(29000, 33000)",
            "max": 73277
        },    
        
        {
            "label": "(1597, inf)",
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
            "label": "(37, 40)",
            "max": 11400
        },
        
        {
            "label": "(1597, inf)",
            "max": sys.maxsize
        },
    ],
    "total_pymnt_inv": [
        {
            "label": "(37, 40)",
            "max": 11400
        },
        
        {
            "label": "(1597, inf)",
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
            "max": 10000
        },
        
        {
            "label": "(1597, inf)",
            "max": sys.maxsize
        },
    ],
    "total_rec_int": [
        {
            "label": "(12, 45)",
            "max": 2589
        },
        {
            "label": "(45, 71)",
            "max": 24206
        },
    ],
    "last_pymnt_amnt": [
        {
            "label": "(558, 1254)",
            "max": 3124
        },
        {
            "label": "(1597, inf)",
            "max": sys.maxsize
        },
    ],

}