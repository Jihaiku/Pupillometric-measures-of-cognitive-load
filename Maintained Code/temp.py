from Data_Preprocessor import *
import glob
import os
import pandas as pd


os.chdir(r"C:\Users\cdhye\Desktop\Semester 5, 2023\Eye Tracking\Project\New Project Content\Dataframes")
processor = Pypil_Dataframe_Processor()
processor.process_csv_files()