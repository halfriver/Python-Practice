# Green Eggs and Ham Text Corrector
# 4 Nov 2019

mistakes = 0
text = []
text_corrected = []

# open text file of the story to read
f = open("GreenEggsandHam.txt", "r")

# copy text to list to work with and close original file
for line in f:
    text.append(line)
f.close()

for line in text:
    # split each line on the incorrect "i", increment to mistakes counter, reconstitute to correct
    if "i " in line:
        line = line.split("i ")
        mistakes += (len(line) - 1)
        line = "I ".join(line)

    # split each line on "-i-am", increment to mistakes counter, reconstitute to correct
    if "-i-am" in line:
        line = line.split("-i-am")
        mistakes += (len(line) - 1)
        line = "-I-Am".join(line)

    text_corrected.append(line)

# create new file if it doesn't already exist and write corrected text to it
new = open("GreenEggsandHam_corrected.txt","w")
for line in text_corrected:
    new.write(str(line))
new.close()

print(str(mistakes) + " mistakes have been corrected and the corrected text has been written to GreenEggsandHam_corrected.txt")
