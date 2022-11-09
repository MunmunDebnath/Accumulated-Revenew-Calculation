import argparse
from datetime import datetime
import functools
from pathlib import Path
import os
import shutil
import json
import xml.etree.cElementTree as ET 

from jinja2 import Environment, FileSystemLoader

from extractor import *
from revcalculate import *
from xmlgenerator import *

def main(ifilename,ofilepath)->bool:
    unique_banner_list=[]
    list_of_lists=creatlistfromtext(ifilename)
    if list_of_lists:
       unique_banner_list=uniqueBannerSearch(list_of_lists)
    if unique_banner_list:  
        total_price_calculated=revenueCalculation(unique_banner_list,list_of_lists)
    
    

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--inputfilepath', default=None, type=str, required=False)
    parser.add_argument('--outputfilepath',default=None, type=str, required=False)
    parser.add_argument('--xmlrootelement',default=None, type=str, required=False)
    args=parser.parse_args()

    root = ET.Element("Banners")

    input_file_location= args.inputfilepath
    output_file_location=args.outputfilepath
    xml_root_element=args.xmlrootelement 

    if not input_file_location:
        input_file_location='.\\reportgenerator\\resources\data.log'

    if not output_file_location:
        output_file_location='.\\reportgenerator\\resources'

    if not xml_root_element:
        xml_root_element='Banners'  

   
    main(input_file_location,output_file_location)    

    
    

 