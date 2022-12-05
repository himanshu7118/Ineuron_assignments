1.	How do you distinguish between shutil.copy() and shutil.copytree()?
Ans: The shutil.copy() function will copy a single file, while shutil.copytree() will copy an entire folder, along with all its contents.

2.	What function is used to rename files??
Ans: The shutil.move() function is used for renaming files, as well as moving them.

3.	What is the difference between the delete functions in the send2trash and shutil modules?
Ans: The send2trash functions will move a file or folder to the recycle bin, while shutil functions will permanently delete files and folders.

4.ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?
Ans:  The zipfile.ZipFile() function is equivalent to the open() function; the first argument is the filename, and the second argument is the mode to open the ZIP file in (read, write, or append).

5.	Create a programme that searches a folder tree for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.
Ans: 
            import os, shutil
            sourcePath = input('Enter the absolute path of the source folder: ') 
            fileExtType = input('Enter the type of file to copy (such as .pdf or .jpg): ').lower() 
            destPath = input('Enter the absolute path of the destination folder: ')
            for foldername, subfolders, filenames in os.walk(sourcePath): 
                for filename in filenames: 
                    if filename.lower().endswith(fileExtType): 
                        print(foldername + '\\' + filename) 
                        copySourcePath = os.path.join(foldername, filename) 
                        print(copySourcePath) 
                        shutil.copy(copySourcePath, destPath) 
                    else: 
                        continue
