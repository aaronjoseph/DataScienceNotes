## Visual Mode

There are set of functionalities that work in visual mode. Namely in terms of 

Command | Significance
---|---
v | Enable character-wise Visual Mode
V | Enable Line-wise Visual Mode
Ctrl + v | Enable block-wise Visual Mode
viw | Selects the word
gv | Select last visual selection
S{char} | Surround - Surrounds the selection with the char

## Selection Related
Here use v before applying the below comands

Keystroke | Significance | Keystroke | Significance
----------|--------------|----------|-------------
a) or ab  | A pair of (parentheses) | i) or ib  | Inside of (parentheses)
a} or aB  | A pair of {braces} | i} or iB | Inside of {braces}
a]        | A pair of [brackets] | i]      | Inside of [brackets]
a>        | A pair of angle brackets <> | i> | Inside of angle brackets <>
a'        | A pair of 'single quotes' | i' | Inside of 'single quotes'
a"        | A pair of "double quotes" | i" | Inside of "double quotes"
a`        | A pair of `backticks` | i`     | Inside of `backticks`
at        | A pair of &lt;xml&gt;tags&lt;/xml&gt; | it  | Inside of &lt;xml&gt;tags&lt;/xml&gt;
aw        | A word plus spaces | iw | Inside a word
aW        | A WORD plus spaces | iW | Inside a WORD
as        | A sentence plus spaces | is | Inside a sentence
ap        | A paragraph plus blank lines | ip | Inside a paragraph

## Search Related 

Command | Significance
---|---
`/{text}<CR>`| After entering visual mode, this mode will allow for selection upto the {text} 