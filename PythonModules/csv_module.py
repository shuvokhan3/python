import csv

with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'Los Angeles'])

    


    
with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row) 
