import logging
from extract.scrapper import read_csv
from transform.transform import transform_csv
from load.load import load_reviews

logging.basicConfig(
    level = logging.INFO,
    
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("logs/pipeline.log")
    ]
)

df= read_csv()

df_cleaned = transform_csv(df)

df_load = load_reviews(df_cleaned)

