import csv
import re

#The directory/path of input and output data files
FilePath="/Users/YourID/"
#FilePath="/YourFilePath/"


filenameTarget=FilePath+"BRC12105-CopyofOrderFamSpec-MENUS1-3_011619.csv"

filenameTest=FilePath+"BRC12105-IRDAvianHost1copy.txt"

filenameCOMMON_MATCH=FilePath+"COMMON_MATCH.txt"

filenameSCI_MATCH=FilePath+"SCI_MATCH.txt"

filenameFAIL=FilePath+"FAIL.txt"

fields=[]
rows=[]

ffail=open(filenameFAIL, 'w')
fcommon=open(filenameCOMMON_MATCH, 'w')
fsci=open(filenameSCI_MATCH, 'w')

f=open(filenameTest, 'r')

#for a csv file created with windows comma separated 
#with open(filenameTarget, 'r') as csvfile:

#for a csv file created with MS-DOS comma-separated csv
with open(filenameTarget, 'rU') as csvfile:
 csvreader=csv.reader(csvfile)

 fields=csvreader.next()

 for row in csvreader:
  rows.append(row)

 print("Total number of rows: %d"%(csvreader.line_num))

print("Field names are: " + " , ".join(field for field in fields))

p0=re.compile("\"+")
p1=re.compile(" sp\.")
p2=re.compile('\s\(.*\)')
p3=re.compile('\/')

for term in f:
 row4match=0
 row5match=0
 term=term.strip().lower()

 for row in rows:

   row4=row[3].strip().lower()
   row4=p0.sub("", row4)
   row4=p1.sub("", row4)
   row4=p2.sub("", row4)
   row4=p3.sub(" ", row4)

   row5=row[4].strip().lower()
   row5=p0.sub("", row5)
   row5=p1.sub("", row5)
   row5=p2.sub("", row5)

   if (term==row4 and row4match==0):
    print("row4 matched !!!!")
    print("term " + term + "\n")
    print("row4 " + row4 + "\n")
    row4match=1
    fcommon.write(term + "\n")
   elif (term==row5 and row5match==0):
    print("row5 matched !!!!!")
    print("term " + term + "\n")
    print("row5 " + row5 + "\n")
    row5match=1
    fsci.write(term + "\n")

 if (row4match==0 and row5match==0):
  print("both row4 and row5 are not matched>>")
  print("term " + term + "\n")
  print("row4 " + row4 + "\n")
  print("row5 " + row5 + "\n")
  ffail.write(term + "\n")

 print('\n')

fcommon.close()
ffail.close()
fsci.close()
