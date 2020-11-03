from tkinter import *
import random
import tkinter

e_q =["1. Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1]?",
           "2. Suppose list1 is [1, 3, 2], What is list1 * 2?",
           "3. Which of the following is a Python tuple?",
           "4. What will be the output of the following Python code?\n>a=(2,3,4)\n> sum(a,3)",
           """5. What will be the output of the following Python code snippet?\n 1.d= {"john":40, "peter":45}\n 2.print(list(d.keys()))""",
           "6. Suppose d = {“john”:40, “peter”:45}, what happens when we try to retrieve a value using the expression d[“susan”]?",
           "7. Which of the following isn’t true about dictionary keys?",
           "8.  Which of the following functions is a built-in function in python?",
           "9. What will be the output of the following Python function?\nmin(max(False,-3,-4), 2,7)",
           "10. Suppose there is a list such that: l=[2,3,4]. If we want to print this list in reverse order, which of the following methods should be used?",
           "11.  What will be the output of the following Python code?\n1.def f(x, y, z): return x + y + z\n 2.f(2, 30, 400)",
           "12.  How are variable length arguments specified in the function heading?"]
e_options=[["a) Error","b) None","c) 25","d) 2"],
             ["a) [2, 6, 4]","b) [1, 3, 2, 1, 3]","c) [1, 3, 2, 1, 3, 2]","d) [1, 3, 2, 3, 2, 1]"],
             ["a) [1, 2, 3]","b) (1, 2, 3)","c) {1, 2, 3}","d) {}"],
             ["a)Too many arguments for sum() method","b)The method sum() doesn’t exist for tuples","c)12","d) 9"],
             ["a)[“john”,“peter”]","b)[“john”:40,“peter”:45]","c)(“john”,“peter”)","d) (“john”:40, “peter”:45)"],
             ["a) Since “susan” is not a value in the set,Python raises a KeyError exception","b) It is executed fine and no exception is raised, and it returns None","c) Since “susan” is not a key in the set, Python raises a KeyError exception","d) Since “susan” is not a key in the set, Python raises a syntax error"],
             ["a) More than one key isn’t allowed","b) Keys must be immutable","c) Keys must be integers","d) When duplicate keys encountered, the last assignment wins"],
             ["a)seed()","b)sqrt()","c)factorial()","d) print()"],
             ["a)2","b)False","c)-3","d) -4"],
             ["a)reverse(l)","b)list(reverse[(l)])","c)reversed(l)","d) list(reversed(l))"],
             ["a)432","b)24000","c)430","d) No output"],
             ["a)one star followed by a valid identifier","b)one underscore followed by a valid identifier","c)two stars followed by a valid identifier","d) two underscores followed by a valid identifier"]]
e_a=[3,3,2,3,1,3,3,4,2,4,1,1]

m_q =[" 1.To shuffle the list(say list1) what function do we use?",
           "2.What will be the output of the following Python code?\n1.names = ['Amir', 'Bear', 'Charlton', 'Daman']\n2.print(names[-1][-1])",
           "3. What will be the output of the following Python code?\n1.my_tuple = (1, 2, 3, 4)\n2.my_tuple.append( (5, 6, 7) )\n3.print len(my_tuple)",
           "4.  Is the following Python code valid?\n>>> a=(1,2,3)\n>>> b=('A','B','C')\n>>> c=tuple(zip(a,b))",
           """5.  What will be the output of the following Python code?\n>>> a=[(2,4),(1,2),(3,9)]\n>>> a.sort()\n>>> a""",
           """6. What will be the output of the following Python code snippet?\n 1.d1 = {"john":40, "peter":45}\n 2.d2 = {"john":466, "peter":45}\n 3.d1 > d2""",
           "7.  Which of the following is not a declaration of the dictionary?",
           "8. What is the output of the function complex()?",
           "9. Which of the following functions does not necessarily accept only iterables as arguments?",
           "10.Where is function defined?",
           "11. Which of the following is the use of id() function in python?",
           "12.  What will be the output of the following Python code?\ndef change(one, *two):\n\nprint(type(two))\nchange(1,2,3,4)"]
m_options=[["a) list1.shuffle()","b) shuffle(list1)","c) random.shuffle(list1)","d) random.shuffleList(list1)"],
             ["a)A","b)Daman","c)Error","d) n"],
             ["a)1","b)2","c)5","d) Error"],
             ["a) Yes, c will be ((1, ‘A’), (2, ‘B’), (3, ‘C’))","b) Yes, c will be ((1,2,3),(‘A’,’B’,’C’))","c) No because tuples are immutable","d) No because the syntax for zip function isn’t valid"],
             ["a)[(1, 2),(2, 4),(3, 9)]","b)[(2,4),(1,2),(3,9)]","c)Error because tuples are immutable","d) Error, tuple has no sort attribute"],
             ["a)True","b)False","c)Error","d) None"],
             ["a){1: ‘A’, 2: ‘B’}","b)dict([[1,”A”],[2,”B”]])","c){1,”A”,2”B”}","d) { }"],
             ["a)0j","b)0+0j","c)0","d) Error"],
             ["a)enumerate()","b)all()","c)chr()","d) max()"],
             ["a)Module","b)Class","c)Another function","d) All of the mentioned"],
             ["a)Id returns the identity of the object","b)Every object doesn’t have a unique id","c)All of the mentioned","d) None of the mentioned"],
             ["a)Integer","b)Tuple","c)Dictionary","d) An exception is thrown"]]
m_a=[3,4,4,1,1,3,3,1,3,4,1,2]


d_q =["  1.Suppose list1 is [4, 2, 2, 4, 5, 2, 1, 0], Which of the following is correct syntax for slicing operation?",
           "2.  What will be the output of the following Python code?\n1.data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]\n 2.print(data[1][0][0])",
           "3.  What will be the output of the following Python code?\n1.numberGames = {}\n2.numberGames[(1,2,4)] = 8\n3.numberGames[(4,2,1)] = 10\n4.numberGames[(1,2)] = 12\n5.sum = 0\n6.for k in numberGames:\n7.sum += numberGames[k]\n8.print len(numberGames) + sum",
           "4.  What will be the output of the following Python code?\na = ('check',)\nn = 2\nfor i in range(int(n)):\n\ta = (a,)\n\tprint(a)",
           """5.What will be the output of the following Python code snippet?
                a={1:"A",2:"B",3:"C"}
                print(a.get(1,4))""",
           """6. What is the output of the following program?
                D = dict() 
                for x in enumerate(range(2)): 
                    D[x[0]] = x[1] 
                    D[x[1]+7] = x[0] 
                    print(D) 
                """,
           "7. What will be the output of 7^10 in python?",
           "8. What will be the output of the following Python function?\nlist(enumerate([2, 3]))",
           "9.  What will be the output of the following Python function?\nfloat(‘-infinity’)\nfloat(‘inf’)",
           "10. Which of the following is a feature of DocString?",
           "11. Python supports the creation of anonymous functions at runtime, using a construct called ",
           "12.  What will be the output of the following Python code?\n1.min = (lambda x, y: x if x < y else y)\n2. min(101*99, 102*98)"]
d_options=[["a) print(list1[0])","b) print(list1[:2])","c) print(list1[:-2])","d) all of the mentioned"],
             ["a)1","b)2","c)4","d) 5"],
             ["a)30","b)24","c)33","d)12"],
             ["a) Error, tuples are immutable","b) (('check',),)\n((('check',),),)","c)((‘check’,)’check’,)","d) (('check',)’check’,)\n((('check',)’check’,)’check’,)"],
             ["a)1","b)A","c)4","d) Invalid syntax for get method"],
             ["a) Key Error","b) {0: 1, 7: 0, 1: 1, 8: 0}","c) {0: 0, 7: 0, 1: 1, 8: 1}","d) {1: 1, 7: 2, 0: 1, 8: 1}"],
             ["a)15","b)13","c)3","d)17"],
             ["a)Error","b)[(1, 2), (2, 3)]","c)[(0, 2), (1, 3)]","d) [(2, 3)]"],
             ["a) –inf  inf","b) –infinity  inf","c) Error  Error","d) Error  Junk value "],
             ["a) Provide a convenient way of associating documentation\n with Python modules, functions, classes, and methods","b)All functions should have a docstrings","c)Docstrings can be accessed by the __doc__ attribute on objects","d) All of the mentioned"],
             ["a)lambda","b)pi","c)anonymous","d) None of the mentioned"],
             ["a)9998","b)9999","c)9996","dd) None of the mentioned"]]
d_a=[4,4,3,2,2,3,2,3,1,4,1,3]


y=130

class easy_quiz:
    def __init__(self,master):
        self.opt_selected=IntVar()
        self.count=0
        self.qn=0
        self.correct=0
        self.ques=self.create_q(master,self.qn)
        self.opts=self.create_options(master,4)
        self.display_q(self.qn)
        self.b1=Button(master,text="End",font=("",20),bg="#B9C109",fg="white",activebackground="#D9E12B",activeforeground="white",command=self.end)
        self.b1.place(x=490,y=340,width=140,height=35)
        self.b2=Button(master,text="Save & Next",font=("",20),bg="#B9C109",fg="white",activebackground="#D9E12B",activeforeground="white",command=self.next_btn)
        self.b2.place(x=50,y=340,width=180,height=35)
    def create_q(self,master,qn):
        
        w= Label(master,text=e_q[qn],font = ("Consolas", 16),wraplength = 600,width=500,justify="left",bg='#727618',fg='white')
        w.pack(padx=5,pady=20)

        return w
    def create_options(self,master,n):
        b_val=0
        b=[]
        while b_val<n:
            global y
            r1 = Radiobutton(master,font = ("Times", 12),variable=self.opt_selected,value=b_val+1,bg='#FDF65C',fg='#727618',activebackground="#727618",activeforeground='white')
            b.append(r1)
            r1.pack(side=TOP,padx=20,anchor='w')
            b_val=b_val+1
        return b
    def display_q(self,qn):
        b_val=0
        self.opt_selected.set(0)
        self.ques['text']=e_q[qn]
        for op in e_options[qn]:
            self.opts[b_val]['text']=op
            b_val=b_val+1
    def check_q(self,qn):
        #self.count+=1
        if self.opt_selected.get()==e_a[qn]:
            return True
        return False
    def print_result(self):
        return True
    def next_btn(self):
        
        if self.check_q(self.qn):
            self.correct+=1
        self.qn=self.qn+1    
        if self.qn>=len(e_q):
            self.print_result()
        else:
            self.display_q(self.qn)
    def end(self):
        f3=Frame(bg="white")
        f3.place(x=0,y=0,width=700,height=500)
        self.a=self.correct
        self.score=str(self.a)
        labelimage = Label(f3,background = "#0D7CD8",border = 0,bg="#0D7CD8")
        labelimage.pack(padx=0,pady=5)
        labelresulttext = Label(f3,font = ("Consolas",20),background = "#075698",fg="white")
        labelresulttext.place(x=200,y=450)
        if self.a >= 11:
            img = PhotoImage(file="great.png")
            labelimage.configure(image=img)
            labelimage.image = img
            u2=Label(f3,text="Your marks are:",font=("",20),background = "#075698",fg="white")
            u2.place(x=200,y=400)
            u2=Label(f3,text=self.score,font=("",20),background = "#075698",fg="white")
            u2.place(x=400,y=400)
            labelresulttext.configure(text="You Are Excellent !!")
           
        elif (self.a >= 7 and self.a <= 10):
            img = PhotoImage(file="ok.png")
            labelimage.configure(image=img)
            labelimage.image = img
            u2=Label(f3,text="Your marks are:",font=("",20),background = "#075698",fg="white")
            u2.place(x=200,y=400)
            u2=Label(f3,text=self.score,font=("",20),background = "#075698",fg="white")
            u2.place(x=400,y=400)
            labelresulttext.configure(text="You Can Be Better !!")
            
        else:
            img = PhotoImage(file="bad.png")
            labelimage.configure(image=img)
            labelimage.image = img
            u2=Label(f3,text="Your marks are:",font=("",20),background = "#075698",fg="white")
            u2.place(x=200,y=400)
            u2=Label(f3,text=self.score,font=("",20),background = "#075698",fg="white")
            u2.place(x=400,y=400)
            labelresulttext.configure(text="You Should Work Hard !!")
            
class middle_quiz:
    def __init__(self,master):
        self.opt_selected=IntVar()
        self.count=0
        self.qn=0
        self.correct=0
        self.ques=self.create_q(master,self.qn)
        self.opts=self.create_options(master,4)
        self.display_q(self.qn)
        self.b1=Button(master,text="End",font=("",20),bg="#FDB45C",fg="white",activebackground="#D89012",activeforeground="white",command=self.end)
        self.b1.place(x=490,y=340,width=140,height=35)
        self.b2=Button(master,text="Save & Next",font=("",20),bg="#FDB45C",fg="white",activebackground="#D89012",activeforeground="white",command=self.next_btn)
        self.b2.place(x=50,y=340,width=180,height=35)
    def create_q(self,master,qn):
        
        w= Label(master,text=e_q[qn],font = ("Consolas", 16),wraplength = 600,width=500,justify="left",bg='#D89012',fg='white')
        w.pack(padx=5,pady=20)

        return w
    def create_options(self,master,n):
        b_val=0
        b=[]
        while b_val<n:
            global y
            r1 = Radiobutton(master,font = ("Times", 12),variable=self.opt_selected,value=b_val+1,bg='#FDB45C',fg='#727618',activebackground="#D89012",activeforeground='white')
            b.append(r1)
            r1.pack(side=TOP,padx=20,anchor='w')
            b_val=b_val+1
        return b
    def display_q(self,qn):
        b_val=0
        self.opt_selected.set(0)
        self.ques['text']=m_q[qn]
        for op in m_options[qn]:
            self.opts[b_val]['text']=op
            b_val=b_val+1
    def check_q(self,qn):
        #self.count+=1
        if self.opt_selected.get()==m_a[qn]:
            return True
        return False
    def print_result(self):
        return True
    def next_btn(self):
        
        if self.check_q(self.qn):
            self.correct+=1
        self.qn=self.qn+1    
        if self.qn>=len(m_q):
            self.print_result()
        else:
            self.display_q(self.qn)
    def end(self):
        f3=Frame(bg="white")
        f3.place(x=0,y=0,width=700,height=500)
        self.a=self.correct
        self.score=str(self.a)
        labelimage = Label(f3,background = "#0D7CD8",border = 0,bg="#0D7CD8")
        labelimage.pack(padx=0,pady=5)
        labelresulttext = Label(f3,font = ("Consolas",20),background = "#075698",fg="white")
        labelresulttext.place(x=200,y=450)
        if self.a >= 11:
            img = PhotoImage(file="great.png")
            labelimage.configure(image=img)
            labelimage.image = img
            u2=Label(f3,text="Your marks are:",font=("",20),background = "#075698",fg="white")
            u2.place(x=200,y=400)
            u2=Label(f3,text=self.score,font=("",20),background = "#075698",fg="white")
            u2.place(x=400,y=400)
            labelresulttext.configure(text="You Are Excellent !!")
           
        elif (self.a >= 7 and self.a <= 10):
            img = PhotoImage(file="ok.png")
            labelimage.configure(image=img)
            labelimage.image = img
            u2=Label(f3,text="Your marks are:",font=("",20),background = "#075698",fg="white")
            u2.place(x=200,y=400)
            u2=Label(f3,text=self.score,font=("",20),background = "#075698",fg="white")
            u2.place(x=400,y=400)
            labelresulttext.configure(text="You Can Be Better !!")
            
        else:
            img = PhotoImage(file="bad.png")
            labelimage.configure(image=img)
            labelimage.image = img
            u2=Label(f3,text="Your marks are:",font=("",20),background = "#075698",fg="white")
            u2.place(x=200,y=400)
            u2=Label(f3,text=self.score,font=("",20),background = "#075698",fg="white")
            u2.place(x=400,y=400)
            labelresulttext.configure(text="You Should Work Hard !!")  
            

class difficult_quiz:
    def __init__(self,master):
        self.opt_selected=IntVar()
        self.count=0
        self.qn=0
        self.correct=0
        self.ques=self.create_q(master,self.qn)
        self.opts=self.create_options(master,4)
        self.display_q(self.qn)
        self.b1=Button(master,text="End",font=("",20),bg="#FD705C",fg="white",activebackground="#921807",activeforeground="white",command=self.end)
        self.b1.place(x=490,y=420,width=140,height=35)
        self.b2=Button(master,text="Save & Next",font=("",20),bg="#FD705C",fg="white",activebackground="#921807",activeforeground="white",command=self.next_btn)
        self.b2.place(x=50,y=420,width=180,height=35)
    def create_q(self,master,qn):
        
        w= Label(master,text=e_q[qn],font = ("Consolas", 16),wraplength = 600,width=500,justify="left",bg='#921807',fg='white')
        w.pack(padx=5,pady=20)

        return w
    def create_options(self,master,n):
        b_val=0
        b=[]
        while b_val<n:
            global y
            r1 = Radiobutton(master,font = ("Times", 12),variable=self.opt_selected,value=b_val+1,bg='#FD705C',fg='#921807',activebackground="#921807",activeforeground='white')
            b.append(r1)
            r1.pack(side=TOP,padx=20,anchor='w')
            b_val=b_val+1
        return b
    def display_q(self,qn):
        b_val=0
        self.opt_selected.set(0)
        self.ques['text']=d_q[qn]
        for op in d_options[qn]:
            self.opts[b_val]['text']=op
            b_val=b_val+1
    def check_q(self,qn):
        #self.count+=1
        if self.opt_selected.get()==d_a[qn]:
            return True
        return False
    def print_result(self):
        return True
    def next_btn(self):
        
        if self.check_q(self.qn):
            self.correct+=1
        self.qn=self.qn+1    
        if self.qn>=len(d_q):
            self.print_result()
        else:
            self.display_q(self.qn)
    def end(self):
        f3=Frame(bg="white")
        f3.place(x=0,y=0,width=700,height=500)
        self.a=self.correct
        self.score=str(self.a)
        labelimage = Label(f3,background = "#0D7CD8",border = 0,bg="#0D7CD8")
        labelimage.pack(padx=0,pady=5)
        labelresulttext = Label(f3,font = ("Consolas",20),background = "#075698",fg="white")
        labelresulttext.place(x=200,y=450)
        if self.a >= 11:
            img = PhotoImage(file="great.png")
            labelimage.configure(image=img)
            labelimage.image = img
            u2=Label(f3,text="Your marks are:",font=("",20),background = "#075698",fg="white")
            u2.place(x=200,y=400)
            u2=Label(f3,text=self.score,font=("",20),background = "#075698",fg="white")
            u2.place(x=400,y=400)
            labelresulttext.configure(text="You Are Excellent !!")
           
        elif (self.a >= 7 and self.a <= 10):
            img = PhotoImage(file="ok.png")
            labelimage.configure(image=img)
            labelimage.image = img
            u2=Label(f3,text="Your marks are:",font=("",20),background = "#075698",fg="white")
            u2.place(x=200,y=400)
            u2=Label(f3,text=self.score,font=("",20),background = "#075698",fg="white")
            u2.place(x=400,y=400)
            labelresulttext.configure(text="You Can Be Better !!")
            
        else:
            img = PhotoImage(file="bad.png")
            labelimage.configure(image=img)
            labelimage.image = img
            u2=Label(f3,text="Your marks are:",font=("",20),background = "#075698",fg="white")
            u2.place(x=200,y=400)
            u2=Label(f3,text=self.score,font=("",20),background = "#075698",fg="white")
            u2.place(x=400,y=400)
            labelresulttext.configure(text="You Should Work Hard !!")              

def option():
    a=r.get()
    if(a==1):
        str="You have chosen easy questions!!"
        lbl =Label(f1,text=str, bg='#0D7CD8',fg='white').place(x=150, y=360, width=200, height=20)
        f2=Frame(bg="#FDF65C")
        f2.place(x=0,y=0,width=700,height=500)
        app=easy_quiz(f2)
    elif(a==2):
        str="You have chosen moderate questions!!"
        lbl =Label(text=str, bg='#0D7CD8',fg='white').place(x=150, y=360, width=200, height=20)
        f3=Frame(bg="#FDB45C")
        f3.place(x=0,y=0,width=700,height=500)
        app=middle_quiz(f3)
    elif(a==3):
        str="You have chosen difficult questions!!"  
        lbl =Label(text=str, bg='#0D7CD8',fg='white').place(x=150, y=360, width=200, height=20)
        f4=Frame(bg="#FD705C")
        f4.place(x=0,y=0,width=700,height=500)
        app=difficult_quiz(f4)
def option1():
    a=r.get()
    if(a==1):
        str="You have chosen easy questions!!"
        lbl =Label(f1,text=str, bg='#0D7CD8',fg='white').place(x=150, y=350, width=200, height=20)
    elif(a==2):
        str="You have chosen moderate questions!!"
        lbl =Label(text=str, bg='#0D7CD8',fg='white').place(x=150, y=350, width=200, height=20)
    elif(a==3):
        str="You have chosen difficult questions!!"  
        lbl =Label(text=str, bg='#0D7CD8',fg='white').place(x=150, y=350, width=200, height=20)

root=Tk()
root.title("Quiz")
root.geometry("700x500")#width x height
root.minsize(500,400)#width,height
#root.maxsize(1000,900)
root.resizable(0,0)
root.configure(background="#0D7CD8")
f1=Frame(bg="#0D7CD8")
f1.place(x=0,y=0,width=1000,height=900)
u1=Label(f1,text="-- Enter Your Details --",font=("",12),bg="#0D7CD8",fg="white")
u1.place(x=180,y=30)
    
u1=Label(f1,text="Enter name:",font=("",12),bg="#0D7CD8",fg="white")
u1.place(x=100,y=80)
e1=Entry(f1,font=("",12),width=200)
e1.place(x=250,y=80,width=200)
    
u2=Label(f1,text="Registration No:",font=("",12),bg="#0D7CD8",fg="white")
u2.place(x=100,y=130)
    
e2=Entry(f1,font=("",12),width=200)
e2.place(x=250,y=130,width=200)
u3=Label(f1,text="Section:",font=("",12),bg="#0D7CD8",fg="white")
u3.place(x=100,y=180)
    
e3=Entry(f1,font=("",12),width=200)
e3.place(x=250,y=180,width=200)

u2=Label(f1,text="Select Level:",font=("",12),bg="#0D7CD8",fg="white")
u2.place(x=100,y=235)
r=IntVar()
r1=Radiobutton(f1,bg='#0D7CD8',fg='white',activebackground="#075698",font=('', 13),text='    Easy',value=1,variable=r,command=option1)
r1.place(x=250,y=240)
r2=Radiobutton(f1,bg='#0D7CD8',fg='white', activebackground="#075698",font=('', 13),text='    Moderate',value=2,variable=r,command=option1)
r2.place(x=250,y=280)
r3=Radiobutton(f1,bg='#0D7CD8',fg='white',activebackground="#075698",font=('', 13),text='    Difficult',value=3,variable=r,command=option1)
r3.place(x=250,y=320)
u4=Label(f1,text="INSTRUCTIONS: \n>There will be total 12 questions.\n>Each question will be of one mark.",font=("",12),justify="left",bg="#0D7CD8",fg="white")
u4.place(x=150,y=380)
b1=Button(f1,text="Submit",font=("",20),bg="#0D7CD8",fg="white",activebackground="#075698",activeforeground="white",command=option)
b1.place(x=240,y=450,width=140,height=40)
root.mainloop()


# In[ ]:





# In[ ]:




