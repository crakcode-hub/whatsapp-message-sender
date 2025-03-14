import webbrowser
import pyautogui
import time
import urllib.parse
import json

with open("contact-details.json", "r", encoding="utf-8") as file:
    data = json.load(file)

def send_whatsapp_message(phone_number, message):
    # Format the WhatsApp API URL with URL-encoded message
    encoded_message = urllib.parse.quote(message)
    whatsapp_url = f"https://api.whatsapp.com/send/?phone={phone_number}&text={encoded_message}&type=phone_number&app_absent=0"
    
    # Open URL in default browser
    webbrowser.open(whatsapp_url)
    time.sleep(3)  # Increased wait time for browser to open
    
    # Click on "Continue to Chat" or message button
    pyautogui.press('enter')
    time.sleep(3)  # Increased wait time
    
    # Click on "use WhatsApp Web"
    pyautogui.press('enter')
    time.sleep(3)  # Increased wait time
    
    # Send message
    pyautogui.press('enter')
    time.sleep(3)

def main():
    # List of numbers (remove any '+' or spaces from numbers)
 
    
    messageStarting = data["messages"]["start"]
    messageEnd = data["messages"]["end"]
    
    # Send message to each contact
    for contact in data["contacts"]:
        try:
            # Access name and phone as dictionary keys
            full_message = messageStarting + contact['name'] + messageEnd
            send_whatsapp_message(contact['phone'], full_message)
            print(f"Message sent to {contact['name']}")
            time.sleep(3)  # Increased wait time between messages
        except Exception as e:
            print(f"Error sending message to {contact['name']}: {str(e)}")

if __name__ == "__main__":
    main()