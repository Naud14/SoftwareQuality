from database.database import prepare_database
from views.menus import main_menu

if __name__ == '__main__':
    prepare_database()
    main_menu()
