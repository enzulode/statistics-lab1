import csv
import numpy as np
from os.path import exists
from os import access, R_OK
from typing import *

def test_file_readable(file_path: str) -> bool:
  r"""
  Checks if the file is readable

  Parameters
  ----------
  file_path: file to be checked path

  Returns
  -------
  True: if the file exists and is readable
  False: otherwise
  """
  if (not exists(file_path)):
    raise Exception('File not found')
  
  return access(file_path, R_OK)

def read_csv(file_path: str) -> List[float]:
  r"""
  Reads data from the CSV file

  Parameters
  ----------
  filename: file path to read from

  Returns
  -------
  List[float]
  """
  sample = []
  try:
    if (test_file_readable(file_path)):
      with open(file_path, newline='\n') as csvfile:
        reader =  csv.reader(csvfile, delimiter=',')
        for row in reader:
          for el in row:
            sample.append(float(el))

    return np.sort(sample)
  except Exception:
    raise


  
  


