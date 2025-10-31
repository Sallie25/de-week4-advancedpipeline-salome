from pipeline.config import ConfigManager

def main():
    config = ConfigManager() #creating an object of the class 

    print("Base API URL:", config.base_url)
    print("Pagination Limit:", config.pagination_limit)
    print("Log Level:", config.log_level)
    print("Log File:", config.log_file)

if __name__ == "__main__":
    main()