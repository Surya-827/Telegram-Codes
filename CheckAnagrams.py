def check_anagram():

    str1=input("enter the 1st string: ")

    str2=input("enter the 2nd string: ")

    if sorted(str1)==sorted(str2):

        return "Yes"

    else:

        return "No"
