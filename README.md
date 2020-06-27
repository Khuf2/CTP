# CTP

This is a program that allows you to store people as entries in a simple
JSON file, which can be revisited and add to a database of your own rating
information. 

Later, sorting and searching will be implemented to allow for more smarter
presentation of the data. Users will also have the option to set their own rating
scale, rather than use the default scales.

Its also an option to migrate to a web app and implement a login system so that
each user's entries will be anonymous, but this will not happen in the near future.

************************************************************************
Usage:

************************************************************************

After you log in, the program operates out of a central menu loop.
In this menu, you can select different operations with shortcuts.

Shortcuts:		Operations:
ls			=	[list] name, gender, and CTP of all entries
add 		= 	[add] a new entry
edit		= 	[edit] an existing entry
del 		= 	[delete] an existing entry
f 			= 	[find] entries based on a search query
lb 			= 	[weights] used for CTP calculation, returns
rpt 		= 	[report] entries from a comma-seperated list of names
q 			= 	[quits] and saves new changes to JSON

!! CHANGES TO DATA WILL NOT BE SAVED TO THE JSON UNLESS YOU QUIT FROM THE MENU FIRST !!

You can view all the data in your data.json file. This file can be sent and used in another
user's CTP program. It contains all of your personalized information. 