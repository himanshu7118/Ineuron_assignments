1.	Create a list called years_list, starting with the year of your birth, and each year thereafter until the year of your fifth birthday. For example, if you were born in 1980. the list would be years_list = [1980, 1981, 1982, 1983, 1984, 1985].
Ans: [1999,2000,2001,2002,2003]

2.	In which year in years_list was your third birthday? Remember, you were 0 years of age for your first year.
Ans: years_list[2]

3.In the years list, which year were you the oldest?
Ans:  years_list[-1]
                                                                                                                                                                                                                     
4.	Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".
Ans: things = ["mozzarella", "cinderella", "salmonella"]

5.	Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?
Ans: things = ["mozzarella", "cinderella", "salmonella"]
person = []

for i in range(len(things)):
  person.append(things[i].upper())

print(person)


6.	Make a surprise list with the elements "Groucho," "Chico," and "Harpo."
Ans: surprise = [ "Groucho”,"Chico","Harpo"]

7.	Lowercase the last element of the surprise list, reverse it, and then capitalize it.
Ans: print(surprise [-1].lower())

8.	Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is chien, cat is chat, and walrus is morse.
Ans: esf = {
“dog”:” chien”,
“cat”:” chat”,
“walrus”:” morse” }

9.	Write the French word for walrus in your three-word dictionary e2f.
Ans: e2f[‘walrus’]
Which is morse.

10.	Make a French-to-English dictionary called f2e from e2f. Use the items method.
Ans:  e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
f2e = {}
for english, french in e2f.items():
    f2e[french] = english

11.	Print the English version of the French word chien using f2e.
Ans: f2e[‘chien’]
Which is 'dog'.

12.	Make and print a set of English words from the keys in e2f.
Ans:  print(esf.values())

13.	Make a multilevel dictionary called life. Use these strings for the topmost keys: 'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys refer to empty dictionaries.
Ans:
Life = {
'animals': {
'cats':[ 'Henri', 'Grumpy','Lucy'],
'octopi': {} ,
'emus': {}},
'plants' : {},
'other': {}
}

14.	Print the top-level keys of life.
Ans: print(Life.keys())
dict_keys(['animals', 'plants', 'other'])


15.	Print the keys for life['animals'].
Ans: print(Life['animals'].keys())
dict_keys(['cats', 'octopi', 'emus'])


16.	Print the values for life['animals']['cats']
Ans:  print(Life['animals']['cats'])
['Henri', 'Grumpy', 'Lucy']



