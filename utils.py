from datetime import datetime

def calculate_fine(borrow_date_str, return_date_str, free_days=7, fine_per_day=10):
    borrow_date = datetime.strptime(borrow_date_str, "%Y-%m-%d")
    return_date = datetime.strptime(return_date_str, "%Y-%m-%d")
    days = (return_date - borrow_date).days
    if days > free_days:
        return (days - free_days) * fine_per_day
    return 0
