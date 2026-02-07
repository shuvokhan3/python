#create a csv file
import csv
#data
data = [
    ["name","salary", "designation", "department","location"],
    ["shuvo",344,"se","it","parish"]
]

with open("csvfile.csv","w",newline="") as csvfile:
    csv_file = csv.writer(csvfile)
    csv_file.writerows(data)
    print("file created successfully")


with open("csvfile.csv","r",newline="") as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        print(row)

