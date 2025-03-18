import pywhatkit
import os

phone_number = os.environ.get("PHONE_NUMBER")
message = "Hi 👋 from GitHub Actions and pywhatkit!"

pywhatkit.sendwhatmsg_instantly(
    phone_no=phone_number,  # replace with actual phone number "+919xxxxxxxxx"
    message=message,
    wait_time=10,  # seconds before sending after browser opens
    tab_close=True  # close tab after sending
)

print(f"WhatsApp message sent successfully to {phone_number}!")
