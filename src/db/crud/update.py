
import json
import os

KEY = os.environ["APIKEY"]
URL_UPDATE = os.environ["URL_UPDATE"]

def updateCRUD():
    from db.mainCRUD import CRUD
    url = URL_UPDATE

    payload = json.dumps(
        {
        "collection": "bikes",
        "database": "GreenMobility",
        "dataSource": "Cluster0",
        "filter": {"name":"Prueba"},
        "update": { "$set": { "name": "PruebaDeLaMuerte" } } })

    return CRUD(url, payload)
