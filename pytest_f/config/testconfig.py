import os

project_file=os.path.dirname(os.path.dirname(__file__))


url="http://110.40.173.25:9000/zentao/user-login-L3plbnRhby8=.html"
driver_path=project_file+r'\driver\chromedriver.exe'
datafile_path=project_file+r'\data\testdata.xlsx'
#datafile_path=project_file+r'\data\iwebsnsdata.xlsx'
#case_path=project_file+r'\testcases'
report_path=project_file+r'\result\report'
log_path=project_file+r'\log\log.txt'