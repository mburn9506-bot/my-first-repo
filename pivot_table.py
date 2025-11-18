import pandas as pd

data = {
    'Department': ['IT', 'IT', 'HR', 'HR', 'Finance', 'Finance'],
    'Employee': ['John', 'Sam', 'Anna', 'Bob', 'Alice', 'George'],
    'Salary': [5000, 6000, 4500, 4800, 7000, 7200]
}

df = pd.DataFrame(data)
# print(df)
# df.pivot_table(values='Salary', index='Department')
# print(df.pivot_table)
x = df.pivot_table(values='Salary', index='Department', aggfunc='sum')
print(x)

y = df.pivot_table(values='Salary', index='Department', aggfunc=['mean', 'max', 'min'])
print(y)
z = df.pivot_table(values='Salary', index='Employee', aggfunc=['mean', 'max', 'min'])

print(z)
"""/Users/michelkadi/dataanalytics/mat/bin/python /Users/michelkadi/dataanalytics/pivot_table.py
➜  dataanalytics /Users/michelkadi/dataanalytics/mat/bin/python /Users/michelkadi/dataanalytics/pivot_table.py
➜  dataanalytics git:(mike) ✗ /Users/michelkadi/dataanalytics/mat/bin/python /Users/michelkadi/dataanalytics/pivot_table.py
  Department Employee  Salary
0         IT     John    5000
1         IT      Sam    6000
2         HR     Anna    4500
3         HR      Bob    4800
4    Finance    Alice    7000
5    Finance   George    7200
➜  dataanalytics git:(mike) ✗ /Users/michelkadi/dataanalytics/mat/bin/python /Users/michelkadi/dataanalytics/pivot_table.p
y
  Department Employee  Salary
0         IT     John    5000
1         IT      Sam    6000
2         HR     Anna    4500
3         HR      Bob    4800
4    Finance    Alice    7000
5    Finance   George    7200
➜  dataanalytics git:(mike) ✗ /Users/michelkadi/dataanalytics/mat/bin/python /Users/michelkadi/dataanalytics/pivot_table.p
y
➜  dataanalytics git:(mike) ✗ /Users/michelkadi/dataanalytics/mat/bin/python /Users/michelkadi/dataanalytics/pivot_table.p
y
<bound method DataFrame.pivot_table of   Department Employee  Salary
0         IT     John    5000
1         IT      Sam    6000
2         HR     Anna    4500
3         HR      Bob    4800
4    Finance    Alice    7000
5    Finance   George    7200>
➜  dataanalytics git:(mike) ✗ /Users/michelkadi/dataanalytics/mat/bin/python /Users/michelkadi/dataanalytics/pivot_table.p
y
➜  dataanalytics git:(mike) ✗ /Users/michelkadi/dataanalytics/mat/bin/python /Users/michelkadi/dataanalytics/pivot_table.p
y
  Department Employee  Salary
0         IT     John    5000
1         IT      Sam    6000
2         HR     Anna    4500
3         HR      Bob    4800
4    Finance    Alice    7000
5    Finance   George    7200
➜  dataanalytics git:(mike) ✗ /Users/michelkadi/dataanalytics/mat/bin/python /Users/michelkadi/dataanalytics/pivot_table.p
y
            Salary
Department        
Finance      14200
HR            9300
IT           11000
➜  dataanalytics git:(mike) ✗ /Users/michelkadi/dataanalytics/mat/bin/python /Users/michelkadi/dataanalytics/pivot_table.py
            Salary
Department        
Finance      14200
HR            9300
IT           11000
              mean    max    min
            Salary Salary Salary
Department                      
Finance     7100.0   7200   7000
HR          4650.0   4800   4500
IT          5500.0   6000   5000
➜  dataanalytics git:(mike) ✗ /Users/michelkadi/dataanalytics/mat/bin/python /Users/michelkadi/dataanalytics/pivot_table.py
            Salary
Department        
Finance      14200
HR            9300
IT           11000
              mean    max    min
            Salary Salary Salary
Department                      
Finance     7100.0   7200   7000
HR          4650.0   4800   4500
IT          5500.0   6000   5000

                               ^^^^^^^^^^^^
  
            Salary
Department        
Finance      14200
HR            9300
IT           11000
              mean    max    min
            Salary Salary Salary
Department                      
Finance     7100.0   7200   7000
HR          4650.0   4800   4500
IT          5500.0   6000   5000
            mean    max    min
z = df.pivot_table(values='Salary', index='Employee', aggfunc=['mean', 'max', 'min'])
          Salary Salary Salary
Employee                      
Alice     7000.0   7000   7000
Anna      4500.0   4500   4500
Bob       4800.0   4800   4800
George    7200.0   7200   7200
John      5000.0   5000   5000
Sam       6000.0   6000   6000
➜  dataanalytics git:(mike) ✗ y = df.pivot_table(values='Salary', index='Department', aggfunc=['mean', 'max', 'min'])"""