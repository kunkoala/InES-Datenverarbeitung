# InES-Datenverarbeitung
BT-Lab .mpt to csv converter with loops.

Extra: The mpt to pandas dataframe can be used as well for other purposes such as plotting using 
       matplotlib or seaborn with python.

# HOW TO USE

1. Place .py or .ipnyb script files in the same directory as the .mpt files you want to convert.

   **Skip to 2. for .ipnyb**
   
   **Skip to 3. for .py**

2. ---> JUPYTER NOTEBOOK file (.ipnyb)
    1. Run Jupyter Notebook in the directory of the script and open the mpt_to_csv_withloop.ipnyb
    2. Make sure the .ipnyb file is in the same directory as the .mpt files.
    3. Run the script through the menu Cell > Run All
    4. The .csv files can be found in the same directory with *__loopNr.csv filename.

3. ---> PYTHON SCRIPT file (.py)
    1. Run the program through the Terminal (Anaconda Prompt recommended for windows)
    2. Type in: `python scriptname.py` --- example: `python mpt_to_csv_withloop.py`
    3. The program will run through terminal and the .csv files can be found in the same directory. 



