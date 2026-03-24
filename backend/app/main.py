from fastapi import FastAPI
from query_engine import most_ordered_products

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Graph ERP AI system running"}

@app.get("/top-products")
def top_products():

    result = most_ordered_products()

    return result.to_dict()