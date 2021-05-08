
# Command Line Mode
Command line mode differs a bit from the other modes, in the sense that it can impact the entire text file. Many commands can be given a range of lines to act upon. We can specify the start and end of a range with either a line number, a mark, or a pattern.

Command | Significance
---|---
:[Number] | Takes cursor to the line number specified
:% | `Has a special meaning` - Refers to all lines in the file
:%s/[Target]/[Target_Update] | s -> Substitute, the Target with Target_Update 
:. | Back to line where the cursor was placed
:bnext | Takes to next file in the buffer
Ctrl + F | Vim command history
:shell | Open up terminal
:jumps | Shows list of previous jumps
:set ignorecase | Make vim search pattern case insensitive


## Search Related
Command | Significance
---|---
/{word} | Searches for word in the entire file
n | Previous search
N | Next search

## Steps to modify words
Step | Command | Significance
---|---|---
1 | *,cw (str) | To replace the first string
2  | :%s//Ctrl+r Ctrl+w/g | Replaces the last changed


## VIM Register
Command | Significance
---|---
:reg | Opens the register
"[a-z]{command} | Saves to [a-z] register basis the command
"[A-Z]{command} | Appends to [A-Z] register basis the command


## Pasting from System Clipboard

Command | Significance
---|---
"+{cmd} | Saves or Obtains from system clipboard
"*{cmd} | Saves or obtains from secondary clipboard

