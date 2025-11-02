#from pipeline.config import ConfigManager
from pipeline.pipeline import Pipeline

def main():
    # config = ConfigManager() #creating an object of the class 

    # print("Base API URL:", config.base_url)
    # print("Pagination Limit:", config.pagination_limit)
    # print("Log Level:", config.log_level)
    # print("Log File:", config.log_file)
    
    pipeline = Pipeline()
    pipeline.run()

if __name__ == "__main__":
    main()