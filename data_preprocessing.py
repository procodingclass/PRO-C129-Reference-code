# import csv
import csv
  
# open input CSV file as source

with open("final_1.csv", "r") as source:
    reader = csv.reader(source)

# open output CSV file as result    
    with open("final_2.csv", "w") as result:
        writer = csv.writer(result)
        for row in reader:
            if row!='':
                writer.writerow((row[0], row[1], row[2], row[3], row[4],row[5], row[6], row[9]))
            else:
                pass


