import json
filename=input("Enter the file name : ")
data={}
with open(filename+'2.json') as json_file:
    copy=json.load(json_file)

with open('master.json') as json_file:
    master=json.load(json_file)

for key in copy:
        
    print(key)
    value=copy[key]
    print("The key and value are ({}) = ({})".format(key, value))
