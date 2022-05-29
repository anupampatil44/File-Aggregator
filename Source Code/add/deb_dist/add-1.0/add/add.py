import sys
import os
import json

try:
    with open('aggregator.txt', 'r') as fh:
        json_file=str(fh.readlines()[0])
        json_file=eval(json_file)
        file_content=json_file

except Exception as e:
    file_content={}

def adder(filename):
    try:
        global listoffilesinagg
        global file_content

        file=open(filename,'r')

        file_content[filename] =[x.strip() for x in file.readlines()]
        file.seek(0)

        agg=open('aggregator.txt','w')
        agg.write(str(file_content))

        agg.write('\n')
        for key, value in file_content.items():
            for i in value:
                agg.write(i)
                agg.write('\n')
        agg.close()
        file.close()
        os.system('rm -rf {}'.format(filename))


    except Exception as e:
        print(e)

def main():
    adder(str(sys.argv[1]))
if __name__ == '__main__':
    main()