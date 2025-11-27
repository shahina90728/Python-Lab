import csv
csv_col=['RollNo','Name','Department']
dict_data=[{'RollNo':1,'Name':'Alex','Department':'MCA'},
           {'RollNo':2,'Name':'Aleena','Department':'MCA'},
           {'RollNo':3,'Name': 'Minu','Department':'MCA'},
           {'RollNo':4,'Name':'Ebin','Department':'MCA'},
           {'RollNo':5,'Name':'Jimmy','Department':'MCA'}]
csv_file="student.csv"
try:
  with open(csv_file,'w')as file1:
    writer=csv.DictWriter(file1,fieldnames=csv_col)
    writer.writeheader()
    for data1 in dict_data:
       writer.writerow(data1)
       
except IOError:
    print("I/O error")
data1 = csv.DictReader(open(csv_file))
print("CSV file as a dictionary:\n")
for row in data1:
     print(row)
