#oan 

Symbol | Relevance
---|---
. | Any Character except New Line
\d | Digit (0-9)
\D | Matches any non-digit character, [\^0-9]
\w | Word Character (a-z, A-Z, 0-9, _)
\W | Not a word Character
\s | Whitespace (space, tab, newline)
\S | Not a Whitespace (space, tab, newline)
\b | Word Boundary
\B | Not a Word Boundary
^ | Beginning of a string
$ | End of a string
[] | Matches Characters in a brackets
[^ ] | Matches Characters Not in a brackets/ Complement
\| | Either Or
\( ) | Group
* | 0 or More
+ | 1 or More
? | 0 or More
{3} | Exact Number
{3,4} | Range of Numbers (Minimum, Maximum)


## Tagging in Python

You can tag python regex

```python
re_names3 = re.compile(r'''^
                           (?P<first>[a-zA-Z]+)
                           \s
                           (?P<middle>[a-zA-Z]+\s)?
                           \s*
                           (?P<last>[a-zA-Z]+)
                           $
                        ''',
                        re.VERBOSE)
print(re_names3.match('Rich Vuduc').group('first'))
```

```python
import re 

pattern = re.compile() # Compiles a pattern
matches = pattern.search() #Searches for the pattern
matches.group() # Gives the group
matches.start() # Start of the search
matches.end() # End of the search
matches.span() # Span of the serach
```

1.  `match()` - Determine if the regular expression (RE) matches at the beginning of the string.
2.  `search()` - Scan through a string, looking for any location where this RE matches.
3.  `findall()` - Find all substrings where the RE matches, and returns them as a list.
4.  `finditer()` - Find all substrings where the RE matches, and returns them as an iterator.

```python


```