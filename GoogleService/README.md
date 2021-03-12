# Setup
1. After cloning the repo, access the `GoogleService` Folder
    ```bash
    cd rPacks/GoogleService/
    ```

2. Then install the package
    ```bash
    pip install -e .
    ```

3. Create a new directory for your project. For this example, it will be the directory `SheetsProject/` 

4. Now you must enable the Google Sheets API by accessing [this link](https://developers.google.com/sheets/api/quickstart/python) and clicking the "Enable the Google Sheets API" button

5. After enabling the API, download your credentials.json and save it to `SheetsProject/`

Now, you are ready to use the package

# How to use
First, create a new python file inside `SheetsProject/`, so the folder structure will be:
```
SheetsProject
    |- credentials.json
    |- project.py 
```

Create a connection to the Google Sheets API, you will need the ID of the sheet that you will be using
[How to find the sheet ID](https://developers.google.com/sheets/api/guides/concepts#spreadsheet_id)

```python
from GoogleSheets.GoogleSheets import GoogleSheetsService

CREDENTIALS = './credentials.json'  # path to your credentials
PICKLE = './token.pickle'           # path to the token.pickle that will be created by the API
SHEET_ID = '<your google sheet ID>'
WRITE_RANGE = 'Página1!A1'
READ_RANGE = 'Página1!A1:C2'

service = GoogleSheetsService(CREDENTIALS, PICKLE) # Connect

write_data = [['apple', 'orange', 'pineapple'],    # Values that will be written in the sheet
              ['Book', 'Car', 'Chair'],
              ['test', 1, 2]]

service.write(SHEET_ID, WRITE_RANGE, write_data) # Write values to the sheet

received_values = service.read(SHEET_ID, READ_RANGE) # Read values from the sheet
print(received_values)

```
