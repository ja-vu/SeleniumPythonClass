""""
1. combine multiple gcf files
2. Parse all different 7-8 terms
3. Calculate the latency for between each phase
4. export all numbers to excel sheet
"""

import glob

read_files = glob.glob("*.log")


def combineLogs():
    with open('gcf.log_combined.txt', "wb") as outfile:
        for f in read_files:
            with open(f, "rb") as infile:
                outfile.write(infile.read())


if __name__ == '__main__':
    combineLogs()

    with open('gcf.log_combined.txt', "r") as InputFile:
        Line = InputFile.readline()
        file = open("parsed_gcflog.txt",'w')

        while Line:
            #file.write("Test 1")
            if "FB_Recog_State recog_state=RECOG_STATE_ENDPOINT_DETECTED" in Line:
                file.write(Line)
            Line = InputFile.readline()