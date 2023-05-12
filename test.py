    def __init__(self, parent, App):
        self.settings = App.settings
        self.app = App

        super().__init__(parent)
        self.configure(bg="white")
        self.pack(fill="both", expand=True)

        self.pixelButton = tk.PhotoImage(width=1, height=1)
        self.email_pemb = tk.StringVar()
        self.mainframe()
        self.FrameUp()
        self.FrameLeft()



    def mainframe(self):
        self.Feedback = tk.Frame(self,bg='purple',width=self.settings.width,height = self.settings.height)
        self.Feedback.grid(row=0,column=0,sticky='nsew')
        self.Feedback.pack_propagate(False)

    def FrameUp(self):
        FrameUp = tk.Frame(self.Feedback, bg='gray',width=self.settings.width,height=(self.settings.height//5))
        FrameUp.pack(fill='both')
        tk.Label(FrameUp , text ='APLIKASI PERGUDANGAN \n  by: Ethan Bast , Kenzie',font=('arial',20),bg='gray',fg='white').pack(side='right')
        tk.Button(FrameUp , text=' <- Back to main menu ', command = self.app.Feedback_back_to_main).pack(side='left')

    def FrameLeft(self):
        FrameDown = tk.Frame(self.Feedback, bg='black',width=self.settings.width ,height=self.settings.height)
        FrameDown.pack(side='left')
        FrameDown.pack_propagate(False)
