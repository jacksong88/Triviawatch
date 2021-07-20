#import libraries
import tkinter as tk            
from tkinter import ttk         
import pygame                   
import time        
import os             
from PIL import ImageTk, Image  

#Intro Window
#Creates the Intro window with all the necessary widgets functions.
def CreateIntroWindowAndFunctions():

        #function to play the starting music of program
        def PlayIntroMusic():                
                #play intro music
                pygame.mixer.music.load(os.path.join("sounds","IntroTheme.mp3")) 
                pygame.mixer.music.play()

        #function for the QuitButton to play button sound and close game
        def QuitFunction():               
                #Play Button sound effect if user chose to have sound effects
                if(NoSound_tk.get()==0):
                        pygame.mixer.music.load(os.path.join("sounds","ButtonSoundEffect.mp3")) 
                        pygame.mixer.music.play()
                
                #destroy window
                IntroWindow.destroy()

        #function for the CreditsButton to play button sound and show credits
        def CreditsFunction():               
                #Play Button sound effect if user chose to have sound effects
                if(NoSound_tk.get()==0):
                        pygame.mixer.music.load(os.path.join("sounds","ButtonSoundEffect.mp3"))
                        pygame.mixer.music.play()
                
                #Create credits labels
                CreditsTitleLabel=tk.Label(CreditsFrame,text="Credits",
                                           font = "times 18 bold",
                                           bg="gray87")
                CreatedByLabel=tk.Label(CreditsFrame,text="Created by: Jack Song",
                                        font="times 16",
                                        bg="gray87")
                ImagesByLabel=tk.Label(CreditsFrame,text="Images are from Blizzard and Google",
                                        font="times 14",
                                        bg="gray87")
                SoundsFromLabel=tk.Label(CreditsFrame,text="Sounds From SoundStripe and Youtube",
                                         font="times 14",
                                         bg="gray87")
                
                #Place credits labels
                CreditsTitleLabel.place(x=120,y=15,width=100,height=20)
                CreatedByLabel.place(x=70,y=70,width=200,height=25)
                ImagesByLabel.place(x=30,y=120,width=300,height=25)
                SoundsFromLabel.place(x=20,y=170,width=315,height=25)

        #function for the InstructionsButton to play button sound and show instructions
        def InstructionsFunction():
                #Play Button sound effect if user chose to have sound effects
                if(NoSound_tk.get()==0):
                        pygame.mixer.music.load(os.path.join("sounds","ButtonSoundEffect.mp3")) 
                        pygame.mixer.music.play()
    
                
                #Create Instructions labels
                InstructionsTitleLabel=tk.Label(InstructionsFrame,text="Instructions",
                                                font = "times 18 bold",
                                                bg="gray87")
                MainInstructionsLabel=tk.Label(InstructionsFrame,
                                               font="times 14",
                                               text=INSTRUCTIONS,
                                               bg="gray87")
                #Place Instructions labels
                InstructionsTitleLabel.place(x=100,y=10,width=200,height=20)
                MainInstructionsLabel.place(x=10,y=30,width=390,height=250)

        #function for the StartButton to play button sound and start the game
        def StartFunction():
                #Play Button sound effect if user chose to have sound effects
                if(NoSound_tk.get()==0):
                        pygame.mixer.music.load(os.path.join("sounds","ButtonSoundEffect.mp3")) 
                        pygame.mixer.music.play()
                
		#Destroy intro window
                IntroWindow.destroy()

                #Calls Game Window Function
                #passes whether or not user wants sound to next function
                CreateGameWindowAndFunctions(NoSound_tk.get())
                
	#Function to create all of the intro window buttons	
        def CreateIntroButtons():
                #Create Buttons
                QuitButton=tk.Button(IntroButtonFrame, text="Quit",
                                     fg="red",
                                     bg="gray70",
                                     font="Arial 20",
                                     command=QuitFunction)
                CreditsButton=tk.Button(IntroButtonFrame, text="Credits",
                                     bg="gray70",
                                     font="Arial 20",
                                     command=CreditsFunction)
                StartButton=tk.Button(IntroButtonFrame, text="Start",
                                     fg="green",
                                     bg="gray70",
                                     font="Arial 20",
                                     command=StartFunction)
                InstructionsButton=tk.Button(IntroButtonFrame, text="Instructions",
                                     bg="gray70",
                                     font="Arial 20",
                                     command=InstructionsFunction)

		#Place Buttons
                InstructionsButton.place(x=40,y=25,width=250,height=100)
                StartButton.place(x=330,y=25,width=250,height=100)
                CreditsButton.place(x=620,y=25,width=250,height=100)
                QuitButton.place(x=910,y=25,width=250,height=100)

        #function to stop playing sounds
        def StopSound():
                #stop music and sounds from playing if no sound is selected
                if(NoSound_tk.get()==1):
                        pygame.mixer.music.stop()

        #Function to create the checkbutton           
        def CreateCheckButton():                
                #create check button
                NoSoundCheckButton=tk.Checkbutton(IntroTitleFrame,text="No Sound",
                                                variable=NoSound_tk,
                                                font="comicsans 16",
                                                bg="ivory2",
                                                command=StopSound)

                #place check button
                NoSoundCheckButton.place(x=1050,y=80,width=120,height=25)

        #function to create all the intro window labels
        def CreateIntroLabels():
		#Create Labels
                TitleLabel=tk.Label(IntroTitleFrame,text="TRIVIAWATCH",
                                    font="ComicSans 35",
                                    bg="ivory2")
                SubtitleLabel=tk.Label(IntroTitleFrame,text="How well do you know your Overwatch?",
                                       font="ComicSans 16",
                                       bg="ivory2")
		#Place Labels
                TitleLabel.place(x=410,y=40,width=400,height=40)
                SubtitleLabel.place(x=410,y=115,width=400,height=25)

        #function to create the starting image  
        def CreateIntroImage():
		#Open intro image from file
                IntroImage=Image.open(os.path.join("images","Overwatchlogo.png"))
                
                #resize image size to fit
                IntroImage=IntroImage.resize((300,300),Image.ANTIALIAS)
                
                #convert into tkinter image type
                IntroImage = ImageTk.PhotoImage(IntroImage)

                #put image as label
                ImageLabel = tk.Label(IntroWindow, image=IntroImage)
                
		#Place Image
                ImageLabel.place(x=450,y=200)

                #allow image to appear on screen
                IntroWindow.mainloop()

        ###################################################
        #Intro Window Main Program
        #create intro window, set minsize, title, background
        IntroWindow=tk.Tk()
        IntroWindow.minsize(width=1200,height=700)
        IntroWindow.title("TriviaWatch - Jack Song")
        IntroWindow.configure(bg="gray87")

        #create intro window frames, set width, height and background colour
        IntroTitleFrame=tk.Frame(IntroWindow,width=1200,height=200, bg="ivory2")
        InstructionsFrame=tk.Frame(IntroWindow,width=400,height=350, bg="gray87")
        CreditsFrame=tk.Frame(IntroWindow,width=350,height=350, bg="gray87")
        IntroButtonFrame=tk.Frame(IntroWindow,width=1200,height=150, bg="ivory2")
        
        #place frames
        IntroTitleFrame.place(x=0,y=0)
        InstructionsFrame.place(x=0,y=200)
        CreditsFrame.place(x=850,y=200)
        IntroButtonFrame.place(x=0,y=550)       

        #Initialize instructions constant
        INSTRUCTIONS="""                                    
Answer a total of 7 questions consisting of
multiple choice, fill in the blanks, and True or False.
The Questions are all Overwatch related questions.
Type your answer in a box for fill in the blanks.
Click one of the four buttons for multiple choice
Click either True or False for True or False.
To submit a question's answer, press submit.
Try using a hint when stuck on a question!
To move onto the next question, press next.
To start the game, pressed start.
Enjoy the Game!"""                                      #Instruction constant 

        #Initialize tkinter variable
        NoSound_tk=tk.IntVar()            #Variable to play sound or not

        #set initial value for tk variable
        NoSound_tk.set(0)
        
        #call needed function
        CreateIntroButtons()
        CreateIntroLabels()        
        CreateCheckButton()
        PlayIntroMusic()
        CreateIntroImage()

        #main loop
        IntroWindow.mainloop()


#################################################################################################

#Game Window
#Creates the game window with all the necessary widgets functions.    
def CreateGameWindowAndFunctions(NoSound_tk):

        #function to create all game window labels
        def CreateGameLabels():
		#Create Labels
                TitleLabel=tk.Label(GameTitleFrame,text="TRIVIAWATCH",
                                    font="ComicSans 35",
                                    bg="ivory2")
                QuestionNumberLabel=tk.Label(GameTitleFrame, text="Question "+str(QuestionNum_tk.get())+":",
                                             font="ComicSans 18",
                                             bg="ivory2")
                QuestionTypeLabel=tk.Label(GameTitleFrame, text=GetQuestionType(),
                                           font="Comicsans 18",
                                           bg="ivory2")                
                QuestionsCorrectLabel=tk.Label(ScoreTrackFrame,text="Number of Questions Correct: ",
                                                font="times 14",
                                                bg="gray87")
                QuestionsCorrectNumberLabel=tk.Label(ScoreTrackFrame,textvariable=CorrectCnt_tk,
                                                     font="times 16",
                                                     bg="gray87")
                HintsLeftLabel=tk.Label(ScoreTrackFrame,text="Number of Hints Left: ",
                                        font="times 14",
                                        bg="gray87")
                HintsLeftNumberLabel=tk.Label(ScoreTrackFrame,textvariable=HintCnt_tk,
                                              font="times 16",
                                              bg="gray87")
                
		#Place Labels
                TitleLabel.place(x=410,y=30,width=400,height=40)
                QuestionNumberLabel.place(x=450,y=90,width=130,height=30)
                QuestionTypeLabel.place(x=600, y=90,width=200,height=30)                
                QuestionsCorrectLabel.place(x=10,y=30,width=230,height=30)
                QuestionsCorrectNumberLabel.place(x=250,y=32,height=25)
                HintsLeftLabel.place(x=10,y=120,width=200,height=30)
                HintsLeftNumberLabel.place(x=230,y=122,height=25)

        #function to create all game window buttons
        def CreateGameButtons():
                #Create Buttons
                QuitButton=tk.Button(GameButtonFrame, text="Quit",
                                     fg="red",
                                     bg="gray70",
                                     font="Arial 20",
                                     command=QuitFunction)
                HintButton=tk.Button(GameButtonFrame, text="Hint",
                                     bg="gray70",
                                     font="Arial 20",
                                     command=HintFunction)
                NextButton=tk.Button(GameButtonFrame, text="Next",
                                     fg="green",
                                     bg="gray70",
                                     font="Arial 20",
                                     command=NextFunction)
                SubmitButton=tk.Button(GameButtonFrame, text="Submit",
                                     bg="gray70",
                                     font="Arial 20",
                                     command=SubmitFunction)

		#Place Buttons
                SubmitButton.place(x=40,y=25,width=250,height=100)
                NextButton.place(x=330,y=25,width=250,height=100)
                HintButton.place(x=620,y=25,width=250,height=100)
                QuitButton.place(x=910,y=25,width=250,height=100)

        #Function to get the question type for the question its on      
        def GetQuestionType():
                #checks what question user is on, gives corresponding Question type
                if(QuestionNum_tk.get()==1):
                        return FILLINTHEBLANK
                elif(QuestionNum_tk.get()==2):
                        return MULTIPLECHOICE
                elif(QuestionNum_tk.get()==3):
                        return MULTIPLECHOICE
                elif(QuestionNum_tk.get()==4):
                        return MULTIPLECHOICE
                elif(QuestionNum_tk.get()==5):
                        return TRUEORFALSE
                elif(QuestionNum_tk.get()==6):
                        return TRUEORFALSE
                elif(QuestionNum_tk.get()==7):
                        return TRUEORFALSE

        #Function for Quitbutton to close program  
        def QuitFunction():
                #Play Button sound effect if user chose to have sound effects
                if(NoSound_tk==0):
                        pygame.mixer.music.load(os.path.join("sounds","ButtonSoundEffect.mp3")) 
                        pygame.mixer.music.play()

                #destroy game window
                GameWindow.destroy()

        #Function for HintButton to display hint if user has hints
        def HintFunction():
                #Play Hint sound effect if user chooses to have sound
                if(NoSound_tk==0):
                        pygame.mixer.music.load(os.path.join("sounds","HintSoundEffect.mp3")) 
                        pygame.mixer.music.play()

                #Create label to cover previous labels and create Hint Title Label
                BlankLabel=tk.Label(HintFrame, bg="gray87")
                HintTitleLabel=tk.Label(HintFrame,text="Hint",
                                        font="Times 18 underline",
                                        bg="gray87")
                
                #place BlankLabel
                BlankLabel.place(x=0,y=0,width=300,height=200)
                HintTitleLabel.place(x=50,y=10,width=200,height=50)

                #Gives hint if user has hints
                #otherwise, tell user all hints are used
                if(HintCnt_tk.get()>0):
                        #subtract one hint
                        HintCnt_tk.set(HintCnt_tk.get()-1)

                        #Create Label with the hint
                        HintLabel=tk.Label(HintFrame,text=GiveHint(),
                                           font="times 14",
                                           bg="gray87")

                        #Place Label
                        HintLabel.place(x=10,y=50,width=280,height=120)

                else:
                        #Create User Message Label
                        NoHintsLeftLabel=tk.Label(HintFrame, text="You have used all your hints!",
                                                  font="times 16",
                                                  bg="gray87")
                        SecondNoHintsLeftLabel=tk.Label(HintFrame,text="Nice Try!",
                                                        font="times 16",
                                                        bg="gray87")
                        
                        #place user message label
                        NoHintsLeftLabel.place(x=10,y=70,width=290,height=30)
                        SecondNoHintsLeftLabel.place(x=90,y=120,width=150,height=30)

        #give hint depending on the question number 
        def GiveHint():
                #checks what question user is on, gives corresponding hint
                if(QuestionNum_tk.get()==1):
                        return HINT1
                elif(QuestionNum_tk.get()==2):
                        return HINT2
                elif(QuestionNum_tk.get()==3):
                        return HINT3
                elif(QuestionNum_tk.get()==4):
                        return HINT4
                elif(QuestionNum_tk.get()==5):
                        return HINT5
                elif(QuestionNum_tk.get()==6):
                        return HINT6
                elif(QuestionNum_tk.get()==7):
                        return HINT7

        #Function for next button to go to the next question   
        def NextFunction():
                #Play Button sound effect if user chose to have sound effects
                if(NoSound_tk==0):
                        pygame.mixer.music.load(os.path.join("sounds","ButtonSoundEffect.mp3")) 
                        pygame.mixer.music.play()
                
                #if user didn't submit, tell them to submit
                if(CanSubmit_tk.get()==True):
                        #Create Label
                        SubmitMessageLabel=tk.Label(GameWindow,text="Please Submit before moving on.",
                                                    fg="red",
                                                    font="times 16",
                                                    bg="gray87")
                        #place Label
                        SubmitMessageLabel.place(x=300,y=510,width=300,height=25)
                        return
                        
                #clear useranswer from last question
                UserAnswer_tk.set(" ")
                
                #Allow user to submit again for new question
                CanSubmit_tk.set(True)
                
                #adds 1 to the question number
                QuestionNum_tk.set(QuestionNum_tk.get()+1)

                #if all 7 questions are asked, the game finishes
                #destroy game window and show end window
                #pass the number of correct value to next function
                #also pass wether or not user wants sound
                if(QuestionNum_tk.get()>=8):
                        GameWindow.destroy()
                        CreateEndWindowAndFunctions(CorrectCnt_tk.get(), NoSound_tk)
                        return
                        
                #updates question number and type
                CreateGameLabels()

                #create blank labels
                QuestionBlankLabel=tk.Label(QuestionFrame,bg="gray87")
                QuestionAnsBlankLabel=tk.Label(GameWindow,bg="gray87")
                GameResultBlankLabel=tk.Label(GameResultFrame,bg="gray87")
                HintBlankLabel=tk.Label(HintFrame,bg="gray87")
                QuestionImageBlankLabel=tk.Label(GameImageFrame,bg="gray87")

                #place blank labels
                QuestionBlankLabel.place(x=0,y=0,width=600,height=400)
                QuestionAnsBlankLabel.place(x=0,y=250,width=600,height=300)
                GameResultBlankLabel.place(x=0,y=0,width=600,height=400)
                HintBlankLabel.place(x=0,y=50,width=300,height=200)
                QuestionImageBlankLabel.place(x=0,y=0,width=300,height=250)

                #create next question widgets
                CreateNextQuestion()
                
        #Function to create necessary widgets for each question        
        def CreateNextQuestion():
                #creates widgets for corresponding question number
                if(QuestionNum_tk.get()==1):
                        #create question labels
                        Question1Label=tk.Label(QuestionFrame, text=QUESTION1,
                                                font = "times 18",
                                                bg="gray87")
                        InputAnswer1Label=tk.Label(QuestionFrame,text="Please Enter your answer -->",
                                                   font="times 16",
                                                   bg="gray87")

                        #place question labels
                        Question1Label.place(x=30,y=10,width=500,height=25)
                        InputAnswer1Label.place(x=10,y=300,width=300,height=30)

                        #create Entry
                        AnswerEntry=tk.Entry(QuestionFrame,textvariable=UserAnswer_tk)

                        #place Entry
                        AnswerEntry.place(x=320,y=305,width=100,height=20)
                
                elif(QuestionNum_tk.get()==2):
                        #create question label
                        Question2Label=tk.Label(QuestionFrame,text=QUESTION2,
                                               font="times 16",
                                                bg="gray87")

                        #place question label
                        Question2Label.place(x=10,y=10,width=570,height=100)

                        #create Radio buttons
                        Question2Ans1RadioButton=tk.Radiobutton(GameWindow,text="a) Bastion",
                                                       font="times 18",
                                                       value="a",
                                                       bg="gray87",
                                                       variable=UserAnswer_tk)
                        Question2Ans2RadioButton=tk.Radiobutton(GameWindow,text="b) Ana",
                                                       font="times 18",
                                                       value="b",
                                                       bg="gray87",
                                                       variable=UserAnswer_tk)
                        Question2Ans3RadioButton=tk.Radiobutton(GameWindow,text="c) D.va",
                                                       font="times 18",
                                                       value="c",
                                                       bg="gray87" ,
                                                       variable=UserAnswer_tk)
                        Question2Ans4RadioButton=tk.Radiobutton(GameWindow,text="d) Sombra",
                                                       font="times 18",
                                                       value="d",
                                                       bg="gray87",        
                                                       variable=UserAnswer_tk)

                        #place radio buttons
                        Question2Ans1RadioButton.place(x=20,y=280)
                        Question2Ans2RadioButton.place(x=20,y=340)
                        Question2Ans3RadioButton.place(x=20,y=400)
                        Question2Ans4RadioButton.place(x=20,y=460)

                elif(QuestionNum_tk.get()==3):
                        #create question label
                        Question3Label=tk.Label(QuestionFrame,text=QUESTION3,
                                               font="times 18",
                                               bg="gray87")

                        #place question label
                        Question3Label.place(x=10,y=10,width=570,height=50)

                        #create Radio buttons
                        Question3Ans1RadioButton=tk.Radiobutton(GameWindow,text="a) Shields for Teammates",
                                                       font="times 18",
                                                       value="a",
                                                       bg="gray87",      
                                                       variable=UserAnswer_tk)
                        Question3Ans2RadioButton=tk.Radiobutton(GameWindow,text="b) Hack",
                                                       font="times 18",
                                                       value="b",
                                                       bg="gray87", 
                                                       variable=UserAnswer_tk)
                        Question3Ans3RadioButton=tk.Radiobutton(GameWindow,text="c) Fly",
                                                       font="times 18",
                                                       value="c",
                                                       bg="gray87",
                                                       variable=UserAnswer_tk)
                        Question3Ans4RadioButton=tk.Radiobutton(GameWindow,text="d) Wallride",
                                                       font="times 18",
                                                       value="d",
                                                       bg="gray87",         
                                                       variable=UserAnswer_tk)

                        #place radio buttons
                        Question3Ans1RadioButton.place(x=20,y=280)
                        Question3Ans2RadioButton.place(x=20,y=340)
                        Question3Ans3RadioButton.place(x=20,y=400)
                        Question3Ans4RadioButton.place(x=20,y=460)
                        
                elif(QuestionNum_tk.get()==4):
                        #create question label
                        Question4Label=tk.Label(QuestionFrame,text=QUESTION4,
                                               font="times 18",
                                               bg="gray87")

                        #place question label
                        Question4Label.place(x=10,y=10,width=570,height=50)

                        #create Radio buttons
                        Question4Ans1RadioButton=tk.Radiobutton(GameWindow,text="a) London Spitfire",
                                                       font="times 18",
                                                       value="a",
                                                       bg="gray87", 
                                                       variable=UserAnswer_tk)
                        Question4Ans2RadioButton=tk.Radiobutton(GameWindow,text="b) NewYork Excelsior",
                                                       font="times 18",
                                                       value="b",
                                                       bg="gray87", 
                                                       variable=UserAnswer_tk)
                        Question4Ans3RadioButton=tk.Radiobutton(GameWindow,text="c) Shanghai Dragons",
                                                       font="times 18",
                                                       value="c",
                                                       bg="gray87", 
                                                       variable=UserAnswer_tk)
                        Question4Ans4RadioButton=tk.Radiobutton(GameWindow,text="d) Toronto Defiant",
                                                       font="times 18",
                                                       value="d",
                                                       bg="gray87", 
                                                       variable=UserAnswer_tk)

                        #place radio buttons
                        Question4Ans1RadioButton.place(x=20,y=280)
                        Question4Ans2RadioButton.place(x=20,y=340)
                        Question4Ans3RadioButton.place(x=20,y=400)
                        Question4Ans4RadioButton.place(x=20,y=460)
                        
                elif(QuestionNum_tk.get()==5):
                        #create question label
                        Question5Label=tk.Label(QuestionFrame,text=QUESTION5,
                                               font="times 18",
                                               bg="gray87")

                        #place question label
                        Question5Label.place(x=10,y=10,width=570,height=50)

                        #create Radio buttons
                        Question5TrueRadioButton=tk.Radiobutton(GameWindow,text="True",
                                                       font="times 22",
                                                       value="true",
                                                       bg="gray87", 
                                                       variable=UserAnswer_tk)
                        Question5FalseRadioButton=tk.Radiobutton(GameWindow,text="False",
                                                       font="times 22",
                                                       value="false",
                                                       bg="gray87", 
                                                       variable=UserAnswer_tk)

                        #place radio buttons
                        Question5TrueRadioButton.place(x=90,y=280)
                        Question5FalseRadioButton.place(x=360,y=280)
                        
                elif(QuestionNum_tk.get()==6):
                        #create question label
                        Question6Label=tk.Label(QuestionFrame,text=QUESTION6,
                                               font="times 16",
                                                bg="gray87")

                        #place question label
                        Question6Label.place(x=10,y=10,width=570,height=50)

                        #create Radio buttons
                        Question6TrueRadioButton=tk.Radiobutton(GameWindow,text="True",
                                                       font="times 22",
                                                       value="true",
                                                       bg="gray87", 
                                                       variable=UserAnswer_tk)
                        Question6FalseRadioButton=tk.Radiobutton(GameWindow,text="False",
                                                       font="times 22",
                                                       value="false",
                                                       bg="gray87", 
                                                       variable=UserAnswer_tk)

                        #place radio buttons
                        Question6TrueRadioButton.place(x=90,y=280)
                        Question6FalseRadioButton.place(x=360,y=280)
                        
                elif(QuestionNum_tk.get()==7):
                        #create question label
                        Question7Label=tk.Label(QuestionFrame,text=QUESTION7,
                                               font="times 22",
                                                bg="gray87")

                        #place question label
                        Question7Label.place(x=10,y=10,width=570,height=50)
                        
                        #create Radio buttons
                        Question7TrueRadioButton=tk.Radiobutton(GameWindow,text="True",
                                                       font="times 22",
                                                       value="true",
                                                       bg="gray87", 
                                                       variable=UserAnswer_tk)
                        Question7FalseRadioButton=tk.Radiobutton(GameWindow,text="False",
                                                       font="times 22",
                                                       value="false",
                                                       bg="gray87",
                                                       variable=UserAnswer_tk)

                        #place radio buttons
                        Question7TrueRadioButton.place(x=90,y=280)
                        Question7FalseRadioButton.place(x=360,y=280)

        #Function for Submit button to tell user their answer result
        #Show User correct answer        
        def SubmitFunction():
                #if user already submitted, they cannot submit again
                if(CanSubmit_tk.get()==False):
                        return

                #if user did not answer or pick an answer
                #tell user to answer the question
                if(UserAnswer_tk.get()==" "):
                        #Create Label
                        AnswerQuestionMessageLabel=tk.Label(GameWindow,text="""Please Answer the question
before submitting""",
                                                            fg="red",
                                                            font="times 14",
                                                            bg="gray87")
                        #place Label
                        AnswerQuestionMessageLabel.place(x=10,y=500,width=300,height=40)
                        return
                        
                #checks if UserAnswer is correct
                #if correct, Correct counter +1
                if(IsAnswerCorrect(UserAnswer_tk.get().lower())):
                        #play correct sound effect if user chose to have sounds
                        if(NoSound_tk==0):
                                pygame.mixer.music.load(os.path.join("sounds","CorrectSoundEffect.mp3")) 
                                pygame.mixer.music.play()

                        #add counter by 1
                        CorrectCnt_tk.set(CorrectCnt_tk.get()+1)
                        
                        #Create label to tell user they are correct
                        UserResultLabel=tk.Label(GameResultFrame, text="You are CORRECT!!!",
                                                 font="Times 17",
                                                 fg="green",
                                                 bg="gray87")
                        CongratsLabel=tk.Label(GameResultFrame,text="Excellent Job!",
                                                 font="Times 17",
                                                 fg="green",
                                                 bg="gray87")
                        
                        #place label
                        UserResultLabel.place(x=60,y=10,width=220,height=25)
                        CongratsLabel.place(x=93,y=60,width=150,height=25)
                else:
                        #play incorrect sound effect if user chose to have sounds
                        if(NoSound_tk==0):
                                pygame.mixer.music.load(os.path.join("sounds","IncorrectSoundEffect.mp3")) 
                                pygame.mixer.music.play()
                        
                        #Create label to tell user they are incorrect and the correct answer
                        UserResultLabel=tk.Label(GameResultFrame, text="You are Incorrect!!!",
                                                 font="Times 16",
                                                 fg="red",
                                                 bg="gray87")
                        CorrectAnswerLabel=tk.Label(GameResultFrame, text=GetCorrectAns(),
                                                    font="Times 14",
                                                    bg="gray87")

                        #place label
                        UserResultLabel.place(x=60,y=10,width=180,height=25)
                        CorrectAnswerLabel.place(x=10,y=40,width=280,height=100)
                        
                #after submitting, prevent user from submitting again
                CanSubmit_tk.set(False)

                #show image about the question when user finish answering
                ShowQuestionImage()

        #Function to check if the User Answer is correct       
        def IsAnswerCorrect(UserAns):
                #checks what question user is on
                #then check if UserAnswer qualifes for multiple
                #correct answers for the question.
                if(QuestionNum_tk.get()==1):
                        #Remove all whitespaces 
                        if(UserAns.replace(" ","")==ANS1_1):
                                return True
                        elif(UserAns.replace(" ","")==ANS1_2):
                                return True;
                        return False
                elif(QuestionNum_tk.get()==2):
                        if(UserAns==ANS2):
                                return True
                        return False
                elif(QuestionNum_tk.get()==3):
                        if(UserAns==ANS3):
                                return True
                        return False
                elif(QuestionNum_tk.get()==4):
                        if(UserAns==ANS4):
                                return True
                        return False
                elif(QuestionNum_tk.get()==5):
                        if(UserAns==ANS5):
                                return True
                        return False
                elif(QuestionNum_tk.get()==6):
                        if(UserAns==ANS6):
                                return True
                        return False
                elif(QuestionNum_tk.get()==7):
                        if(UserAns==ANS7):
                                return True
                        return False
                
        #function to get the correct answer for question        
        def GetCorrectAns():
                #checks what question user is on
                #gives corresponding correct answer when user answers wrong
                if(QuestionNum_tk.get()==1):
                        return CORRECTANSMESSAGE1
                elif(QuestionNum_tk.get()==2):
                        return  CORRECTANSMESSAGE2
                elif(QuestionNum_tk.get()==3):
                        return CORRECTANSMESSAGE3
                elif(QuestionNum_tk.get()==4):
                        return CORRECTANSMESSAGE4
                elif(QuestionNum_tk.get()==5):
                        return CORRECTANSMESSAGE5
                elif(QuestionNum_tk.get()==6):
                        return CORRECTANSMESSAGE6
                elif(QuestionNum_tk.get()==7):
                        return CORRECTANSMESSAGE7

        #function to show the image for question     
        def ShowQuestionImage():               
                #Open Question image from file depending on question num
                QuestionImage=Image.open(os.path.join("images","Question"+str(QuestionNum_tk.get())+"Image.jpg"))
        
                #resize image size to fit
                QuestionImage=QuestionImage.resize((300,250),Image.ANTIALIAS)
        
                #convert into tkinter image type
                QuestionImage = ImageTk.PhotoImage(QuestionImage)

                #put image as label
                ImageLabel = tk.Label(GameImageFrame, image=QuestionImage)
        
                #Place Image
                ImageLabel.place(x=0,y=0)

                #allow image to appear on screen
                GameWindow.mainloop()
                
        ##################################
        #Game Window Main Program
        #create game window, set minsize, title, background
        GameWindow=tk.Tk()
        GameWindow.minsize(width=1200,height=700)
        GameWindow.title("TriviaWatch - Jack Song")
        GameWindow.configure(bg="gray87")
        
        #create Game window frames with width, height and backgroun
        GameTitleFrame=tk.Frame(GameWindow,width=1200,height=150,bg="ivory2")
        GameButtonFrame=tk.Frame(GameWindow,width=1200,height=150,bg="ivory2")
        QuestionFrame=tk.Frame(GameWindow,width=600,height=400,bg="gray87")
        GameImageFrame=tk.Frame(GameWindow,width=300,height=250,bg="gray87")
        GameResultFrame=tk.Frame(GameWindow,width=300,height=150,bg="gray87")
        ScoreTrackFrame=tk.Frame(GameWindow,width=300,height=200,bg="gray87")
        HintFrame=tk.Frame(GameWindow,width=300,height=200,bg="gray87")
        
        #place frames
        GameTitleFrame.place(x=0,y=0)
        GameButtonFrame.place(x=0,y=550)
        QuestionFrame.place(x=0,y=150)
        GameImageFrame.place(x=600,y=150)
        GameResultFrame.place(x=600,y=400)
        ScoreTrackFrame.place(x=900,y=150)
        HintFrame.place(x=900,y=350)
        
        #initialize constants

        #hints contstants
        HINT1="Ashe says this during her Ultimate!"             
        HINT2="""                      She is 19 years old and                        
her names ends with an a."""                                    
        HINT3="Sombra is able to disable abilities."           
        HINT4="""The Team's name is not related
to Canada."""                                                   
        HINT5="""Tracer is the lowest hp
character in the game."""                                       
        HINT6="""Reinhardt is the second
oldest person in the game"""                                    
        HINT7="JunkerTown is in a desert"                       

        #question type constants
        FILLINTHEBLANK="Fill In The Blank!"                     
        MULTIPLECHOICE="Multiple Choice!"                       
        TRUEORFALSE="True Or False!"                            
        
        #question #1-7 answers constants
        ANS1_1="bob"                            
        ANS1_2="b.o.b."                         
        ANS2="c"                                
        ANS3="b"                                
        ANS4="a"                                
        ANS5="true"                             
        ANS6="false"                            
        ANS7="true"                             

        #correct answer messages constants
        CORRECTANSMESSAGE1="""Ashe says:
"BOB! DO SOMETHING!"
when using her ultimate ability"""                                      
        CORRECTANSMESSAGE2="""D.va is actually really good at gaming!
It was the main reason why
she was conscripted for Korea"""                                        
        CORRECTANSMESSAGE3="""Sombra's main job in game is to hack!"""  
        CORRECTANSMESSAGE4="""London Spitfire won the
2018 Overwatch League Season!"""                                        
        CORRECTANSMESSAGE5="""Tracer does have 150hp!"""                
        CORRECTANSMESSAGE6="""Reinhardt is a person,
Orisa was created by Efi!"""                                            
        CORRECTANSMESSAGE7="""JunkerTown is in Australia!"""            

        #question constants
        QUESTION1 = "Ashe says: _________! DO SOMETHING!"                               
        QUESTION2 = """This Korean Gamer was the World Champion of "StarCraft"  
for three years straight. She was conscripted by her country to
pilot a mech in the Omnic Crisis. Who is this character?"""                            
        QUESTION3 = "What does the character Sombra do?"                                
        QUESTION4 = "Which team won the 2018 Overwatch League Season?"                  
        QUESTION5 = "The Character Tracer has 150hp"                                    
        QUESTION6 = """Reinhardt was created by an eleven years old girl named Efi"""   
        QUESTION7 = "Junkertown is a place located in Australia"                        
        
                
        #initialize tk Variables
        UserAnswer_tk=tk.StringVar()            #tk variable for user answers
        QuestionNum_tk=tk.IntVar()              #tk variable to keep track of question numbers
        HintCnt_tk=tk.IntVar()                  #tk variable to keep track the amount of hints left
        CorrectCnt_tk=tk.IntVar()               #tk variable to keep track the amount of correct questions
        CanSubmit_tk=tk.BooleanVar()            #tk variable to keep track if user can submit.

        #set tk variables initial values
        UserAnswer_tk.set(" ")
        QuestionNum_tk.set(1)       
        HintCnt_tk.set(3)
        CorrectCnt_tk.set(0)
        CanSubmit_tk.set(True)
        
        #call needed function       
        CreateGameButtons()
        CreateGameLabels()
        CreateNextQuestion()

        #main loop
        GameWindow.mainloop()

#################################################################################################
#End Window
#Creates the End window with all the necessary widgets functions.   
def CreateEndWindowAndFunctions(CorrectCnt_tk, NoSound_tk):

        #Function to create labels for the end window
        def CreateEndLabels():
                #Create Labels
                TitleLabel=tk.Label(EndTitleFrame,text="TRIVIAWATCH",
                                    font="ComicSans 35",
                                    bg="ivory2")
                SubtitleLabel=tk.Label(EndTitleFrame,text="GAME ENDED",
                                       font="ComicSans 30",
                                       bg="ivory2")
                ThanksMessageLabel=tk.Label(EndMessageFrame,text="Thanks For Playing!",
                                            font="comicsans 40",
                                            bg="gray87")
                ResultTitleLabel=tk.Label(EndResultsFrame,text="Game Results",
                                          font="comicsans 20 underline",
                                          bg="gray87")
                ResultLabel=tk.Label(EndResultsFrame, text="You got "+str(CorrectCnt_tk)+"/7 questions correct!",
                                     font="times 18",
                                     bg="gray87")
                ResultMessageLabel=tk.Label(EndResultsFrame,text=GetMessage(),
                                            font="times 18",
                                            bg="gray87")
		#Place Labels
                TitleLabel.place(x=410,y=40,width=400,height=40)
                SubtitleLabel.place(x=410,y=115,width=400,height=40)
                ThanksMessageLabel.place(x=310,y=10,width=600,height=60)
                ResultTitleLabel.place(x=180,y=40,width=200,height=30)
                ResultLabel.place(x=100,y=90,width=400,height=25)
                ResultMessageLabel.place(x=75,y=160,width=460,height=25)

        #function to get the final user question        
        def GetMessage():
                if(CorrectCnt_tk>=6):
                        return RESULTMESSAGE1
                elif(CorrectCnt_tk>=4 and CorrectCnt_tk<6):
                        return RESULTMESSAGE2
                elif(CorrectCnt_tk>=2 and CorrectCnt_tk<4):
                        return RESULTMESSAGE3
                else:
                        return RESULTMESSAGE4

        #Function to show user the easter egg if they discover it        
        #Can be found on the bottom left of the ending screen as a small red box.
        def EasterEggFunction():
                #Open easter egg image from file
                EasterEggImage=Image.open(os.path.join("images","EasterEggImage.jpg"))
                
                #resize image size to fit
                EasterEggImage=EasterEggImage.resize((400,200),Image.ANTIALIAS)
                
                #convert into tkinter image type
                EasterEggImage = ImageTk.PhotoImage(EasterEggImage)

                #put image as label
                ImageLabel = tk.Label(EasterEggFrame, image=EasterEggImage)
                
                #Play EasterEgg sound effect if user chooses to have sound
                if(NoSound_tk==0):
                        pygame.mixer.music.load(os.path.join("sounds","EasterEggSoundEffect.mp3")) 
                        pygame.mixer.music.play()

                        #wait 3 seconds
                        time.sleep(3)

                        #play character in game voice line
                        pygame.mixer.music.load(os.path.join("sounds","MercyVoiceLine.mp3")) 
                        pygame.mixer.music.play()
                        
                #Place Image
                ImageLabel.place(x=100,y=0)

                #create character quote label
                CharacterQuoteLabel=tk.Label(EasterEggFrame,text="""Mercy: I'll be watching over you""",
                                             font="times 14",
                                             bg="gray87")

                #place label
                CharacterQuoteLabel.place(x=100,y=210,width=400,height=25)

                #allow image to appear on screen
                EndWindow.mainloop()

        #create the end window buttons                
        def CreateEndButtons():
                #Create Buttons
                CloseGameButton=tk.Button(EndButtonFrame, text="CLOSE GAME",
                                         fg="red",
                                         bg="gray70",
                                         font="times 30",
                                         command=CloseGameFunction)
                #The easter egg will be located in the bottom right corner of the window
                EasterEggButton=tk.Button(EndButtonFrame,
                                          bg="red",
                                          command=EasterEggFunction)
                #place buttons
                CloseGameButton.place(x=400,y=40,width=400,height=70)
                EasterEggButton.place(x=100,y=80,width=3,height=3)

        #Function close the game        
        def CloseGameFunction():
                #Play Button sound effect if user chose to have sound effects
                if(NoSound_tk==0):
                        pygame.mixer.music.load(os.path.join("sounds","ButtonSoundEffect.mp3")) 
                        pygame.mixer.music.play()
                        
                #destroy window
                EndWindow.destroy()


        ############################
        #End window main function
        #create end window, set minsize, title
        EndWindow=tk.Tk()
        EndWindow.minsize(width=1200,height=700)
        EndWindow.title("TriviaWatch - Jack Song")
        
        #create End window frames
        EndTitleFrame=tk.Frame(EndWindow,width=1200,height=200,bg="ivory2")
        EndMessageFrame=tk.Frame(EndWindow,width=1200,height=100,bg="gray87")
        EndResultsFrame=tk.Frame(EndWindow,width=600,height=250,bg="gray87")
        EasterEggFrame=tk.Frame(EndWindow,width=600,height=250,bg="gray87")
        EndButtonFrame=tk.Frame(EndWindow,width=1200,height=150,bg="ivory2")
        
        #place frames
        EndTitleFrame.place(x=0,y=0)
        EndMessageFrame.place(x=0,y=200)
        EndResultsFrame.place(x=0,y=300)
        EasterEggFrame.place(x=600,y=300)
        EndButtonFrame.place(x=0,y=550)

        #Initialize Constants
        RESULTMESSAGE1="You are a Pro Overwatch Player!"                
        RESULTMESSAGE2="You can become a Pro Overwatch Player!"        
        RESULTMESSAGE3="You should read more Overwatch Stories!"      
        RESULTMESSAGE4="You should spend more time in the Practice Range!"  

        #call needed functions
        CreateEndLabels()
        CreateEndButtons()

        #main loop
        EndWindow.mainloop()


#################################################################################################
#Main program
#pygame start commmand
pygame.init()

#call functions
CreateIntroWindowAndFunctions()


