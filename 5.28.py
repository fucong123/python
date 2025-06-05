import threading
import time
import random

lock = threading.RLock()
students = 100
class MyThread(threading.Thread):
    def go(self):
        lock.acquire()
        global students
        if students<1:
            lock.release
            return False
        go_door = random.randint(1,3)
        students-=go_door
        name = threading.currentThread().getName()
        time.sleep(0.1)
        print(f"{name}出去了{go_door}个，还剩{students}人")
        lock.release()
        return students>0
    def run(self):
        while self.go():
            pass

threadList = []
for i in range(2):
    th = MyThread()
    th.setName(f'door{i}')
    th.start()
    threadList.append(th)



# import os
# import xml.etree.ElementTree as ET
# def m1(path):
#     name = []
#     str_line=""
#     list = os.listdir(path)
#     for i in list:
#         new_path=os.path.join(path,i)
#         tree = ET.parse(new_path)
#         root = tree.getroot()
#         filename = root.find('filename').text
#         new_name = os.path.join(path,filename)
#         str_line += new_name+"\t"
#         for obj in root.iter("object"):
#             cls_name = obj.findtext("name")
#             if cls_name not in name:
#                 name.append(cls_name)
#             cls_index = name.index(cls_name)
#             xmlbox = obj.find('bndbox')
#             point1=(int(xmlbox.find('xmin').text)+int(xmlbox.find('xmax').text))/2
#             point2=(int(xmlbox.find('ymin').text)+int(xmlbox.find('ymax').text))/2
#             width = int(xmlbox.find('xmax').text)-int(xmlbox.find('xmin').text)
#             high = int(xmlbox.find('ymax').text)-int(xmlbox.find('ymin').text)
#             str_line += f'{cls_index} ({point1} {point2}) ({width}, {high}) '
#         str_line +="\n"
#     return str_line
# if __name__ == '__main__':
#     path = r"D:\homework\data\data4\voc_imgs\Annotations"
#     str = m1(path)
#     print(str)
