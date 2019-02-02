# noddus-python

To run type in
`loader.py assets/student-data.csv`

Or if you have another file
`loader.py <filename.csv>`

This will create an SQLite database called grades.db if it does not already exists.
It will create a table called grades in the database if one does not exists.

It will add every row from the csv file into the database. Except the first row
which we count as a header.

It will report the number of rows added and the final size of the grades table
in the database
