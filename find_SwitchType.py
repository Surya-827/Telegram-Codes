
class UserMainCode(object):
    @classmethod
    def findSwitchType(cls,s:str)->str:
        port_idx = s.find("P") - 2
        val = int(s[port_idx:port_idx + 2])
        stack_idx = s[s.find("X")]
        rev_str = s[::-1]
        port_val = rev_str[rev_str.find("X") + 1:rev_str.find("-")]

        type1 = [
            5200, 5250, 5270
        ]

        type2 = [
            5200, 5250, 5270, 5350, 5370, 5400
        ]

        if (val <= 24):
            for i in type1:
                if str(i) in s:
                    print(f"{val}\nType 1")

        if (val > 24):
            for i in type2:
                if str(i) in s:
                    print(f"{val}\nType 2")
        if ('X' not in s or 'L' not in s or 'P' not in s):
            print("Invalid model number")
        else:
            print("Core")
            
            
if "__name__"=="__main__":
    s = input()
    obj = UserMainCode()
    obj.findSwitchType(s)

