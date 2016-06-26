
import cx_Oracle

from petl import*

connstr='bala/balaji@xe'
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()
curs.execute('select * from employee_data')

# Fetchall will fetch all the records and store into a python object

qresult=curs.fetchall()
conn.close()

fieldname=[('Empno','Empname','Deptno','Sal')]

#appending field name to the query result set
finalqresult=fieldname+qresult

#print(finalqresult)

# read Dept Dimension records from csv file

DeptDim=fromcsv('Dept_Dim1.csv',delimiter=',')

DeptDimCon=convert(DeptDim,'Deptno',int)

#print DeptDimCon

#inner join Employee data from Oracle with DeptDim from csv file based on Deptno

JoinResult=join(finalqresult,DeptDimCon,key='Deptno')

print JoinResult




