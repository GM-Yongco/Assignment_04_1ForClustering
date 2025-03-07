# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: Code that will impress u ;)
# HEADERS ================================================================
import pyreadr
import pandas as pd
from collections import OrderedDict

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def section(section_name:str = "SECTION") -> None:
	section_name = f"\n {section_name} {'-' * (40 - len(section_name))}\n"
	print(section_name)

# ========================================================================
# FUNCTIONS 
# ========================================================================

def read_rda():

	result:dict = pyreadr.read_r("data_censored.rda")  # Reads the .rda file

	print(result)
	section("kill yourself")

	print(f"wiwiwi {result.keys()}")  # Shows the names of the objects in the file
	df:pd.DataFrame = result["data_censored"]  # Convert an object to a pandas DataFrame

	print(df.head())  # View the first few rows
	df.to_csv("data_censored.csv", index=False)

# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")
	read_rda()
	section("END")