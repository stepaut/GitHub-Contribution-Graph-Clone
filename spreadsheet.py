import os
import gspread
import xlrd
from pandas import *
from tkinter import *
from tkinter.filedialog import askopenfile
from oauth2client.service_account import ServiceAccountCredentials


def getDataFromGoogleDrive():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_file = os.path.join(SITE_ROOT, 'static', 'Client_Secret.json')
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(json_file, scope)
    client = gspread.authorize(creds)

    sheet = client.open('Daily Contribution').sheet1

    date = sheet.col_values(1, value_render_option='FORMATTED_VALUE')
    task = sheet.col_values(2, value_render_option='FORMATTED_VALUE')
    numberOfTasks = sheet.col_values(3, value_render_option='FORMATTED_VALUE')
    level = sheet.col_values(4, value_render_option='FORMATTED_VALUE')
    
    return [date, task, level]


def getDataFromExcel():
    # TODO
    workbook = xlrd.open_workbook(r'test.xls', on_demand=True)
    # TODO
    sheet = workbook.sheet_by_name('Sheet1')
    date = sheet.col_values(0)
    level = sheet.col_values(1)

    return [date, level]


def getDataFromCsv():
    try:
        Tk().withdraw()
        csv_file = askopenfile(filetypes=([("CSV files", "*.csv")]))

        data = read_csv(csv_file)
        date = data["Date"].tolist()
        level = data["Level"].tolist()

        print([date, level])

        return [date, level]
    except Exception as ex:
        print(ex)
        return None
