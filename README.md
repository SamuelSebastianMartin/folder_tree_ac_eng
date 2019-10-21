# Make a file tree for student work.

This project is to convert the student lists (supplied in
SOAS registers) into a tree of directories which can be
uploaded to Google drive as 'Folders' for academic work.

            ```
            Student work/
              |
              |___ SURNAME Firstname/
              |    |
              |    |__Term 1/
              |    |
              |    |__Term 2/
              |    |
              |    |__Term 3/
              |
              |____NEXT Student/
              |    |
              |    |__Term 1/
              |    |
              |    |__Term 2/
              |    |
              |    |__Term 3/
            ```

## Use
        `python3 make_google_folders.py`

NOTE: There must be a .csv file handy, which has been
downloaded from the Google Docs class register of the
teacher concerned.

## Potential Problems

Some functions are not robust and will break if the
format of the registers change:

  * If words like *Name* or *Family Name* appear among
    the folders, it probably means that SOAS has changed
    the column names in the spreadsheet.
    To fix, edit the regex expressions in
    `clean_names_list()`. Or make a more robust function.

  * If the folder names include student numbers or Boolean
    values, or other strange values, then the problem is
    probably that the column order has changed.
    To fix, change the column numbers, hard-coded into
    `extract_names()`. Or make a more robust function.
