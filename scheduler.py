from send_email import send_emails
from datetime import datetime

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

if __name__ == "__main__":
    log_message("Scheduler triggered by GitHub Actions")
    send_emails()
    log_message("Email sending completed")
