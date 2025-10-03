import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

upassBotWebhookUrl = os.getenv("GENERAL_WEBHOOK")
monthBotWebhookUrl = os.getenv("MONTH_ALREADY_REQUESTED")
authenticateBot    = os.getenv('NO_NEED_TO_AUTHENTICATE')

upassAuthNotRequiredMessage = (f"<@{os.getenv('DISCORD_USER_ID')}>, there is no need to do your auth")

def upass_auth_request_message(authNum):
    if not upassBotWebhookUrl:
        print("Error: GENERAL_WEBHOOK not found in environment variables")
        return
        
    isNum = True
    try:
        int(authNum)
    except:
        isNum = False

    if (isNum == False):
        print("Trolling Program")

    upassAuthRequestMessage     = f"Hello {os.getenv('FULL_NAME')} Please authentVicate Request Auth Num is {authNum}"    
    try:
        response = requests.post(upassBotWebhookUrl, data = {"content": upassAuthRequestMessage})
        if response.status_code == 204:
            print("Discord notification sent successfully")
        else:
            print(f"Failed to send Discord notification: {response.status_code}")
    except Exception as e:
        print(f"Error sending Discord notification: {e}")

def monthAlreadyRequested():
    if not monthBotWebhookUrl:
        print("Error: MONTH_ALREADY_REQUESTED not found in environment variables")
        return
        
    currentMonth = datetime.now().strftime("%B")
    monthRequestedMessage = f"Sorry {os.getenv('FULL_NAME')}, {currentMonth} has already been requested"
    
    try:
        response = requests.post(monthBotWebhookUrl, data = {"content": monthRequestedMessage})
        if response.status_code == 204:
            print("Month already requested notification sent successfully")
        else:
            print(f"Failed to send month notification: {response.status_code}")
    except Exception as e:
        print(f"Error sending month notification: {e}")

## This function sends a message via up
def noAuthRequired():
    if not authenticateBot:
        print("Can not find upass bot webhook URL")
    try:
        response = requests.post(authenticateBot, data = {"content": upassAuthNotRequiredMessage})
        if response.status_code == 204:
            print(f" No auth required Message Sent on Discord")
    except Exception as e:
        print(f"Error sending message Through discord")