
import cx_Oracle

connstr='bala/balaji@xe'
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()

result = curs.execute('select * from employee_data')

print result.count

for row in curs:
   print row
conn.close()