Grep is used for pattern matching within a file.
Grep cannot search a binary & directory

Similar to [[Regex]]

```shell
grep the .bashrc # Returns every line in bashrc with the text the
grep -w the .bashrc # Here you are looking for specific pattern
grep test . # This will fail, grep doesn't work on directory
grep [aeiou] .bashrc # Return every line that has vowel
grep [x-z] .bashrc # return every line that has x,y & z
grep -A 3 test .bashrc # Here, it will check for the text after the 3rd line and before with a dash
grep -i test .bashrc # Making it case insensitive

```


### Grep Regex Examples

```shell
grep test$ word.txt #searches for test in the end of line
grep ^test word.txt #seraches for test in the start of line
grep [0-9][0-9][0-9]$ word.txt #Outputs lines ending with atleast 3 numbers
grep ^$ word.txt #Outputs blank lines
grep -v ^$ word.txt # -v does an invert search, which find non-blank lines
```