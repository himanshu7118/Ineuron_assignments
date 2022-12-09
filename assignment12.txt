1.	In what modes should the PdfFileReader() and PdfFileWriter() File objects will be opened?
Ans: For PdfFileReader() file objects should be opened in rb -> read binary mode, Whereas for PdfFileWriter() file objects should be opened in wb -> write binary mode.

2.	From a PdfFileReader object, how do you get a Page object for page 5?
Ans: PdfFileReader class provides a method called getPage(page_no) to get a page object.

3.	What PdfFileReader variable stores the number of pages in the PDF document?
Ans: getNumPages() method of PdfFileReader class stores the no pages in a PDF document.

4.	If a PdfFileReader object’s PDF is encrypted with the password swordfish, what must you do before you can obtain Page objects from it?
Ans: PdfFileReader class provides a attribute called isEncrypted to check whether a pdf is encrypted or not. the method returns true if a pdf is encrypted and vice versa.
if pdf is encrypted use the decrypt() method provided by PdfFileReader class first then try to read the contents/pages of the pdf.

5.	What methods do you use to rotate a page?
Ans: rotateClockWise() , rotateCounterClockWise()

6.	What is the difference between a Run object and a Paragraph object?
Ans: The Document object contains a list of Paragraph objects for the paragraphs in the document.Each of these Paragraph objects contains a list of one or more Run objects.

7.	How do you obtain a list of Paragraph objects for a Document object that’s stored in a variable named doc?
Ans: 
from docx import Document
doc = Document("sample_file.docx") 
print(doc.paragraphs) 
for paragraph in doc.paragraphs:
    print(paragraph.text) 

8.	What type of object has bold, underline, italic, strike, and outline variables?
Ans: Run object has bold, underline, italic, strike, and outline variables.

9.	What is the difference between False, True, and None for the bold variable?
Ans: 
bold = True  # Style Set to Bold
bold = False # Style Not Set to Bold
bold = None # Style is Not Applicable

10.	How do you create a Document object for a new Word document?
Ans:
from docx import Document
document = Document()
document.add_paragraph("Learn python programming")
document.save('mydocument.docx')

11.	How do you add a paragraph with the text 'Hello, there!' to a Document object stored in a variable named doc?
Ans: 
from docx import Document
doc = Document()
doc.add_paragraph('Hello, there!')
doc.save('hello.docx')

12.	What integers represent the levels of headings available in Word documents?
Ans: The levels for a heading in a word document can be specified by using the level attribute inside the add_heading method. There are a total of 5 levels statring for 0 t0 4. where level 0 makes a headline with the horizontal line below the text, whereas the heading level 1 is the main heading. Similarly, the other headings are sub-heading with their's font-sizes in decreasing order.

