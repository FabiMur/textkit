from pathlib import Path
from typing import Iterator
from .base_reader import BaseReader

class TxtReader(BaseReader):
    
    def read(self, file_path: str) -> Iterator[str]:
        """
        Reads a text file and yields its lines one by one.
        
        :param self: Description
        :param file_path: Description
        :type file_path: str
        :return: Description
        :rtype: Iterator[str]
        """
        # TODO: Add error handling for file not found, permission issues, etc.  
        with open(file_path, 'r', encoding='utf-8') as file:
            
            for line in file:
                yield line