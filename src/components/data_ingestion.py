from email import header
from genericpath import exists
from operator import index
import os
# from re import S
import sys
from dataclasses import dataclass
import pandas as pd
from sklearn.model_selection import train_test_split
from src.exception import CustomException
from src.logger import logging
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        '''
        This will read from the data base
        '''
        logging.info("Entered The Data Ingestion method")
        try:
            '''
            Here we can call from mongoDB or any cloud DataBases
            '''
            df=pd.read_csv('src/notebook/data/stud.csv')
            logging.info("Exported the dataset as Dataframe")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) #If folder is already there then exist_ok will keep the same folder instead of creating
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train Test split Initiated")
            train_set,test_set = train_test_split(df,test_size=0.1,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)      
            
            logging.info("Ingestion of Data is completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()