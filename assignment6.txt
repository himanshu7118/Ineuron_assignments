1.	What are escape characters, and how do you use them?
Ans: Escape characters:
\",\', \\,\n, \r, \t, \b, \f, \ooo, \xhh
Ex:
txt = "We are the so-called \"Vikings\" from the north."
txt = 'It\'s alright.'
txt = "This will insert one \\."
txt = "Hello\nWorld!"
txt = "Hello\rWorld!"
txt = "Hello\tWorld!"
txt = "Hello \bWorld!"
txt = "\110\145\154\154\157"
txt = "\x48\x65\x6c\x6c\x6f"


2.	What do the escape characters n and t stand for?
Ans:  n stands for new line. t stans for tab.

3.	What is the way to include backslash characters in a string?
Ans:  \\ (backslash) we can backlash character in string.

4.	The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the word Howl's not escaped a problem?
Ans: its wrong symbol you passed here original character is \’.

5.	How do you write a string of newlines if you don't want to use the n character?
Ans: with the help of \r.

6. What are the values of the given expressions?
'Hello, world!'[1]
'Hello, world!'[0:5]
'Hello, world!'[:5]
'Hello, world!'[3:]

Ans: ‘e’
‘Hello’
‘Hello’
‘lo,world!’

7. What are the values of the following expressions?
'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()
Ans:
‘HELLO’
True
‘hello’

8. What are the values of the following expressions?
'Remember, remember, the fifth of July.'.split()
'-'.join('There can only one.'.split())
Ans: 
['Remember,’,’ remember,’ the’, ‘fifth’,’of’,’July.’]
‘There-can-only-one.’

9. What are the methods for right-justifying, left-justifying, and centering a string?
Ans: ljust(), rjust() , center()
Here inside you can define width and character.

10. What is the best way to remove whitespace characters from the start or end?
Ans: .strip() method you can use to remove white space from the start and end.

