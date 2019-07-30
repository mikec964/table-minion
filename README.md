# Table Minion

If you give this app the name of a table and a die roll to look up, it will return a PNG image of the result column. It's intended to provide better table features for Roll20.net.

Why return an image? Because Roll20 macros can retrieve images from the web, but not other data types.

Planned features:
* Flexible index column
    * [x] Ranges (e.g. 2, or 2–5)
    * [ ] Weights (e.g. 35, fraction of index sum)
    * [ ] Min/max ranges (e.g. 3-, 11+)
* Easy CSV tables
    * [x] White space ignored
    * [ ] Heading row
    * [ ] Allow commas in results, strip quote marks
* Results can trigger additional rolls on tables
    * [x] Name table to roll
    * [ ] Secondary tables can have different ranges
* Advanced queries
    * [ ] Roll on a table multiple times
    * [ ] Multiply roll by value (e.g. 1d10 * 100 gold)
    * [ ] Rolls within results (e.g. d6 rats)
    * [ ] Results can have modifiers to additional rolls
    * [ ] Tables can have more than one results column
    * [ ] Combine results into sentences
    * [ ] Return image linked by URL in the result

Table format:
* indexCol, resultCol
    * indexCol: 2, 2-3, 3-, 10+
    * resultCol:
        * string
        * optional: /rollon(table-name\[, add\[, roll_list\]\])

Query format:
    * [ ]   /troll      # table roll service
    * [ ]   ?table=<tablename>
    * [ ]   &showtable  # show entire table (else show only result)
    * [ ]   &showroll   # show roll with result (else show only result)
    * [ ]   &animate    # animate die roll
    * [ ]   &rolls=3,2,5    # default roll_list (e.g. 2d6 results)
    * [ ]   &rolls-b=15,10  # roll_list b. Use a-z. (e.g. 1d20 results)

Site features:
* Registered users can create and upload tables
* Users can share tables
