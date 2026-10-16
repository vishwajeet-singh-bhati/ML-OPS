class chatbook:
    def __init__(self):
        self.username=''
        self.password = ''
        self.loggedin = False
        self.menu()


    def menu(self):
        user_input = input("""welcome to chatbook !! how would u like to proceed?
                            1. press 1 to signup
                            2. press 2 to signin
                            3. press 3  to write a post
                            4. press 4 to message a friend
                            5. press any other key to exit 
                             """)
        if user_input == "1": 
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input=="3":
            self.my_post()
        elif user_input=="4":
            self.sendmsg()
        else:
            exit()


    def signup(self):
        email=input("enter your email ->")
        pwd = input("enter your password ->")
        self.username=email
        self.password=pwd
        print("you have signed up successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("please signup first by pressing 1 in the main menu")
        else:
            uname=input("enter email ->") 
            pwd= input("enter pwd->")
            if self.username==uname and self.password==pwd:
                print("sign in successfull")
                self.loggedin=True
            else:
                print("wrong username or password")
        
        self.menu()


    def my_post(self):
        if(self.loggedin==True):
            txt=input("enter your message here")
            print(f"following content has been posted->{txt}")
        else :
            (print("you need to signin first to post something"))
        self.menu()
    def sendmsg(self):
        if self.loggedin == True:
            txt=input("enter ur msg here->")
            frnd = input("enter friend name")
            print(f"your msg {txt} has been sent to {frnd}")
        else:
            print("please signin first")
        self.menu()

        
    
obj=chatbook()

