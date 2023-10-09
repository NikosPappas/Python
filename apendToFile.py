#a script that appends
#data at the end of a file
file_name=input("Type the name of the file: ");
try:
  f=open(file_name,"a");
  line=input("Type some text: ");
  f.write(line);
  f.close();
  f=open(file_name,"r");
  print(f.read());
  f.close();
except:
  print("Error opening file.");
print("Done");
