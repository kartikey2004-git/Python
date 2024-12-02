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