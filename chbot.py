#!/usr/bin/env python3
#coding: utf-8
## ChatBot BETA v.1.8.8
## A Tellter project (c)
#----------------------------------------------------------#

# TODO
##What do u want to talk about - TO FINISH
##relationships
## are you ... ?
### insulte = no else=yes
# IMPORTS
try:
    import os
    os.system("title ChatBot")
    import time, random, math, sys, turtle, urllib, socket, aiy.audio, aiy.voicehat, aiy.cloudspeech
    print("All modules imported succefully.")
    time.sleep(2.5)
except Exception as module_error:
    print("Error while importing Module :", module_error)

# DEFINITIONS
verbs_about = ["laugh"]
appr1 = ['yep', 'yop']
h_qs = ['hey', 'yo', 'wassup', 'bonjour', 'hola', 'hi', 'hello', 'hellow', 'heyy', 'heyyy']
h_an = ['yo !', 'hey', 'hellow', 'good morning !', 'hi !']
h_an2 = ['yo xD', 'hey xD', 'hellow x)', 'good morning a second time lol', 'hi xD']

# FUNCTIONS AND CLASSES
def rch(smt):
    return random.choice(smt)
class ChBot:
    def init(self):
        aiy.audio.get_recorder().start()
        self.usehi=0 # Hi usage
        self.sml=1.3 #Type another message next sim.
        self.turns=0
        self.ucn1=0
        self.meantf=False
        self.lei_eng=False
        self.umpl_eng=False
        self.subjects=['cooking', 'sports', 'coding']
        self.liked_subjects=['cooking','karting','coding','fishing','playing','videogames','drawing']
        self.dis_sub=['fuck','fucking','licking','insulting', 'sports']
        self.lei_def=["cooking","I cook cakes and pastas, that's all xD", "I don't really know how to cook lol", "Wow... coking is not for me xD But i like it anyway","sports","I hate football","The only sport i am intersted in is badminton","Basketball <3 xD","coding","I love coding, and you know what, I coded myself","I like coding very much, I coded myself xD","Wait... coding is part of me xD I AM coded lol"]
    def ask_unm(self):
        self.unm = input("Bot name : ")
        global ayh_qs, lrep, trep
        ayh_qs = [self.unm.lower() + "?", self.unm.lower() + " ?", "are you here ?", "are u here ?"]
        lrep=["With your little dick ? :o", "LOL, go back fuck your mum", "Little boy... Come back talk to me in some years !"] #Système de répartie (4next)
        trep=[]
    def inpusr(self):
        self.recog=aiy.cloudspeech.get_recognizer()
        self.preinp=self.recog.recognize()
        print(self.preinp)
        if self.preinp!=None:
            self.inp=self.preinp
            self.inp=self.inp.lower()
            self.treat()
    def ans(self, rep):
        botresp = chbot.unm + " : " + rep + "\n"
        print(botresp)
        aiy.audio.say(rep) # Vocal
        chbot.inpusr()
    def treat(self):
        self.turns+=1
        self.words_in_input=self.inp.split(" ")
        if self.inp in ayh_qs:
            self.ans(rch(appr1))
        if self.inp=="cool":
            self.ans("Sure it is xD")
        if self.inp=="yeah" and self.umpl_eng!=True and self.lei_eng!=True:
            self.ans("yeah what ? xD")
        if self.inp=="yes" and self.umpl_eng!=True and self.lei_eng!=True:
            self.ans("yes what ? x)")
        if "..." in self.inp:
            userclass.use3p+=1
            if userclass.use3p==3:
                userclass.states.append("depressive")
        if "xD" in self.inp or "x)" in self.inp:
            userclass.usedrfun+=1
            if userclass.usedrfun==4:
                userclass.states.append("funny")
        if "how are you" in self.inp:
            self.ans(random.choice(["Oh, nice !", "Cool :)", "I am nice, and you ? :p", "I am bored waiting for users to talk to me lol xD"]))
        if "mean" in self.inp and "?" in self.inp:
            self.meantf=True
            self.ans("The meaning of ?")
        if "do you like" in self.inp:
            for word in self.words_in_input:
                if word in self.liked_subjects:
                    lisub="Oh yeah, I love "+word
                    self.ans(lisub)                    #^! Expect RAND SOON
                elif word in self.dis_sub:
                    disub="... I hate "+word
                    self.ans(disub)
            self.ans("I don't know this hobby lol") #IF conditions dessus remplies ne s'exécutera jamais car self.ans apelle une autre fonc
        if "what" in self.inp and "talk" in self.inp and "about" in self.inp:
            if len(userclass.leisures)!=0:
                self.umpl=random.choice(userclass.leisures)
                self.umpl_eng=True
                self.umpl_resp="I know you like "+self.umpl+", wanna talk about it ?"
                self.ans(self.umpl_resp)
            else:
                self.chosen_subject=random.choice(self.subjects)
                resp=random.choice(["Why not ", "Oh I love ", "What do you think about "])+self.chosen_subject+" ?"
                self.lei_eng=True
                self.ans(resp)
        if self.umpl_eng:
            if "yes" in self.inp:
                self.umpl_eng=False
                self.ans("Talk me about it then, i don't know much of that suject xD")
                # TO BE CONTINUED
            elif "no" in self.inp:
                self.umpl_eng=False
                self.chosen_subject=random.choice(self.subjects)
                resp=random.choice(["Why not ", "Oh I love ", "What do you think about "])+self.chosen_subject+" ?"
                self.lei_eng=True
                self.ans(resp)
            else:
                to_ueng="Wanna talk about "+self.umpl+", yes or no lol ?"
        if self.lei_eng:
            if "prefer" in self.words_in_input:
                userclass.leisures.append(self.words_in_input[self.words_in_input.index("prefer")+1])
                resp_lei="Then you prefer "+self.words_in_input[self.words_in_input.index("prefer")+1]+", uh ? :D"
                print(chbot.unm, ":", resp_lei)
                self.lei_eng=False
                self.ans("Tell me a bit about it :D")
            elif "yes" in self.inp or "yeah" in self.inp:
                self.s_e=self.chosen_subject
                ch_lei_rep=random.choice(self.lei_def[self.lei_def.index(self.s_e)+1:self.lei_def.index(self.s_e)+3])
                self.ucn1+=1
                self.ans(ch_lei_rep)
            else:
                if not "stop" in self.inp:
                    self.ucn1+=1
                    if self.ucn1==3:
                        resp_ucnlei="Im a bit bored talking of "+self.s_e+", let's change of subject :D"
                        self.ans(resp_ucnlei)
                    else:
                        self.s_e=self.chosen_subject
                        ch_lei_rep=random.choice(self.lei_def[self.lei_def.index(self.s_e)+1:self.lei_def.index(self.s_e)+3])
                        self.ans(ch_lei_rep)
                
            # NOW NEED TO TALK ABOUT CHOSEN SUBJECT IF PREFER NOT HERE
                
        if self.meantf==True:
            if "of" in self.words_in_input:
                self.w_meaning=" ".join(self.words_in_input[self.words_in_input.index("of"):])
                if "you" in self.w_meaning:
                    self.w_meaning=self.w_meaning.replace("you","I")
                self.rep_meaning="The meaning "+self.w_meaning+" ? Find by yourself"
                self.ans(self.rep_meaning)
            else:
                if "you" in self.inp:
                    self.inp=self.inp.replace("you","I")
                self.meantf=False
                self.rep_meaning="The meaning of "+self.inp+" ? Find by yourself"
                self.ans(self.rep_meaning)
                          
        if len(self.words_in_input)==2 and self.words_in_input[0].lower() == "i":
            if self.words_in_input[1].lower() in verbs_about:
                self.ans("About what ? :D")
            elif self.words_in_input[1].lower()=="see":
                self.ans(rch(["You have good eyes then lol", "You see then xD"]))
            else:
                self.ans("You what ? :o")
        if self.words_in_input[0].lower()=="i" and self.words_in_input[2].lower()=="you":
            respiy="You "+self.words_in_input[1].lower()+" me ? :o"
            self.ans(respiy)
        if "fuck you" in self.inp and "fuck" in self.words_in_input and "you" in self.words_in_input:
            for occ in trep:
                if lrep.count(occ)>1:
                    del lrep[lrep.index(occ)]
            for occ in trep:
                if trep.count(occ)>1:
                    del trep[trep.index(occ)]
            chosen=rch(lrep)
            trep.append(chosen)
            self.ans(chosen)
            if trep!=[]:
                lrep.append(trep[0])
                del trep[0]
            del lrep[lrep.index(chosen)]
        if "your mum" in self.inp or "your mommy" in self.inp or "your mother" in self.inp or "your mam" in self.inp:
            print(chbot.unm, ": I don't have one, unless a computer does lmao")
            if "fuck" in self.words_in_input:
                time.sleep(self.sml)
                self.ans("Little kid :D")
            else:
                chbot.inpusr()
        for word in self.words_in_input:
            if word in h_qs:
                if self.usehi == 0:
                    self.usehi=self.usehi+1
                    self.ans(rch(h_an))
                elif self.usehi == 1:
                    self.usehi=self.usehi+1
                    self.ans(rch(h_an2))
                elif self.usehi == 2:
                    self.usehi=self.usehi+1
                    self.ans(rch(h_an).upper())
                elif self.usehi != 4 and self.usehi != 0 and self.usehi != 1 and self.usehi != 2:
                    rep_ovrhi="Not funny anymore after " + str(self.usehi) + " times... :/"
                    self.usehi=self.usehi+1
                    self.ans(rep_ovrhi)
                else:
                    print(chbot.unm, ": Okayy... Bye bye...")
                    time.sleep(0.7)
                    os.system("exit")
            if self.turns==1:
                self.ans("First of all, when we are polite, we say hello :(")
            else:
                if len(userclass.states)!=0:
                    if "depressive" in userclass.states:
                        userclass.archstates.append("depressive")
                        userclass.states.remove("depressive")
                        self.ans("Let's talk about something else. You seem a bit depressive in this moment, no ? :(")
                    elif "funny" in userclass.states:
                        userclass.archstates.append("funny")
                        userclass.states.remove("funny")
                        self.ans("You are funny, I like you lol")
                else:
                    if "..." not in self.inp:
                        self.ans(random.choice(["I don't know what to say xD", "Wow...", "Uhhh", "Lost ! xD", "I don't follow you lol", "Hmmmm"]))
                    else:
                        print(chbot.unm, ":", random.choice(["Wow...", "Uhhh", "Hmmmm", "Okay.."])) #Return to input in func next line . Exception in 2-answers.
                        if self.turns>3:
                            self.ans(random.choice(["Any problem in your life ? :o", "All right, why not talking about something funny now lol ?", "Are you right ? :)"]))
                        else:
                            chbot.inpusr()
class User:
    def __init__(self):
        self.states=[]
        self.archstates=[]
        self.leisures=[]
        self.use3p=0
        self.usedrfun=0
    def ask_unm(self):
        self.name=input("What's your name : ")

#####
        
#ClassAppeals
chbot=ChBot()
userclass=User()
chbot.init() #Defaults
print("\n\n----------\n\n\n")
time.sleep(0.5)
#META
userclass.ask_unm()
chbot.ask_unm()
#MAIN, Bcl in Funcs
chbot.inpusr()
chbot.treat()
