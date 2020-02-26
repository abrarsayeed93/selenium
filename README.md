# selenium
bot to download SF data

This document will guide the user to install the selenium environment and the necessary packages required to run the bot. Please follow accordingly.

Prerequisites:
•	Make sure Salesforce is authenticated in your browser. This script will not do windows authentication.
•	Anaconda needs to be downloaded and installed in your computer. Follow the link to download anaconda here 
•	This programme was written to work on Microsoft Edge browser. If you are using any other browsers(e.g. Chrome), make sure to make the necessary changes to the script as well as having the necessary drivers installed. The folder drivers contain the drivers for chrome and firefox respectively.
Steps:
1.	Copy and place the Selenium folder from the Automating the redundant folder into the desired directory of your choice in your desktop.
2.	Open the anaconda command prompt
3.	Go to the Selenium directory in your computer by typing “cd path/to/selenium/folder” into the command terminal.
4.	Run the command by typing “conda create --name selenium --file requirements.txt”
5.	This will create the environment and install all the packages required.
6.	Follow below:

If you need to change the link you may do so in the python script by replacing the url at line 18
driver.get('https://studygroup.my.salesforce.com/00O3z000007aYcW')

1.	Change the source directories at lines 54-56.
2.	Src_dir is the Downloads folder where your file is downloaded to.
3.	Dst_dir0 is the full path name of the file that the report will be renamed to
4.	Dst_dir is the final full path of the file.
Note: Only use Salesforce Classic URL.
