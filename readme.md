
## Goal:
Create a simple file aggregator. It takes a list of files and clubs them into a single file while keeping track of individual files.

## Setup:
Under the 'Deb Files' folder you will find all the deb files needed for performing the required operations. Each operation has its own deb package which you are required to install via the following command:
```
sudo dpkg -i <package_name>
```

## Operations:

1. ```add```: Adds the file passed in the argument to aggregator.txt and deletes the original file.
Syntax: ```add file1.txt```

2. ```copy_util```: This will keep the file passed in the aggregation.txt and create a copy of original file as copy_filename. If the file isn't added to aggregation.txt, it will be added to aggregation.txt first. 
Syntax: ```copy_util file1.txt```


3. ```cut_util```: This will remove file passed from aggregation.txt and create a separate file cut_filename which is exactly same as the original file.
Syntax: ```cut_util file1.txt```

4. ```list```:  This is a command without any arguement that lists all the files present in aggregation.txt.
Syntax: ```list```

**Note**: Certain keywords such as ```cut``` and ```copy``` are reserved words hence require different naming conventions hence the different names.

## Sample File Handling Output:
<img src= "/Output Screenshots/test_output.png"></img>
