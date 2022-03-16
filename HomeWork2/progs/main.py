
from package.H10_2 import *
alphacounter = AlphaCounter(input("Please enter the full path to filename: "))
alphacounter.calc_chars()
alphacounter.dict_sort()
alphacounter.print_hist()
alphacounter.write_hist()