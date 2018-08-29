from guizero import *
import random
import subprocess
from time import sleep

l1=[[1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,9,10],
    [1,2,3,4,5,6,7,8,9,10]]


l2=[]
answer_no=0

for x in range(1,11):
    for y in range (1,11):
        l2.append([x,y])
print (l2)
l2.pop()
print(l2)
random.shuffle(l2)
print (l2)


    
    

class multiplication(object):
    def __init__(self):
        self.app=App(width=420, title="Mortens gangetræning")
        self.box1=Box(self.app,layout = "grid")
        
        for i in range (7):
            Picture(self.box1, image="/home/pi/pythonfiles/gangespil/res/bluebgtile.png", grid=[i,0,1,8], align="left")
        Picture(self.box1, image="/home/pi/pythonfiles/gangespil/res/bluebg.png", grid=[0,0,8,8], align="left")
        self.number1_field=Text(self.box1,grid=[3,1,2,1],size=30,visible=False , align="left")
        #self.number2_field=Text(self.box1,grid=[3,1,1,1],size=30,align="left",visible=False)
        self.start=PushButton(self.box1, grid=[1,3,4,1],visible=True, text="Start",command=self.start, align="left")
        self.counter=0
        self.correct=0
        self.wrong=0
        self.first_number=0
        self.second_number=0
        self.input_text=Text(self.box1, grid=[5,1,2,1], visible=False, align="left")
        self.correct_text=Text(self.box1, grid=[2,0,1,1],visible=False, align="left")
        self.wrong_text=Text(self.box1, grid=[2,0,3,1], visible=False, align="right")
        self.percent_text=Text(self.box1, grid=[5,0,1,1],visible=True, align="left") 
        self.remaining=Text(self.box1, grid=[0,0,2,1], text="99 tilbage", visible=False, align="left")
        #self.dont_know=PushButton(self.box1, grid=[3,4,5,1],visible=False, text="jeg ved det ikke...", command=self.cont, align="left")
        self.answer=TextBox(self.box1,grid=[3,3,2,1], visible=False, command=self.answer_given, align="left")
        self.timer_text=Text(self.box1,grid=[3,5], visible=False, align="left")
        self.timer=0
        self.rigtigt_text=Text(self.box1, grid=[2,4,5,2], text="RIGTIGT!!", size=34,font="Helvetica", visible=False, align="left")
        self.forkert_text=Text(self.box1, grid=[2,4,5,2], text="Forkert",color="red", size=34,font="Helvetica", visible=False, align="left")
        self.game_over=Text(self.box1, grid=[0,2,6,2],text="Something something", size=18, font="Helvetica", visible=False, align="center")
        
    def start(self):
        self.correct_text.show()
        self.wrong_text.show()
        self.timer_text.show()
        self.timer_text.repeat(1000, self.timeshift)
        self.number1_field.value="{0} * {1}".format(l2[self.counter][0],l2[self.counter][1])
        self.correct_val=0
        self.wrong_val=0
        self.time_val=0
        self.percent_val=0
        self.number1_field.show()
        self.start.hide()
        #self.dont_know.show()
        self.remaining.show()
        self.answer.show()
        self.answer.focus()
        self.answer_no=0
        self.key1=0
        self.correct_answer=0
        self.value1=int(float(l2[self.counter][0]))
        self.value2=int(float(l2[self.counter][1]))
        self.correct_answer=(self.value1*self.value2)
        self.counter+=1
        print(self.correct_answer)
        
    def timeshift(self):
        self.timer+=1
        self.timer_text.value=self.timer
        
        
    def cont(self):
        self.answer.focus()
        self.answer.value=""
        self.counter+=1
        if self.counter>=99:
            self.stop()
        else:
            self.percent=round(((self.correct/(self.counter-1))*100),2)
            self.correct_text.value="{0} rigtige".format(self.correct)
            self.wrong_text.value="{0} forkerte".format(self.wrong)
            self.percent_text.value="{0} procent".format(self.percent)
            self.number1_field.value="{0} * {1}".format(l2[self.counter][0],l2[self.counter][1])
            #self.number2_field.value="* {0}".format(l2[self.counter][1])
            self.remaining.value="{0} tilbage".format(99-self.counter)
            self.value1=int(float(l2[self.counter][0]))
            self.value2=int(float(l2[self.counter][1]))
            self.correct_answer=(self.value1*self.value2)
            print(self.correct_answer)
            
    def stop(self):
        self.timer_text.cancel(self.timeshift)
        self.answer.hide()
        self.timer_text.hide()
        self.percent_text.hide()
        self.remaining.hide()
        print("spillet er slut")
        stop_text="""Game over.
Du fik {0} rigtige.
du brugte {1} sekunder.
Du har svaret {2} procent rigtigt.""".format(self.correct,self.timer,self.percent)
        self.game_over.value=stop_text
        self.game_over.show()
        
        
    def rigtigt(self):
        self.rigtigt_text.show()
        self.rigtigt_text.after(1000, self.sluk_skilt)
        

    def forkert(self):
        self.forkert_text.show()
        self.answer.disable()
        self.det_rigtige_er="{0} * {1} = {2}".format(self.value1,self.value2,self.correct_answer)
        self.forkert_text.value="{0}".format(self.det_rigtige_er)
        self.forkert_text.after(3000, self.sluk_skilt)

    def sluk_skilt(self):
        self.rigtigt_text.hide()
        self.forkert_text.hide()
        self.answer.enable()
        
    def answer_given(self,key):
        self.answer.destroy()
        self.answer=TextBox(self.box1,grid=[3,3,2,1], visible=True, command=self.answer_given, align="left")
        self.answer.focus()
        print("correct answer is ")
        print (self.correct_answer)
        print("you pressed")
        key = int(float(key))
        print (key)
        if self.answer_no==0:
            if int(key)==int(self.correct_answer):
                print("RIGTIGT")
                self.rigtigt()
                self.correct+=1
                self.answer_no=0
                self.answer.value=""
                self.cont()
                
            else:
                self.key1=key
                self.answer_no=1
                self.input_text.value=key
                self.input_text.show()
        elif self.answer_no==1:
            print("2. knap trykket")
            print(self.key1+key)
            now_key=self.key1*10+key
            print(now_key)
            self.input_text.value=self.key1*10+key
            if now_key==int(self.correct_answer):
                print("RIGTIGT")
                self.rigtigt()
                self.answer.value=""
                self.correct+=1
                self.answer_no=0
                self.cont()
            else :
                print("FORKERT")
                self.wrong+=1
                self.answer_no=0
                self.forkert()
                self.cont()

game=multiplication()



