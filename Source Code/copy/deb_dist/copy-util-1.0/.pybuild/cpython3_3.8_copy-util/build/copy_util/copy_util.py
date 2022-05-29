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

def copier(filename):
    if os.path.exists(filename):
        print(file_content)
        agg = open('aggregator.txt', 'w')
        cp = open('copy_{}'.format(filename), 'a')
        orig=open(filename,'r')

        file_content[filename]=[x.strip() for x in orig.readlines()]
        print(file_content)
        orig.seek(0)

        agg.write(str(file_content))
        agg.write('\n')
        for key,value in file_content.items():
            for i in value:
                agg.write(i)
                agg.write('\n')

        for i in orig.readlines():
            cp.write(i)
            cp.write('\n')

        agg.close()

        cp.close()
        orig.close()

        # file = open(filename, 'r')
        # file_content[filename] =[x.strip() for x in file.readlines()]
        # file.close()

        # with open('list.txt', 'w') as f:
        #     for key, value in file_content.items():
        #         f.write(key+'\n')
        #
        # with open("file_content.json", "w") as outfile:
        #     json.dump(file_content, outfile)
        os.system('rm -rf {}'.format(filename))

    else:
        agg = open('aggregator.txt', 'r')
        open('copy_{}'.format(filename), 'w').close()
        cp = open('copy_{}'.format(filename), 'a')
        print('file:',file_content)
        for i in agg.readlines():
            if i.strip() in file_content[filename]:
                cp.write(i+'\n')

        agg.close()
        cp.close()
        
def main():
    copier(str(sys.argv[1]))

if __name__ == '__main__':
    copier(str(sys.argv[1]))
