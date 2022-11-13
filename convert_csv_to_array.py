import json

jsonFile = open("./src/data/characterData.json")
data = json.load(jsonFile)

print("Starting, please wait until complete")

with open("genshinTeamsNamed.csv",'r') as f:
    with open("./src/data/teampresets.ts",'w') as f1:
        f.readline() # skip header line
        f1.write("export const teamPresets = [\n")
        for line in f:
            line = '\t[' + line

            for i in data:
                if i["id"] != 39:
                    line = line.replace(i["shortName"], str(i["id"]))

            # Get rid of the trailing newline (if any).
            line = line.rstrip('\n')
            line += '],\n'
            f1.write(line)
        f1.write("];")
    f1.close()
f.close()

jsonFile.close()

print("Job Complete")

exit(0)