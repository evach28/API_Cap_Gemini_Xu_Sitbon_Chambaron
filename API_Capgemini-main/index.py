from fastapi import FastAPI
from routes.stock import stock
app = FastAPI() # Create FastAPI instance
app.include_router(stock) # Include the stock router