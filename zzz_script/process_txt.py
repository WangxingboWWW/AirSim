import os
import shutil
if __name__ == '__main__':
  file = open('airsim_rec.txt')
  
  while 1:
    line_data = file.readline()
    if not line_data:
      break
    line_data_list = line_data.split()
    x = line_data_list[1]
    y = line_data_list[2]
    z = line_data_list[3]
    print(x, y, z)
  file.close()
