

class UserProfile(object):
    @classmethod
    def greet(cls,name:str) -> str:
        return f"Hello! {name},Welcome Back to Code..."

    @classmethod
    def ConcatNames(cls,lname:str,fname:str) -> str:
        return "Your Full Name is  : "+fname+" "+lname


if __name__=="__main__":
    #x = input("Enter User Name : ")
    obj = UserProfile()
    #print(obj.greet("Surya"))
    print(obj.ConcatNames("Kiran","Surya"))