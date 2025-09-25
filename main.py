import database
from ui import login

def main():
    database.init_db()
    login.login_window()

if __name__ == "__main__":
    main()
