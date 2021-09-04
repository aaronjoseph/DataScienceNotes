Cut help you to read through text files.

```shell
cut -c 1-10 filenamme # Here, cut will grab first 10 char of a text files
echo "This is a line of text" | cut -d ' ' -f5 # Go and grab the 5th field based on spaces
cut -d ':' -f2 /etc/passwd # Read the passwd file, seperate by ':' and grab the 2nd field f2

```