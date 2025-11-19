import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from models import Session, Recipient
from config import EMAIL_USER, EMAIL_PASSWORD
from datetime import datetime
import os

LOG_FILE = "logs/email_log.txt"

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Create logs folder if it does not exist
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    # Write log
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    # Print log to GitHub Actions UI
    print(message)

def send_emails():
    session = Session()
    recipients = session.query(Recipient).all()

    for r in recipients:
        try:
            msg = MIMEMultipart()
            msg['From'] = EMAIL_USER
            msg['To'] = r.email
            msg['Subject'] = "Email Automation System Project"
            body = f"Hi, this is Email Automation System project and done successfully.\n\nRegards,\nLakshmi Narayana Reddy"
            msg.attach(MIMEText(body, 'plain'))

            try:
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.login(EMAIL_USER, EMAIL_PASSWORD)
                server.send_message(msg)
                server.quit()

                r.status = "Sent"
                session.commit()
                log_message(f"Email sent successfully to {r.name} ({r.email})")

            except smtplib.SMTPAuthenticationError:
                r.status = "Failed"
                session.commit()
                log_message(f"SMTP Authentication failed for {r.name} ({r.email})")

            except smtplib.SMTPException as smtp_error:
                r.status = "Failed"
                session.commit()
                log_message(f"SMTP Error for {r.name} ({r.email}): {smtp_error}")

            except Exception as e:
                r.status = "Failed"
                session.commit()
                log_message(f"Failed to send email to {r.name} ({r.email}): {e}")

        except Exception as e_outer:
            log_message(f"Unexpected error for {r.name} ({r.email}): {e_outer}")

    session.close()
