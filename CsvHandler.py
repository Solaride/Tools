import csv

def getFileName():
    while True:
        fileName = input("Enter parameters file name (Empty for parameters.csv): ")
        if (fileName == ""):
            return "parameters.csv"
        if fileName.endswith(".csv"):
            return fileName
        print("File name must have a .csv ending")

def writeParameters(a, b, c):
    print("\nWriting file:")
    fileName = getFileName()

    with open(fileName, mode="w", newline="") as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow("abc")
        csvWriter.writerow([a, b, c])


def readParameters():
    print("\nReading file:")
    fileName = getFileName()

    with open(fileName) as csvFile:
        csvReader = csv.reader(csvFile)

        rows = list(csvReader)
        dataRow = rows[1]

        a = float(dataRow[0])
        b = float(dataRow[1])
        c = float(dataRow[2])

        return a, b, c
