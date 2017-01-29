import os
def rename_files():
   #(1) get file names from a folder
   file_list =  os.listdir(r"C:\Python27\prank\prank")
   print(file_list)
   saved_path = os.getcwd()
   print("current directory is"+saved_path)
   os.chdir(r"C:\Python27\prank\prank")
   #(2) for each file, reaname filename
   for file_name in file_list:
       print("old name "+file_name)
       print("New name "+file_name.translate(None,"0123456789"))
       os.rename(file_name,file_name.translate(None,"0123456789"))
   os.chdir(saved_path)
rename_files()
