import os
import re
import logging
from typing import List

def set_up_logging(level:int) -> None:
    """
    Args:
        level:logging.DEBUG,logging.INFO,etc. Logging level configuration.
    """
    logging.basicConfig(level = level,format = '%(asctime)s [line:%(lineno)d] %(levelname)s: %(message)s', datefmt='%d %b %H:%M:%S')
    logger = logging.getLogger(__name__)

class Log_Parser():
    """Define all log parsing related functions.
    """
    @property
    def full_path_of_files(self) -> None:
        return self._full_path_of_files

    @full_path_of_files.setter
    def full_path_of_files(self,path_of_files:List) -> None:
        self._full_path_of_files=path_of_files

    def __init__(self) -> None:
        self._full_path_of_files=[]

    def get_required_files_path(self, folder_path:str, subfolder_included:bool = False, type_filter_reg:str =r'.(txt|csv)$') -> None:
        """
        Args:
            file_path:full path of folder to be searched.
            sub_folder_included: if we need search sub folder. Default is False.
            type_filter_reg: regular expresion to filter required file
        """
        if os.path.exists(folder_path):
            logging.debug ('Folder path exists.Continue...')
        else:
            logging.error ('Error: Can not find folder path.')
            return os._exit(1)
    
        if subfolder_included:
            #check all sub folders
            for (current_folder_path, sub_folder_name, files_name) in os.walk(folder_path):
                for one_file_name in files_name:
                    if re.search(type_filter_reg,one_file_name):
                        full_path_of_one_file=os.path.join(current_folder_path,one_file_name)
                        self._full_path_of_files.append(full_path_of_one_file)
                        logging.info ('%s is added'%full_path_of_one_file)
        else:
            #only check current folder.
            for dir in os.listdir(folder_path):
                if re.search(type_filter_reg,dir):
                    full_path_of_one_file=os.path.join(folder_path,dir)
                    self._full_path_of_files.append(full_path_of_one_file)
                    logging.info ('%s is added'%full_path_of_one_file)

    def count_required_info(self,required_info_reg:string) -> None:
        """Sum
        Args:
            required_info_reg: regular expression of required infomation
        """
        if self._full_path_of_files.count==0:
            logging.error('No file will be parsed. Check the path you want to search.')
            os._exists(1)

        


if __name__=='__main__':
    set_up_logging(logging.DEBUG)

    my_path=r"D:\Ziwen\Siemens\ET200S testing\02 Testprograms"
    my_parser=Log_Parser()
    my_parser.get_required_files_path(my_path,subfolder_included=True,type_filter_reg='.(xlsx)$')
    print(my_parser.full_path_of_files)



