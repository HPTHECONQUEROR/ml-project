import sys
from src.logger import logging

def error_message_detail(error, error_detail):
    """
    This function generates a detailed error message including the script name, line number, and error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)) 
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail):
        """
        This function inherits from Exception and formats 
        a custom error message using the error_message_detail function, 
        then returns it when the exception is converted to a string
        """
        super().__init__(str(error))
        self.error_message = error_message_detail(error, error_detail=error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        print(12/0)
    except Exception as e:
        logging.info("Dubakoor Error Found")
        raise CustomException(e, sys)


