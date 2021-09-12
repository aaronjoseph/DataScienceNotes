Shell Commands

[[tr - Shell]]
[[Cut - Shell]]
[[grep - Shell]]
[[Xargs]]

## Shortcuts and Tricks

```shell
! ls # It will run the last ls command
! 123 # Runs the 123rd command stored in history
sudo !! # Will run the last command with sudo
Ctrl + R -> Reverse Search
man ls ; tldr ls -> Easier to read manual compared to man
```

## Network Commands

```shell
ping twitter.com # Tests if the host is reachable
hostname # Name of the device host
ip a # To find your IP Address
finger # Tells who all are logged in
netstat -a # Shows all listening port
traceroute google.com # Shows the route a packet took to reach the host
```

## Enviroment Variable

> Global Variables are all caps, `always define variables as small caps`

```shell
printenv #List of all global variable
printenv HOME #Find the home variable config
echo $HOME #Gets the variable config
unset variable #Removes the variable

# Adding to PATH Variable for easy execution
PATH=$PATH:/path/to/specify
```

Additionally, you can add the PATH to Bashrc

```shell
if [-d "$HOME/.bin"];
	then PATH="$HOME/.bin;$PATH"
fi

# Here the code above checks if the folder exists
# If so, then adds it to PATH
```