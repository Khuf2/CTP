# CTP JSON Database

https://github.com/Khuf2/CTP : For more-readable instructions.

This is a program that allows you to **store people** as entries in a simple
**JSON file**, which can be revisited and add to a database of your own rating
information. 

It is operated via a custom command line that reads in user input and decides operations based
on the sequence of shortcuts. This is done via string parsing.

Sorting and searching commands allow for focused presentation of your data, which
is the most significant efficiency difference when compared to manual record-keeping.

This design can be built around any type of data, and the structure can be emulated for a different
purpose than CTP tracking. The user interaction loop, data storage system, and the command line reader 
are the main tools that had to be created in the making of this program.

## Usage:

After you log in, the program operates out of a central menu loop.
In this menu, you can select different operations with shortcuts.

### Shortcuts Glossary:

**ls**
: [list] name, gender, and CTP of all entries
: Usage: ls

**add**
: [add] a new entry
: Usage: add, add ***name***

**edit**
: [edit] an existing entry
: Usage: edit, edit ***name***, edit ***name*** ***category***, edit ***name*** ***category*** ***new value or relative change***

**del**
: [delete] an existing entry
: Usage: del, del ***name***

**f**
: [find] entries based on a search query 
: Usage:  f ***filter***, f ***filter1***, ***filter2***, ***...***
: Filter condition example: age>60, intel<=60
: Make sure there's no blank spaces inside your conditions.

**lb**
: prints [weights] used for CTP calculation
: Usage: lb

**sort**
: [sort] data list by specified criteria.
: Usage: sort, sort ***criterion*** ***order***

**rpt**
: [report] entries from a comma-seperated list of names. Using the asterisk prints all entries.
: Usage: rpt, rpt *, rpt ***name1***, ***name2***, ***name3***, ***...***

**q**
: [quits] and saves new changes to JSON
: Usage: q

You can **view all the data in your data.json file**. This file can be sent and used in another
user's CTP program. It contains all of your personalized information. 
