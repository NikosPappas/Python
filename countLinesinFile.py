#script counting lines in file
file_name=input("Type the name of the file: ");
try:
  f=open(file_name,"r");
  count=0;
  while True:
    count+=1;
    line=f.readline();
    if not line:
      break;
  print("Total number of lines: ",count);
  f.close();
except:
  print("Error opening file.")
print("Done")
