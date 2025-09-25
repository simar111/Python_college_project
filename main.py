import database
import ui

def main():
    database.init_db()  # Setup DB
    ui.launch_ui()      # Start GUI

if __name__ == "__main__":
    main()
