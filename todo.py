from tkinter import *
import sqlite3,sys

def connection():
    try:
        conn=sqlite3.connect("Todo.db")
    except:
        print("cannot connect to the database")
    return conn    


def verifier():
    a=b=c=0
    if not Task.get():
        t1.insert(END,"<>Task is required<>\n")
        a=1
    if not LastDate.get():
        t1.insert(END,"<>Date is required<>\n")
        b=1
    if not Till.get():
        t1.insert(END,"<>Time is requrired<>\n")
        c=1
    
    if a==1 or b==1 or c==1:
        return 1
    else:
        return 0
    
def verifier1():
    a=b=c=0
    if not Task.get():
        t1.insert(END,"<>Task is required<>\n")
        a=1    
    if a==1:
        return 1
    else:
        return 0


def add_task():
            ret=verifier()
            if ret==0:
                conn=connection()
                cur=conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS TODO(TASK TEXT,LASTDATE TEXT, TILL TEXT )")
                cur.execute("insert into TODO values(?,?,?)",(Task.get(), LastDate.get(), Till.get()))
                conn.commit()
                conn.close()
                t1.insert(END,"ADDED SUCCESSFULLY\n")


def view_task():
    conn=connection()
    cur=conn.cursor()
    cur.execute("select * from TODO")
    data=cur.fetchall()
    conn.close()
    for i in data:
        t1.insert(END,str(i)+"\n")


def delete_task():
    ret=verifier1()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("DELETE FROM TODO WHERE TASK=?",(Task.get()),)
        conn.commit()
        conn.close()
        t1.insert(END,"SUCCESSFULLY DELETED THE TASK\n")

def update_task():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("UPDATE TODO SET LASTDATE=?,TILL=? where TASK=?",(LastDate.get(),Till.get(),Task.get()))
        conn.commit()
        conn.close()
        t1.insert(END,"UPDATED SUCCESSFULLY\n")
        
def clear_all():
    conn=connection()
    cur=conn.cursor()
    cur.execute("DROP TABLE TODO")
    conn.commit()
    conn.close()
    t1.insert(END,"CLEARED")

def clse():
    sys.exit() 


if __name__=="__main__":
    root=Tk()
    root.title("Student Management System")
     
    Task=StringVar()
    LastDate=StringVar()
    Till=StringVar()

    
    label1=Label(root,text="Task:")
    label1.place(x=0,y=0)

    label2=Label(root,text="Last Date:")
    label2.place(x=0,y=30)

    label3=Label(root,text="Time Till:")
    label3.place(x=0,y=60)


    e1=Entry(root,textvariable=Task)
    e1.place(x=100,y=0)

    e2=Entry(root,textvariable=LastDate)
    e2.place(x=100,y=30)

    e3=Entry(root,textvariable=Till)
    e3.place(x=100,y=60)

    
    t1=Text(root,width=80,height=20)
    t1.grid(row=10,column=1)
   


    b1=Button(root,text="ADD TASK\n",command=add_task,width=40)
    b1.grid(row=11,column=0)

    b2=Button(root,text="VIEW ALL TASKS\n",command=view_task,width=40)
    b2.grid(row=12,column=0)

    b3=Button(root,text="DELETE TASK\n",command=delete_task,width=40)
    b3.grid(row=13,column=0)

    b4=Button(root,text="UPDATE TASK\n",command=update_task,width=40)
    b4.grid(row=14,column=0)
    
    b5=Button(root,text="CLEAR ALL TASKS\n",command=clear_all,width=40)
    b5.grid(row=15,column=0)
    
    b6=Button(root,text="CLOSE\n",command=clse,width=40)
    b6.grid(row=16,column=0)


    root.mainloop()
