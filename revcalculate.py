import xml.etree.cElementTree as ET
from extractor import *
from xmlgenerator import *


class CalculateRevenew():


    def uniqueBannerSearch(list_of_lists) -> list:
        unique_banner_number = []
        for idx in range(len(list_of_lists)):
            if (list_of_lists[idx][0] == 'sel'):
               if list_of_lists[idx][3] not in unique_banner_number:
                   unique_banner_number.append(list_of_lists[idx][3])
        return unique_banner_number


    def revenueCalculation(unique_banner_number, list_of_lists):
       root = ET.Element("Banners")
       # Iterate for each unique banner
       for banner in unique_banner_number:
           events = {}
           total_price = 0
           # Iterate over whole list
           for idx in range(len(list_of_lists)):
               if (list_of_lists[idx][0] == 'sel'):
                    # Checking for specific unique banner
                    if (list_of_lists[idx][3] == banner):
                        # Collecting the request id for the specific banner in 'sel'
                        request_id = list_of_lists[idx][2]
                        event_id = list_of_lists[idx][1]
                        price = float(list_of_lists[idx][4])
                        if event_id in events:
                           events[event_id] += 1
                        else:
                           events[event_id] = 1
                        # Finding match for request id in 'cent'
                        for i in range(len(list_of_lists)):
                            if (list_of_lists[i][0] == 'cnt'):
                                if(list_of_lists[i][2] == request_id):
                                   event_id = list_of_lists[i][1]
                                   if event_id in events:
                                       events[event_id] += 1
                                   else:
                                        events[event_id] = 1
                                   if(int(event_id) == 1):
                                       total_price += price
           xmlG=XmlGenerator()                            
           xmlG.xmlGeneration(root=root, element="Banner", banner=banner,
                  total_price=round(total_price, 2), events=events, filename='.\\reportgenerator\\result\\output_file.xml')
