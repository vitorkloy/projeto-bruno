from pymongo import MongoClient
from CTkMessagebox import CTkMessagebox

def connect():
    try:
        db = MongoClient("mongodb://localhost:27017/bruno")
        return db["bruno"]
    except Exception as e:
        print("erro " + str(e))
        return CTkMessagebox(title="Erro", icon="warning", message=f"Ocorreu um erro: {str(e)}")  
