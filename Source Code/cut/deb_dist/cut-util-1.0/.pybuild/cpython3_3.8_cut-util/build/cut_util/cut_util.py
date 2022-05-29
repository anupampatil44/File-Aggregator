import sys
import os
import json

try:
    with open('aggregator.txt', 'r') as fh:
        json_file=str(fh.readlines()[0])
        json_file=eval(json_file)
        file_content=json_file

except Exception as e:
    print(e)
    file_content={}

def cutter(filename):
    global file_content
    copyf=file_content.copy()
    copyf.pop(filename)
    agg = open('aggregator.txt', 'w')
    agg.write(str(copyf))
    agg.write('\n')

    cut=open('cut_{}'.format(filename),'w')
    for key,value in file_content.items():
        if key!=filename:
            for i in value:
                agg.write(i+'\n')
        else:
            for i in value:
                cut.write(i+'\n')

    file_content.pop(filename)

    agg.close()
    cut.close()

def main():
    cutter(str(sys.argv[1]))

if __name__ == '__main__':
    main()
