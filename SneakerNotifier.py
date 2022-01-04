# -selenium webdriver-
from logging import fatal
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

# config file import
import config
import requests # for discord webhook

# makes the bot only use the specified cores. (logical processors)
#import psutil
#p = psutil.Process()
# p.cpu_affinity([2,3,5,6,7,9,10,11,12,13,14])

# get the webdriver you want to use.
browser = webdriver.Firefox(executable_path=r'.\webdrivers\geckodriver.exe')
browser.get(config.PageURL)
#wait = WebDriverWait(browser, 2)
print('waiting')
element = WebDriverWait(browser, 20).until(lambda x: x.find_element_by_xpath(config.Size_Xpath))  # waits for page to finish loading
print('finished waiting')

# timestamp of when the bot was started
print('Time started =', config.current_time)
print('--------------------------------------')
SizeAvailable = browser.find_element_by_xpath(config.Size_Xpath).get_attribute('data-qa')
ShoeNamePrimary = browser.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div[1]/div[2]/div/section[1]/div[2]/aside/div/div[1]/h1').get_attribute('innerHTML')
ShoeNameSecondary = browser.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div[1]/div[2]/div/section[1]/div[2]/aside/div/div[1]/h5').get_attribute('innerHTML')
ShoeThumbnail = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[1]/div[2]/div/section[1]/div[1]/div/div[6]/figure/img').get_attribute('src')
#all_children_by_xpath = browser.find_elements_by_xpath(f'{config.Size_Xpath}.//*')
#print(all_children_by_xpath)

parentElement = browser.find_element_by_xpath(config.Size_Xpath)
elementList = parentElement.find_elements_by_tag_name('button')

print('===============')
print(parentElement)
print(elementList)
print('===============')


print(ShoeNamePrimary)
print(ShoeNameSecondary)
print(SizeAvailable)
# ~~ debug ~~
if config.DebugMode == True:
    print('debug value is true.')
    print('~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'*Debug Info*\nAutoBuy = {config.AutoBuy}\nAutoCart = {config.AutoCart}\nWinToast = {config.WindowsToasts}\nTestMode = {config.TestMode}')
    print('--------------------------------------')

# check if {InStockColor} is the same as the {SizeBgColor}
if SizeAvailable == 'size-unavailable':  # size is unavailable
    print('out of stock')
    # browser.refresh()
    
elif SizeAvailable != 'size-unavailable':  # size is available
    print('in stock')
    # notification settings (you can change them in the config)
    if config.WindowsToasts == True:
        from logging import debug
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast(f'Sneaker Bot v{config.SneakerBotVersion}',
                           (f'{ShoeNamePrimary} are in stock'),
                           icon_path='assets\\sneakerbot-icon.ico',
                           duration=999999,
                           threaded=True)

    if config.DiscordWebhooks == True:
        url = config.DiscordWebhookURL

        if config.DebugMode == True:
            embed = {
            'title': 'Sneakers in stock!',
            'color': 15052624, # 15052624 orange, 14708343 bright red, 12017246 darker red
            'thumbnail': {
                'url': ShoeThumbnail
            },
            'fields': [
                {
                'name': (f'{ShoeNamePrimary} - {ShoeNameSecondary}'),
                'value': (f'[store link]({config.PageURL})\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n```▬ Debug Info ▬\nAutoBuy = {config.AutoBuy}\nAutoCart = {config.AutoCart}\nDiscordHook = {config.DiscordWebhooks}\nWinToast = {config.WindowsToasts}\nTestMode = {config.TestMode}\n```')
                }
            ],
            'footer': {
                'text': (f'Made by MBlais.dev • {config.current_time} • SneakerBot v{config.SneakerBotVersion}'),
                'icon_url': 'https://i.imgur.com/MbrG9HM.png'
            }
            
            }
        elif config.DebugMode == False:
            embed = {
                'title': 'Sneakers in stock!',
                'color': 5546086, # dark green:5546086, light green:8776060
                'thumbnail': {
                    'url': ShoeThumbnail
                },
                'fields': [
                    {
                    'name': (f'{ShoeNamePrimary} - {ShoeNameSecondary}'),
                    'value': (f'[store link]({config.PageURL})\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
                    }
                ],
                'footer': {
                    'text': (f'Made by MBlais.dev • {config.current_time} • SneakerBot v{config.SneakerBotVersion}'),
                    'icon_url': 'https://i.imgur.com/MbrG9HM.png'
                }
                
                }

        data = {
            'username': (f'SneakerBot v{config.SneakerBotVersion}'),
            'avatar_url': 'https://i.imgur.com/eVDSFTr.png',
            'embeds': [
                embed
                ],
        }

        headers = {
            'Content-Type': 'application/json'
        }

        result = requests.post(url, json=data, headers=headers)
        if 200 <= result.status_code < 300:
            print(f'Webhook sent {result.status_code}')
        else:
            print(f'Not sent with {result.status_code}, response:\n{result.json()}')