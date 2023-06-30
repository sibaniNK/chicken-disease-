import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name= "cnn_classifier"

list_of_files = ['.github/workflows/.gitkeep',
                 f'src/{project_name}/__init__.py', # init is a constructer file
                 f'src/{project_name}/components/__init__.py',  # create another constructor file components
                 f'src/{project_name}/utils/__init__.py',
                 f'src/{project_name}/config/configuration.py',
                 f'src/{project_name}/pipeline/__init__.py' ,
                 f'src/{project_name}/entity/__init__.py' ,
                 f'src/{project_name}/constants/__init__.py' ,
                 "config/congig.yaml", # we use mlops tool loke DVC
                 "dvc.yaml",
                 "params.yaml",
                 "requirements.txt",
                 "setup.py",
                 "research/trials.ipynb" # we need to experiment so i created research file

                 ]

for filepath in list_of_files:
    filepath= Path(filepath) # the list_of_files contain so many forward slash
    filedir,filename = os.path.split(filepath)# it will split the directory and python file

    if filedir != "":   # not empty
        os.makedirs(filedir,exist_ok = True) # true it won't create the directory again
        logging.info(f"creating directory:  {filedir} for the file:{filename}")
        # this if condition will give me a directory

    # next we create the files
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): # if the filepath not exist or size ==0 then (get size return the size of the file in numbers.
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file : {filepath}")

    else:
        logging.info(f"{filename} is already exist")