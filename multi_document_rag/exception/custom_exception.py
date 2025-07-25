import sys
from multi_document_rag.logger.logger import logger

def error_message_details(error, error_details=sys):
    """_summary_

    Args:
        error (_type_): _description_
        error_details (_type_): _description_

    Returns:
        _type_: _description_
    """
    # sys.exc_info() returns a tuple of: (exc_type, exc_value, exc_traceback)
    _, _, exc_tb = error_details.exc_info()
    
    # tb_frame: frame object
    # f_code: code object
    # co_filename: the name of the file containing the code
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    error_message = (
        f"\n[ERROR]"
        f"\nFile    : {file_name}"
        f"\nLine    : {exc_tb.tb_lineno}"
        f"\nMessage : {str(error)}\n"
    )
    return error_message
    

class CustomException(Exception):
    def __init__(self, error_message, error_details=sys, log=True, custom_msg=None):
        """ Initializes the CustomException with a detailed error message."""
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_details)
        if custom_msg:
            self.error_message += {custom_msg} + ": " + self.error_message
        if log:
            logger.error(error_message)
            
    def __str__(self):
        return self.error_message
    
if __name__ == "__main__":
    try:
        a = 10 / 0
    except Exception as e:
        raise CustomException(e)
    