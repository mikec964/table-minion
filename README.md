# Table Minion

If you give this app the name of a table and a die roll to look up, it will return a PNG image of the result column. It's intended to provide better table features for Roll20.net.

Why return an image? Because Roll20 macros can retrieve images from the web, but not other data types.

Planned features:
* The index column can be numbers, ranges (e.g. 2–5 or 6+), or percentages.
* You can upload CSV tables
* Results can trigger additional rolls on tables
* Results can have modifiers to additional rolls
* Tables can have more than one results column

Table format:
# name
# desc
indexCol, resultCol
indexCol, resultCol

Query format:
?table-name
&showtable=1    # show entire table (else show only result)
&showroll=1     # show roll with result (else show only result)
&animate=1      # animate die roll
&roll<n>=<value>
&roll<n>=<value>

Site features:
* Registered users can create and upload tables
* Users can share tables
