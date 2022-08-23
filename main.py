import imaplib
import email
from usernamepasswords import *

imap_server = "imap.gmail.com"
email_address = email
password = password # Two Factor Authentication is required for GMAIL

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password)

def __main__():
    imap.select("Inbox")
    _, msgnums = imap.search(None, '(FROM "Ubereats")')

    for msgnum in msgnums[0].split():
        _, data = imap.fetch(msgnum, "(RFC822)")

        message = email.message_from_bytes(data[0][1])

        print("\n---------------------------------------------------------")
        print(f"Message Number: {msgnum}")
        print(f"From: {message.get('From')}")
        print(f"To: {message.get('To')}")
        print(f"BCC: {message.get('BCC')}")
        print(f"Date: {message.get('Date')}")
        print(f"Subject: {message.get('Subject')}")
        print("Content:")
        for part in message.walk():
            if part.get_content_type() == "text/plain":
                print(part.as_string())
        print("---------------------------------------------------------\n")

    imap.close()

__main__()