from fastapi import FastAPI
from models import RequestEvaluation

import pandas as pd

from utils import load_ml_model

app=FastAPI()

@app.get("/health")
def health_check():
    return{"is_aliva": True}

@app.post("/evaluate")
async def evaluate(req: RequestEvaluation):
    print(req)
    df=pd.dataFrame({
        "int_rate":[req.int_rate],
        "out_prncp": [req.out_prncp],
        "total_req_prncp":[req.total_req_prncp],
        "last_pymnt_amnt": [req.last_pymnt_amnt],
        "addr_state": [req.addr_state],
        "grade": [req.grade],
        "sub_grade": [req.sub_grade"],
        "total_pymn": [req.total_pymn],
    })

    model=load_ml_model("/model.pkl")

    print(model)

