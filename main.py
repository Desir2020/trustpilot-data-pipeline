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

try:
    logging.info("Démarrage du pipeline")
    df= read_csv()

    logging.info("Transformation des données")
    df_cleaned = transform_csv(df)

    logging.info("Chargement des données")
    df_load = load_reviews(df_cleaned)

    logging.info("Pipeline terminée")
except Exception as e:
    logging.error(f"Erreur dans le pipeline: {e}")

