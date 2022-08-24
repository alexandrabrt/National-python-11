from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from pandas import ExcelWriter

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.bnr.ro/files/xml/nbrfxrates2021.htm')

table_head = driver.find_element(by=By.XPATH, value='//*[@id="Data_table"]/table/thead')
# print(table_head.text)
table_body = driver.find_element(by=By.XPATH, value='//*[@id="Data_table"]/table/tbody')
# print(table_body.text)

header = table_head.text.split('\n')
body = table_body.text.split('\n')

# print(header)
# print(body)
# print(len(header))
# print(len(body))

# TABEL GENERAT PE RANDURI
# body_rows = []
# counter = 0
# for i in range(0, len(body), len(header)):
#     counter = i # 0, 32, 64,
#     body_rows.append(body[counter: counter+len(header)])

# df = pd.DataFrame(body_rows, columns=header)
# with ExcelWriter('TABEL_BNR_2021.xlsx') as writer:
#     df.to_excel(writer, index=0)

# TABEL GENERAT PE COLOANE

body_columns = {key: [] for key in range(len(header))}
body_columns_list = len(body_columns)
counter = 0
for j in body:
    body_columns[counter % body_columns_list].append(j)
    counter += 1

df = pd.DataFrame(body_columns)
with ExcelWriter('TABEL_2_BNR_2021.xlsx') as writer:
    df.to_excel(writer, header=header, index=0)
