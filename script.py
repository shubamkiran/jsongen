import json

filename=input("Enter the file name you want to open : ")

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './'+ path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp,indent=3,sort_keys=True)
data={}
with open(filename+".json") as myfile:
    for line in myfile:
        name, end = line.partition(":")[::2]
        beg=name.strip()
        if beg.find("}")==-1 and end.find("{")==-1 and beg.find("{")==-1:
            newbeg=beg.replace('"',"")
            data[newbeg] = "NULL"
            
        elif end.find("{}")!=-1:
            newbeg=beg.replace('"',"")
            data[newbeg]="NULL"
           
writeToJSONFile('./','master',data)

with open(filename+".json", 'r') as f:
        datastore = json.load(f)
writeToJSONFile('./',filename+"2",datastore)


       
                    
                                
            
            