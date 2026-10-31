import sys
from pathlib import Path
import pandas as pd
from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import SetItemValues, Batch
from recombee_api_client.exceptions import APIException

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
from db_settings import DB_NAME, PRIVATE_TOKEN, REGION

client = RecombeeClient(DB_NAME, PRIVATE_TOKEN, region=REGION)

PATH_DATASET = f"{PROJECT_ROOT}/datasets/bestsellers.csv" 

def send_items():
    """Functie care citeste dataset-ul si trimite item-urile in Recombee"""
    df = pd.read_csv(PATH_DATASET)
    print(f"Se trimit {len(df)} item-uri in Recombee...")
    
    requests = []
    
    for index, row in df.iterrows():
        # TODO 3: Extrageti ID-ul unic al produsului din coloana corespunzatoare din CSV
        item_id = str(row['nume_coloana_id'])
        
        
        # TODO 4: Mapati proprietatile definite anterior cu valorile din randul curent
        # Exemplu:
        properties = {
            "nume_proprietate_1": str(row['coloana_1']),
            "nume_proprietate_2": int(row['coloana_2']),
            "nume_proprietate_3": float(row['coloana_3'])
        }
        
        # Adaugam request-ul de setare a valorilor pentru item
        # (SetItemValues creează automat item-ul dacă acesta nu există)
        requests.append(SetItemValues(item_id, properties))
        
        # Trimitem in loturi (batch) de cate 100 pentru eficienta
        if len(requests) == 100:
            client.send(Batch(requests))
            requests = []
            print("S-a trimis un lot de 100 item-uri...")
            
    # Trimitem si restul ramanase (daca numarul total nu e multiplu de 100)
    if requests:
        client.send(Batch(requests))
        print("S-a trimis ultimul lot de item-uri.")
        
    print("Toate item-urile au fost trimise cu succes!")

if __name__ == "__main__":
    send_items()
