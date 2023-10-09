#python script that reads
#n first lines of a file

file_name=input("Type the name of the file: ");
lines=int(input("The number of lines to be print: ");
try:
  f=open(file_name,"r");
  for i in range(lines):
    line=next(file).strip();
    print(line)
  f.clsoe();
except:
  print("Error opening file.");
f.close();
print("Done");
