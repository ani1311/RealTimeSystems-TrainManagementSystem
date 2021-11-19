import train_utils 

connection = None 

if __name__ == "__main__":
    while True:
        ip = train_utils.displayMenuAndTakeInput()
        if(ip == 7):
            break
        train_utils.handleInput(ip)
