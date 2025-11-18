from apscheduler.schedulers.blocking import BlockingScheduler
from send_email import send_emails
from datetime import datetime

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def job():
    log_message("Scheduler triggered")
    send_emails()

if __name__ == "__main__":
    scheduler = BlockingScheduler()

    # scheduler.add_job(job, 'cron', hour=00, minute=44)
    # scheduler.add_job(job, 'cron', hour=23, minute=52)


    scheduler.add_job(job, 'cron', day=1, hour=9, minute=0)

    log_message("Scheduler started. Waiting for jobs...")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        log_message("Scheduler stopped.")