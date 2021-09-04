Xargs allows you to execute to pass standard input as an argument to another commands.
It is more of a piping command. Xargs are sometimes faster than exec command
**Command 1 | xargs command 2** `Herein command 1 can be fed into command 2`

```shell
seq 5 | xargs # This command will print 1 to 5, standard xargs is echo
ls | xargs ls # This will be recursive ls
ls | xargs -I {} echo "/home/dt/{}" # Here, it will print ls with the prefix
seq 100 | xargs -I {} touch  {}.txt # Creates 100 txt files from 1.txt to 100.txt
```

