try:
    with open('aggregator.txt', 'r') as fh:
        json_file=str(fh.readlines()[0])
        json_file=eval(json_file)
        file_content=json_file

except Exception as e:
    file_content={}

def list():
    print("Listing files in aggregate.txt:")
    for key,value in file_content.items():
        print(key)

def main():
    list()
    
 
if __name__ == '__main__':
    main()
