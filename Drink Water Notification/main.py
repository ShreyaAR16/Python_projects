import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Time to Drink Water!!",
            message = "Drinking water has many benefits.These include lubricating joints, regulating body temperature by aiding sweating, assisting indigestion, flushing out waste, supporting open airways, and aiding weight loss.",
            app_icon = "icon.ico",
            timeout = 10
        )
        time.sleep(60*60)