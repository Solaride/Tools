def generateFile(values):
    with open("pedalmap.h", "w") as f:
        f.write("float pedalmap[" + str(len(values)) + "] = {0, ")
        for i in range(2, len(values)):
            if (i % 4 == 0):
                f.write("\n\t")

            f.write(str(values[i]) + ", ")
        f.write("1.0};")

