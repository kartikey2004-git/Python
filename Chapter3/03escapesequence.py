a = "Harry is a good boy \n but not a bad\t boy"
print(a)

# Here are some escape sequence
# "" ,\t, \n , \"random text\" , \\


#baad mein padhne ke liye useful hoga

# In Python, escape sequences are used to represent certain characters within strings that cannot be typed directly or are reserved for special meanings. These sequences begin with a backslash (`\`), followed by a character that indicates the desired result.

# Here are common escape sequences in Python:

# ### 1. **Newline (`\n`)**
#    - Represents a new line.
#    - Example: `"Hello\nWorld"` produces:
#      ```
#      Hello
#      World
#      ```

# ### 2. **Tab (`\t`)**
#    - Represents a horizontal tab (indentation).
#    - Example: `"Hello\tWorld"` produces: 
#      ```
#      Hello   World
#      ```

# ### 3. **Backslash (`\\`)**
#    - Escapes the backslash itself.
#    - Example: `"This is a backslash: \\"` produces: 
#      ```
#      This is a backslash: \
#      ```

# ### 4. **Single Quote (`\'`)**
#    - Escapes single quote inside single-quoted strings.
#    - Example: `'It\'s a test'` produces: 
#      ```
#      It's a test
#      ```

# ### 5. **Double Quote (`\"`)**
#    - Escapes double quote inside double-quoted strings.
#    - Example: `"He said, \"Hello!\""` produces: 
#      ```
#      He said, "Hello!"
#      ```

# ### 6. **Carriage Return (`\r`)**
#    - Moves the cursor to the beginning of the line.
#    - Example: `"Hello\rWorld"` replaces `Hello` with `World` in the same line:
#      ```
#      World
#      ```

# ### 7. **Bell/Alert (`\a`)**
#    - Produces a bell sound or beep (depends on system settings).
#    - Example: `"\a"` may trigger a system alert sound.

# ### 8. **Backspace (`\b`)**
#    - Moves the cursor back one space, erasing the previous character.
#    - Example: `"Hello\bWorld"` produces: 
#      ```
#      HellWorld
#      ```

# ### 9. **Form Feed (`\f`)**
#    - Advances the paper feed in printers to the next page (rarely used in modern programming).
#    - Example: `"Hello\fWorld"` may format output depending on context.

# ### 10. **Octal Value (`\ooo`)**
#     - Represents a character using its octal value.
#     - Example: `"\101"` produces: 
#       ```
#       A
#       ```

# ### 11. **Hexadecimal Value (`\xhh`)**
#     - Represents a character using its hexadecimal value.
#     - Example: `"\x41"` produces:
#       ```
#       A
#       ```

# ### 12. **Unicode Character (`\uXXXX` and `\UXXXXXXXX`)**
#     - Represents a Unicode character using a 16-bit (`\u`) or 32-bit (`\U`) hexadecimal value.
#     - Example: `"\u2764"` produces the Unicode heart character:
#       ```
#       ❤
#       ```

#     - Example with 32-bit Unicode: `"\U0001F600"` produces:
#       ```
#       😀
#       ```

# ### 13. **Raw Strings (`r"..."` or `R"..."`)**
#     - A raw string ignores escape sequences (except for `\\` and `\"`), which can be useful for regular expressions and file paths.
#     - Example: `r"C:\new\folder"` produces:
#       ```
#       C:\new\folder
#       ```

# ### 14. **Null Character (`\0`)**
#     - Represents the null character.
#     - Example: `"\0"` is often used to indicate the end of a string in low-level programming.

# These escape sequences allow for flexibility in formatting and controlling output in Python strings.