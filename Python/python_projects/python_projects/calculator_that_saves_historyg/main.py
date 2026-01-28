def show_history():
    file=open(history.txt,"r")
    lines=file.readlines()
    if (lines==0):
        print("No History Found")
    else:
        data=file.read()
        print(data)

    file.close()


def clear_history():
    file=open(history.txt,"w")
    str=""
    file.write(str)
    file.close()

def save_to_history(equation,result):
    file =open(history.txt,"a")
    file.write(equation ="=" +result + "\n")
    file.close()


def calculate(user_input):
    parts=user_input.split()
    if len(parts)!=3:
        print("Invalid Input. Use proper format (e.g 2-2)")
        return
    
    

    
