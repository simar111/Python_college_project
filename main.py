# main.py

import database
from ui.login import login_window   # directly import login screen

def main():
    # Initialize database tables & default admin
    database.init_db()

    # Launch login screen
    login_window()

if __name__ == "__main__":
    main()
