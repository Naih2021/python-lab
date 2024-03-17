import csv

with open("week23.csv", 'w') as f:
    pen = csv.writer (f)
    header = ["Name","cell phone", "city"]
    pen.writerow(header)
    pen.writerow(["Esnai", "813 550 222]", "Gainesville"])
f.close