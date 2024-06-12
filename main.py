from database.database import prepare_database
from database.database import send_query, get_connection
from database.auth import add_user
from views.menus import main_menu

if __name__ == '__main__':
    prepare_database()
    add_user("super_admin", "Admin_123?", "super_admin", "Jonna", "Jimmy")
    main_menu()
