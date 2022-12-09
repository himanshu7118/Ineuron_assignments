1.	What advantages do Excel spreadsheets have over CSV spreadsheets?
Ans: While Excel (XLS and XLSX) file formats are better for storing more complex data, CSV files are supported by nearly all data upload interfaces. If you are planning to move your data between platforms, export and import it from one interface to another, you might be better off with the CSV file format.

2.What do you pass to csv.reader() and csv.writer() to create reader and writer objects?
Ans: call open() and pass it 'w' to open a file in write mode. This will create the object you can then pass to csv. writer()  to create a Writer object.

3.What modes do File objects for reader and writer objects need to be opened in?
Ans: we must use the built-in open() function. The open() function uses two arguments.

4. What method takes a list argument and writes it to a CSV file?
Ans: The most common method to write data from a list to CSV file is the writerow() method of writer and DictWriter class.

5. What do the keyword arguments delimiter and line terminator do?
Ans: This changes the delimiter and line terminator characters in your file. The delimiter is the character that appears between cells on a row. By default, the delimiter for a CSV file is a comma. The line terminator is the character that comes at the end of a row.

6. What function takes a string of JSON data and returns a Python data structure?
Ans: loads() 

7. What function takes a Python data structure and returns a string of JSON data?
Ans: json.dumps()

