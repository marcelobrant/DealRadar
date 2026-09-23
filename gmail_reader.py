import imaplib
import email

EMAIL = "dealradardeals@gmail.com"
APP_PASSWORD = "YOUR_APP_PASSWORD"  # Replace with your actual app password

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(EMAIL, APP_PASSWORD)

mail.select("INBOX")

status, messages = mail.search(None, "ALL")
email_ids = messages[0].split()

print("Total emails:", len(email_ids))
print("\n--- YOUR EMAILS ---")

# Look at the newest 9 emails
for email_id in email_ids[-9:]:
    status, data = mail.fetch(email_id, "(RFC822)")

    raw_email = data[0][1]
    msg = email.message_from_bytes(raw_email)

    print("\nFROM:", msg["From"])
    print("SUBJECT:", msg["Subject"])
    print("DATE:", msg["Date"])

mail.logout()
