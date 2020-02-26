
call "C:\Users\asayeed\Desktop\Python Projects\Selenium\move_old_csv_files_to_archive.bat"
timeout /t 3
call "C:\Users\asayeed\Desktop\Python Projects\Selenium\download_Contact Details.bat"
timeout /t 10
call "C:\Users\asayeed\Desktop\Python Projects\Selenium\download_Conversions.bat"

timeout /t 5
taskkill /F /IM msedge.exe

Exit