Command | Significance
--- | ---
:h vimtutor | Built in documentation of Vim
x | Deletes the character under the cursor
. | Repeats last command
u | Undo Last command
dd | Delete the line
<G | Decrease Indentation till the end of the file
>G  |  Increase Indentation till the end of the file
a | Append
A ($a) | Append at the end of the line
$ | End of the line
J | Merge the next line
ga | To obtain the Hex or Octal code of the data
gf | Go to File under the cursor -> Opens directory to refer files from
Ctrl + ] | Take to the function where it was invoked
`R` | Replace Mode

## Global Marks

Command | Significance
---|---
m{letter} | To place a mark in the codebase Lowercase stores to local and uppercase are Global
'{letter} | Takes back to the mark 



## Windows Related

Command | Significance
---|---
Ctrl + w + s | Horizontal Split
Ctrl + w + v | Vertical Split
Ctrl + w + w | Cycle between open windows
Ctrl + w + h | Cycle between open windows
Ctrl + w + w | Cycle between open windows
Ctrl + w + c | Close the Active window
Ctrl + w + o | Keep the active window, closing all others
Ctrl + w + = | Equalize width and height of all windows
Ctrl + w + _ | Maximise height of current window
Ctrl + w +\|  | Maximise height of current window


## Positioning

Command | Significance
---|---
$ | End of line
\| or 0 | Start of line
w | Forward to start of next word
b | Backward to start of current or previous word
e | Forward to end of next word
ge | Backward to end of previous word
% | Move between the ends of parenthesis

## Insert Mode

Command | Significance
---|---
a | Insert after the cursor
A | Insert at the end of the line
i | Insert before the cursor
S | Delete the line and append
s | Delete the word at cursor and append

## Triggers

Command | Significance
---|---
c | Change
d or x | Delete
y | Yank into register
g~ | Swap case
gu | Make Lowercase
gU | Make Uppercase
< | Shift Left
> | Shift Right
= | Autoindent
! | Filter lines through an external program

## Searching 

Command | Significance
---|---
f{char} | Find the next character `Line-wise`
F{char} | Find the previous character `Line-wise`
; | Repeat the last search forward
, | Repeat the last search backward
* | Searches for similar text where the cursor is placed
(*) n | Searches for next element

## Deleting & Pasting words

Command | Significance
---|---
db | Delete word/ part of word before the string
dl | Delete a character
daw | 'Delete a word' - deletes the whole word
dap | Delete a paragraph
cW | Deletes word, and allows for new edits
c | Delete and Insert
d/{word}<CR> | Delete from the cursor till the first occurance of the word `before the word`
p | Paste  

## Difference between s, c & r

Command | Significance
---|---
`s` (**s**ubstitute) | will delete the current character and place the user in insert mode with the cursor between the two surrounding characters. `3s`, for example, will delete the next three characters and place the user in insert mode
`c` (**c**hange) | takes a vi/vim motion (such as `w`, `j`, `b`, etc.). It deletes the characters from the current cursor position up to the end of the movement. Note that this means that `s` is equivalent to `cl` (vim documentation itself claims these are synonyms)
`r` (**r**eplace) | never enters insert mode at all. Instead, it expects another character, which it will then use to replace the character currently under the cursor.

## Adding or Subtracting Numbers

Command | Significance
---|---
(Number) Ctrl-a | Adds number to Number -> Nearest
(Number) Ctrl-x | Subtract number to Number

# Compund Command
There are commands that can be done with fewer keystrokes - **compund commands**. 

Compound Command | Equivalent in Longhand
-----| -----
C | c$
s | cl
S | ^ C
I |  ^ i
A | $a
o | A<CR>
O | ko

## Undoing Or Repeating

Intent | Act | Repeat | Reverse
---|---|---|---
Make a change | {edit} | . | u
Scan line for next character | f{char}/t{char} | ; | ,
Scan line for previous character | F{char}/T{char} | ; | ,
Scan document for next match | /pattern<CR> | n | N
Scan document for previous match |?pattern<CR> | n | N
Perform substitution | :s/target/replacement | & | u
Execute a sequence of changes | qx{changes}q | @x | u