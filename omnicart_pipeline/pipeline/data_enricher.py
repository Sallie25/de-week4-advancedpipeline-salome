import requests
import pandas as pd
from config import ConfigManager
from api_client import ApiClient

class DataEnricher:
    def __init__(self, products = None, users = None):
        self.products = products # ApiClient.get_all_products()
        self.users = users # ApiClient.get_all_users()

    def convert_to_dataframe(self, data):
        if data.lower() == "products":
            cleaned_products = []
            for item in self.products:
                rating = item.get("rating")
                if isinstance(rating, dict):
                    rate = rating.get("rate")
                    count = rating.get("count")
                else:
                    rate = rating
                    count = None

                cleaned_products.append({
                    "id": item.get("id"),
                    "price": item.get("price"),
                    "category": item.get("category"),
                    "quantity": count,
                    "rating": rate
                })
            df_products = pd.DataFrame(cleaned_products)
            return df_products.head()

        elif data.lower() == "users":
            cleaned_users = []
            for item in self.users:
                cleaned_users.append({
                    "email": item.get("email"),
                    "username": item.get("username"),
                    "first_name": item.get("name", {}).get("firstname"),
                    "last_name": item.get("name", {}).get("lastname"),
                    "id": item.get("id")
                })
            df_users = pd.DataFrame(cleaned_users)
            return df_users.head()

def main():
    config = ConfigManager()
    client = ApiClient(config.base_url)
    # print(client.get_all_products())
    enricher = DataEnricher(client.get_all_products(), client.get_all_users())

    print("Products DataFrame:")
    print(enricher.convert_to_dataframe("products"))    

    print("\nUsers DataFrame:")
    print(enricher.convert_to_dataframe("users"))

if __name__ == "__main__":
    main()