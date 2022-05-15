from Plot import init

from FitData import fit
from CsvHandler import readParameters, writeParameters
from data import X, Y

def main():
    a, b, c = readParameters()

    #a, b, c = fit(f, X, Y)

    init(a, b, c)

if __name__ == "__main__":
    main()
