from models import Usuario
import view

def showAll():
    print 'MVC - Inicio2'
    #gets list of all Usuario objects
    people_in_db = Usuario.getAll()
    #calls view
    return view.showAllView(people_in_db)

def start():
    print 'MVC - Inicio3'
    view.startView()
    input = raw_input()
    if input == 'y':
        return showAll()
    else:
        return view.endView()

if __name__ == "__main__":
    #running controller function
     print 'MVC - Inicio'
    start()