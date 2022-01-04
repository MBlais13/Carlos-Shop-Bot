# SneakerBot made by MBlais (https://github.com/MBlais13)


# important variables
PageURL = 'https://www.nike.com/ca/launch/t/air-force-1-winter-premium-off-noir' # nike shoe page url
Size_Xpath = '/html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/div[2]/ul/li[5]' # you need to change this to the size of shoe you want.

# SneakerBot Options
AutoBuy = False # I wont be adding autobuy features. feel free to fork the code though. (maybe even create a pull request??)
AutoCart = False # nike's website doesn't have cart stock protection.
DiscordWebhooks = False # discord webhook to specified DiscordWebhookURL
WindowsToasts = False #(windows desktop notifications + sound)
TestMode = False

# notification variables
DiscordWebhookURL = 'url here'

# debug values
DebugMode = False


# gets the current date and time, you can format this any way you like.
from datetime import datetime, time
now = datetime.now()
current_time = now.strftime('%H:%M:%S')


### dont change these
SneakerBotVersion = '1.9c'


# have a lovely day - mblais