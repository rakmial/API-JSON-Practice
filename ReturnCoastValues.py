"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
from zipfile import ZipFile
datafile = r"C:\Users\Bash\Desktop\Udacity\2_Data Analysis\P2\Beatles\2013_ERCOT_Hourly_Load_Data.xls"

def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    coast_values = sheet.col_values(1, start_rowx=1)
    time_values = sheet.col_values(0, start_rowx=1)
    coast_mean = sum(coast_values)/len(coast_values)
    coast_min = min(coast_values)
    coast_max = max(coast_values)
    min_time = time_values[coast_values.index(coast_min)]
    max_time = time_values[coast_values.index(coast_max)]
    min_pytime = xlrd.xldate_as_tuple(min_time, 0)
    max_pytime = xlrd.xldate_as_tuple(max_time, 0)

    data = {
            'maxtime': max_pytime,
            'maxvalue': coast_max,
            'mintime': min_pytime,
            'minvalue': coast_min,
            'avgcoast': coast_mean
    }
    return data

    ### example on how you can get the data
    #sheet_data = [[sheet.cell_value(r, col)
    #                    for col in range(sheet.ncols)]
#                            for r in range(sheet.nrows)]

    ### other useful methods:
    # print "\nROWS, COLUMNS, and CELLS:"
    # print "Number of rows in the sheet:",
    # print sheet.nrows
    # print "Type of data in cell (row 3, col 2):",
    # print sheet.cell_type(3, 2)
    # print "Value in cell (row 3, col 2):",
    # print sheet.cell_value(3, 2)
    # print "Get a slice of values in column 3, from rows 1-3:"
    # print sheet.col_values(3, start_rowx=1, end_rowx=4)

    # print "\nDATES:"
    # print "Type of data in cell (row 1, col 0):",
    # print sheet.cell_type(1, 0)
    # exceltime = sheet.cell_value(1, 0)
    # print "Time in Excel format:",
    # print exceltime
    # print "Convert time to a Python datetime tuple, from the Excel float:",
    # print xlrd.xldate_as_tuple(exceltime, 0)


def test():
    data = parse_file(datafile)
    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()
