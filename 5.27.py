# data = [
# ['path', 'x', 'y', 'w', 'h'],
# ['1.png', '100', '100', '200', '200'],
# ['2.png', '50', '100', '100', '100'],
# ['3.png', '200', '50', '150', '100'],
# ['4.png', '150', '100', '100', '100']
# ]


# with open("work.txt","w+",encoding="utf-8")as f1:
#     for i in data:
#         for x in i :
#             f1.write(x+"\t")
#         f1.write("\n")


# datadic={}
# with open("work.txt","r+",encoding="utf-8")as f1:
#     result = f1.readlines()
#     for i in result[1:]:
#         parts = i.strip().split('\t')
#         key = parts[0]  
#         x = parts[1]     
#         y = parts[2]     
#         w = parts[3]     
#         h = parts[4]
#         datadic[key] = [int(x), int(y), int(w), int(h)]
# print(datadic)  




# import yaml

# data={
# "train": r"D:\homework\data\data3\dataset_v2\train",
# "val": r"D:\homework\data\data3\dataset_v2\val",
# "nc": 3,
# "names":{"0": "smoke","1": "drink","2": "phone"}
# }
# with open("test.yaml","w+",encoding="utf-8")as f1:
#     yaml.safe_dump(data, f1)


















import os
import xml.etree.ElementTree as ET
path=r'C:\Users\Student\Desktop\data\outputs'
list = os.listdir(path)
for i in list:
    new_path=os.path.join(path,i)
    tree = ET.parse(new_path)
    root = tree.getroot()
    filename = root.find('filename').text
    size = root.find('size')
    width = int(size.find('width').text)
    height = int(size.find('height').text)
    obj = root.find('object') 
    cls = obj.find('name').text
    xmlbox = obj.find('bndbox')
    a = (int(xmlbox.find('xmin').text),
    int(xmlbox.find('xmax').text))
    b = (int(xmlbox.find('ymin').text),
    int(xmlbox.find('ymax').text))
    point1=(int(xmlbox.find('xmin').text)+int(xmlbox.find('xmax').text))/2
    point2=(int(xmlbox.find('ymin').text)+int(xmlbox.find('ymax').text))/2
    print(filename,width,height,cls,point1,point2)