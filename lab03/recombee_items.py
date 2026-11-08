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

PATH_DATASET = f"{PROJECT_ROOT}/datasets/books.csv" 

def send_items():
    """Functie care citeste dataset-ul si trimite item-urile in Recombee"""
    df = pd.read_csv(PATH_DATASET)
    print(f"Se trimit {len(df)} item-uri in Recombee...")
    
    requests = []

    skipped = 0
    for index, row in df.iterrows():
        item_id = str(row['isbn13'])
        try:
            properties = {
                "title": str(row['title']),
                "subtitle": str(row["subtitle"]) if pd.notna(row["subtitle"]) else "",
                "authors": str(row["authors"]) if pd.notna(row["authors"]) else "Unknown",
                "categories": str(row['categories']),
                "description": str(row["description"]) if pd.notna(row["description"]) else "",
                "published_year": int(row['published_year']),
                "average_rating": float(row['average_rating']),
                "num_pages": int(row['num_pages']),
                "ratings_count": int(row['ratings_count']),
            }
        
        # Adaugam request-ul de setare a valorilor pentru item
        # (SetItemValues creează automat item-ul dacă acesta nu există)
        requests.append(SetItemValues(item_id, properties, cascade_create=True))
        
            # Adaugam request-ul de setare a valorilor pentru item
            # (SetItemValues creează automat item-ul dacă acesta nu există)
            requests.append(SetItemValues(item_id, properties, cascade_create=True))

        except ValueError as e:
            # Sari peste itemi cu valori incomplete sau gresite
            # print(f"Eroare la item {str(row['isbn13'])}: {e}")
            skipped += 1
            continue
        # Trimitem in loturi (batch) de cate 100 pentru eficienta
        if len(requests) == 100:
            client.send(Batch(requests))
            requests = []
            print(f"S-a procesat un lot de 100 item-uri... ({index + 1 - skipped} / {len(df) - skipped})")
            
    # Trimitem si restul ramanase (daca numarul total nu e multiplu de 100)
    if requests:
        client.send(Batch(requests))
        print("S-a trimis ultimul lot de item-uri.")
    
    print(f"Toate item-urile au fost trimise cu succes. Item-uri trimise {len(df) - skipped} / {len(df)} ({skipped} sarite).")

if __name__ == "__main__":
    send_items()
