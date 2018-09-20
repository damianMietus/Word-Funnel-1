# Damian Mietus
# Reddit Daily Programmer
# Challenge #366 [Easy] Word Funnel 1
# Completed September 20 2018

#Function that iterates to find where the stings no longer match, removes the
#character, and returns true or false if it is a valid word funnel
def funnel(arg1, arg2):
    if len(arg2) > len(arg1):
        return False
    else:
        i = 0
        while (i < len(arg1) - 1):
            if arg1[i] != arg2[i]:
                newArg1 = arg1[:i] + arg1[i+1:]
                if (newArg1 == arg2):
                    return True
                    break;
                else:
                    return False
                    break;
            i = i+1
#The main
if funnel("dragoon", "dragon") == True:
    print("true")
else:
    print("false")
