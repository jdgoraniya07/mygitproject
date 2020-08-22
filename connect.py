import sqlite3
class myconnect:
      
      def __init__(self):
              
            try:
                self.conn = sqlite3.connect("emp.db")
                self.conn.execute('create table if not exists emp (name text, salary interger, emp_type char)')
                print('table created')
            except:
                pass
                 
                  
      def savetodb(self,ename,eemail,emob,etype,eexp,esalary):
          self.conn.execute("insert into emp values (?,?,?)",(ename,esalary,etype))
          self.conn.commit()
          print("record added")

      def display(self):
          name = input("Enter the emp name")
          data = self.conn.execute("select * from emp where name=:name",{"name":name})
          

          for i in data:
              print(i[0])
              print(i[1])
              print(i[2])