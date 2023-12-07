import eel

@eel.expose
def strAdd(str):      
    str = str + " Return."     
    return f'{str}'

@eel.expose
def app_start():   
    eel.init('web') #
    eel.start('login.html',size = (800,600))

if __name__ ==  '__main__':
    app_start()