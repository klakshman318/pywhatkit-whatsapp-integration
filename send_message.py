import pywhatkit

message = "Hi 👋 from GitHub Actions and pywhatkit!"

pywhatkit.sendwhatmsg_instantly(
    phone_no="+919XXXXXXXXX",  # replace with actual phone number
    message=message,
    wait_time=10,  # seconds before sending after browser opens
    tab_close=True  # close tab after sending
)

print("WhatsApp message sent successfully!")
