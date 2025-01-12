File Handling

open() function takes two parameters; filename, and mode.

```bash
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
```

you can specify if the file should be handled as binary or text mode

```bash
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
```

To open the file, use the built-in open() function.

The open() function returns a file object


By default the read() method returns the whole text, but you can also specify how many characters you want to return.


Read Lines

You can return one line by using the readline() method


By looping through the lines of the file, you can read the whole file, line by line

It is a good practice to always close the file when you are done with it.

To write to an existing file, you must add a parameter to the open() function

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content

the "w" method will overwrite the entire file.



Create a New File

use the open() method

"x" - Create - will create a file, returns an error if the file exists

"a" - Append - will create a file if the specified file does not exists

"w" - Write - will create a file if the specified file does not exists


Python Delete File

To delete a file, you must import the OS module, and run its os.remove() function

Check if File exist

To avoid getting an error, you might want to check if the file exists before you try to delete it

Delete Folder
To delete an entire folder, use the os.rmdir() method

You can only remove empty folders.