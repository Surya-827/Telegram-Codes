

class UserProfile(object):
    @classmethod
    def greet(cls,name:str) -> str:
        return f"Hello! {name},Welcome Back to Code..."


if __name__=="__main__":
    x = input("Enter User Name : ")
    obj = UserProfile()
    print(obj.greet(x))