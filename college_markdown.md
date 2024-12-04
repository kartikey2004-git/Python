whenever we open a file using open assign to that file , file gets temporarily stored in memory or in buffer

Open a file 
f = open("path","access mode)


path parameter of open function can be defined in two ways 
1. By directly mentioning the name of file(ex file1.txt)
(The file has to be located in same folder where python file exists)
2. The complete path of the file is added with 
f = open("path", file path for ex : "C:\Users\karti\Pictures\Screenshots\OneDrive\Desktop\Javascript projects\projects js\Toast Notificaiton")

different access modes of file handling in python
1. r(used for read data from particular file if exists(only text formats)) . The handle in r mode is placed at the beginning of the
 file and if file does not exists , give error and cmd line prompt that is file not found

2. w(used for read data from particular file if file not exists new file will be created as mentioned in path)
(The handle in w mode is placed at the beginning of the
 file)
3. a(appending character/ data to pre-existing file overwrite ho jata hai)
(if file not exists new file will be created as mentioned in path)
(The handle in w mode is placed at the last of the
 file)

4. r+(both perform reading and writing operations in file but file exists honi chahiye and through an exception in case of non-existing file)(The handle in w mode is placed at the beginning of the
 file)
5. w+(both perform reading and writing operations in file but file exists honi chahiye and create a file if having a non-existing file)(The handle in w mode is placed at the beginning of the
 file)
6. a+
7. rb(reads in binary in file) if we use r access mode then the binary data would be read in characters or text
8. wb(write in binary in file)

If we are using a open function in file handling , It is mandatory tob close the file , or use excpetion handling in order to avoid exception and error

```Python
with open ("file name", access mode) as f
      f.read()
```

if we are using with statement for opening a file theere is no need to handle the exception or close the file it itself takes care of releasing the resources (memory, identifiers)



reading a file
read()
readlines()
readline()



In Python, read(), readlines(), and readline() are methods used to read from a file. Each of these methods works differently:

1. read()
Description: Reads the entire contents of a file as a single string.

```Python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```
Use Case: When you need to read the entire file content at once. This is suitable for small files, but for large files, it can consume a lot of memory.


2. readlines()
Description: Reads the entire file and returns a list where each element is a line from the file.

```Python
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
```

Use Case: When you want to process each line of the file as an item in a list. This is useful when you need to iterate over the lines but still want all of them in memory.

3. readline()
Description: Reads a single line from the file. Each time it's called, it reads the next line.
```Python
with open('example.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()
```

Use Case: When you want to read and process the file line by line, especially for large files, so you don't load the entire file into memory at once.


Summary:
read(): Reads the whole file at once.
readlines(): Reads all lines and returns them as a list.
readline(): Reads one line at a time.
You can choose based on whether you need to process the whole file at once or line by line.

read(): it reads all the data from the text file and return it in string format 
the parametric value represnts the no of bytes and it will return the mention bytes in string format only

readline(): will return a single line into string format
