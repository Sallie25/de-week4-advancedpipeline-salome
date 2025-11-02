from config import ConfigManager
from api_client import ApiClient
from data_enricher import DataEnricher
import json


class Pipeline:

    def run(self):
        # config = ConfigManager()
        # base_url = config.base_url
        # client = ApiClient(base_url)
        # products = client.get_all_products()
        # users = client.get_all_users()
        # enricher = DataEnricher(products, users)
        # print(enricher.convert_to_dataframe("products"))
        # print(enricher.convert_to_dataframe("products")) 

        config = ConfigManager()
        client = ApiClient(config.base_url)
        # print(client.get_all_products())
        enricher = DataEnricher(client.get_all_products(), client.get_all_users())

        # print("Products DataFrame:")
        enricher.convert_to_dataframe("products")

        # print("\nUsers DataFrame:")
        enricher.convert_to_dataframe("users")

        # print("\n Merged Dataframe")

        enricher.merge_df()
       
        updated_data = enricher.revenue_col()

        # merged

        export_to_dict = updated_data.to_dict()

        with open("seller_performance_report.json","w") as f:

            json.dump(export_to_dict,f,indent = 4)

        print("Exported Succefully!")


