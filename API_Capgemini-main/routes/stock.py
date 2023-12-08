from fastapi import APIRouter
from models.stock import Stock
from config.db import conn
from schemas.stock import stockEntity, stocksEntity
from fastapi import HTTPException
from pymongo.errors import OperationFailure
import logging
stock=APIRouter()


# Create an instance of APIRouter for the 'stock' route
stock = APIRouter()

@stock.get('/{siret}')
async def find_one_stock(siret):
    try:
        # Log de la requête HTTP
        logging.info(f"HTTP GET request received for siret: {siret}")

        # Attempt to find the stock with the given siret in the database
        result = stockEntity(conn.capgemini_db.capgemini_clt.find_one({"siret": int(siret)}))
        if result:
            # Log success and return the stock entity
            logging.info(f"Retrieved stock with siret {siret}")
            return stockEntity(result)
        else:
            # Log a warning and raise an HTTPException if the stock is not found
            logging.warning(f"Stock with siret {siret} not found")
            raise HTTPException(status_code=404, detail="Stock not found")
    except OperationFailure as e:
        # Log an error and raise an HTTPException for operation failure
        logging.error(f"Operation failure while retrieving stock: {e}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")
    except Exception as e:
        # Log an error and raise an HTTPException for any other exception
        logging.error(f"An unexpected error occurred: {e}")
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")


@stock.delete('/{siret}')
async def delete_stock(siret):
    try:
        # Log de la requête HTTP
        logging.info(f"HTTP DELETE request received for siret: {siret}")

        # Attempt to find and delete the stock with the given siret in the database
        deleted_stock = stockEntity(conn.capgemini_db.capgemini_clt.find_one_and_delete({"siret": int(siret)}))
        
        if deleted_stock:
            # Log success and return the deleted stock entity
            logging.info(f"Stock deleted with siret {siret}")
            return deleted_stock
        else:
            # Log a warning and raise an HTTPException if the stock is not found
            logging.warning(f"Stock with siret {siret} not found for deletion")
            raise HTTPException(status_code=404, detail="Stock not found for deletion")
    except OperationFailure as e:
        # Log an error and raise an HTTPException for operation failure
        logging.error(f"Operation failure while deleting stock: {e}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")
    except Exception as e:
        # Log an error and raise an HTTPException for any other exception
        logging.error(f"An unexpected error occurred during deletion: {e}")
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")
