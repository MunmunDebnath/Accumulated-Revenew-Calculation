import json
import os

class ListExtactor():

   def creatlistfromtext(inputfilename)->list:
      list_of_lists=[]
      with open(inputfilename) as f:
         for line in f:
            temp_list = [elt.strip() for elt in line.split(':')]
            inner_list = []
            inner_list.append(temp_list[0])
            temp_list = [elt.strip() for elt in temp_list[1].split(',')]
            for i in range (len(temp_list)):
               inner_list.append(temp_list[i])
            list_of_lists.append(inner_list)

      return list_of_lists      

   def convertInputFileType(inputfilename,outputfilepath):

      jsonDict={}

      with open(inputfilename) as fh:
        for line in fh:
           keyName, valueItem = line.strip().split(":")
           if keyName not in jsonDict.keys():
              jsonDict[keyName]=[valueItem]
           elif type(jsonDict[keyName]) == list:
              jsonDict[keyName].append([valueItem])    
           else:
              jsonDict[keyName] = [[jsonDict[keyName]], [valueItem]]
   
      listC=ListExtactor()
      listC.create_json(outputfilepath, 'input_json.json', jsonDict)
 

   def create_json(target_path, target_json_file, json_data):
      if not os.path.exists(target_path):
         try:
           os.makedirs(target_path)
         except Exception as excep:
           print(excep)
         raise
      with open(os.path.join(target_path, target_json_file), 'w') as resultFile:
         json.dump(json_data, resultFile) 
         resultFile.close()  

