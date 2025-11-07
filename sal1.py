class JobPost:
    def __init__(self, title, company, location, salary, description):
        self.title = title
        self.company = company
        self.location = location
        self.salary = salary
        self.description = description

    def display_info(self):
        print(f"Job Title: {self.title}")
        print(f"Company: {self.company}")
        print(f"Location: {self.location}")
        print(f"Salary: {self.salary}")
        print(f"Description: {self.description}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Updated salary for {self.title} to {self.salary}")
Job = JobPost("Data Engineer", "atm","New York, NY",425000, "contract" )
x = Job.display_info()
job1 = JobPost("ceo","ibm","london",9000,"permanent")
print(Job.display_info)
print(job1.description)
print(x)
#### Built-in Types

"""Python has the following data types built-in by default:
| Type               | Data Type           | Example               |
|--------------------|---------------------|-----------------------|
| Text               | `str`               | `"Data Nerd!"`     |
| Numeric            | `int`               | `42`                  |
|                    | `float`             | `3.14159`             |
|                    | `complex`           | `1 + 2j`              |
|------------------------------------------------------------------
 Sequence           | `list`              | `[1, 2, 3]`           |
|                    | `tuple`             | `(1, 2, 3)`           |
|                    | `range`             | `range(10)`           |
|-------------------------------------------------------------------
 Mapping            | `dict`              | `{"key": "value"}`    |
|--------------------------------------------------------------------
 Set                | `set`               | `{1, 2, 3}`           |
|                    | `frozenset`         | `frozenset([1, 2, 3])`|
|-------------------------------------------------------------------
 Boolean            | `bool`              | `True` or `False`     |
|-------------------------------------------------------------------
 Binary             | `bytes`             | `b"Data"`            |
|                    | `bytearray`         | `bytearray(5)`        |
|                    | `memoryview`        | `memoryview(b"Data")`|
|-------------------------------------------------------------------
 None               | `NoneType`          | `None`                |
 ------------------------------------------------------------------

For more information on the different data types in Python check out 
the Python documentation 
for data types [here](https://docs.python.org/3/library/datatypes.html).

#### Types Common in Data Analytics

We'll mainly focus on the most common ones in data analytics:
* Text Type: `str`
* Numeric Types: `int`, `float`
* Sequence Types:	`list`, `tuples`
* Mapping Type:	`dict`
* Set Types:	`set`

### Importance
Fundamental for data processing. Pandas and matplotlib
 automatically handle different data types for operations 
 like mathematical calculations, data manipulation, and plotting.
"""

