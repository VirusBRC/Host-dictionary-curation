import csv
import re

#The directory/path of input and output data files
FilePath="/Users/userid/"

filenameTarget=FilePath+"BRC12104_IRDAvianHost_Excel.csv"
filenameOut1=FilePath+"Output1"
filenameOut2=FilePath+"Output2"

filenameOut1=open(filenameOut1, 'w')
filenameOut2=open(filenameOut2, 'w')

fields=[]
rows=[]

with open(filenameTarget, 'r') as csvfile:
 csvreader=csv.reader(csvfile)
 fields=csvreader.next()

 for row in csvreader:
  rows.append(row)
 print("Total number of rows: %d"%(csvreader.line_num))

print("Field names are: " + " , ".join(field for field in fields))

Number_Of_Lines=0
Count_CHARMatch=0
Count_CHARMatch=0
Count_WORDMatch=0

p00=re.compile("\"+")

p0=re.compile("\s*\;.*$")
p2=re.compile("\s*\(.*$")
p3=re.compile("\s*\[.*$")
p4=re.compile("\s*\{.*$")
p5=re.compile("\s*\;.*$")
p6=re.compile("\s*\:.*$")
p7=re.compile("\s*,.*$")

p10=re.compile("wild\s")
p11=re.compile("live bird market\s")
p12=re.compile("household\s")
p13=re.compile("broiler\s")
p14=re.compile("breeder\s")
p15=re.compile("feral\s")
p16=re.compile("backyard\s")
p17=re.compile("domesticated\s")
p18=re.compile("breeding\s")
p19=re.compile("farm\s" )
p20=re.compile("domestic\s")

for row in rows:
 row2=row[2].strip().lower()
 if (len(row)==4):
  row3=row[3].strip().lower()
  row2=row2+row3

 GB_HOST=row2
 CURATED_AVIAN_HOST=row[1].strip().lower()

 print("original--> "+row2)
 row2=p00.sub("", row2)
 row2=p0.sub("", row2)
 row2=p2.sub("", row2)
 row2=p3.sub("", row2)
 row2=p4.sub("", row2)
 row2=p5.sub("", row2)
 row2=p6.sub("", row2)
 row2=p7.sub("", row2)
 row2=row2.strip()

 Edit1_GB_Host=row2
 print("Edit1_GB_Host is " + Edit1_GB_Host)

 if (Edit1_GB_Host!=GB_HOST and Edit1_GB_Host==CURATED_AVIAN_HOST):
  Count_CHARMatch=Count_CHARMatch+1
  print("* first condition ")
  print("GB_HOST  = "+GB_HOST)
  print("Edit1_GB_Host  = "+ Edit1_GB_Host)
  print("CURATED_AVIAN_HOST  = "+CURATED_AVIAN_HOST)
  print("Count_CHARMatch = "+str(Count_CHARMatch)+"\n")
 else:
  print("* second condition ")
  row2=p10.sub("", row2)
  row2=p11.sub("", row2)
  row2=p12.sub("", row2)
  row2=p13.sub("", row2)
  row2=p14.sub("", row2)
  row2=p15.sub("", row2)
  row2=p16.sub("", row2)
  row2=p17.sub("", row2)
  row2=p18.sub("", row2)
  row2=p19.sub("", row2)
  row2=p20.sub("", row2)

  row2=row2.strip()

  Edit2_GB_Host=row2

  if (Edit2_GB_Host!=Edit1_GB_Host and Edit2_GB_Host ==CURATED_AVIAN_HOST):
    Count_WORDMatch=Count_WORDMatch+1

  if (Edit2_GB_Host !=CURATED_AVIAN_HOST):
    filenameOut2.write(GB_HOST+"\t"+Edit1_GB_Host+"\t"+Edit2_GB_Host+"\n")

 Number_Of_Lines=Number_Of_Lines+1


print("Number_Of_Lines = "+str(Number_Of_Lines))
print("Count_CHARMatch = "+str(Count_CHARMatch))
print("Count_WORDMatch = "+str(Count_WORDMatch))

filenameOut1.write(str(Number_Of_Lines)+"\t"+str(Count_CHARMatch)+"\t"+str(Count_WORDMatch))

filenameOut1.close()
filenameOut2.close()

