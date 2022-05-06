import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title = "Stop Working",
            message = "Take short breaks often, rather than longer ones less often. For example 5 to 10 minutes every hour is better than 20 minutes every 2 hours.",
            app_icon = "F:\Python\Desktop Notifier\icon.ico",
            timeout = 10
        )
        time.sleep(60*60)