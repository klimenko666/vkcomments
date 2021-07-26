import vk_api, time, os, sys
from colorama import init, Fore
from time import sleep
from python_json_config import ConfigBuilder
init()

builder = ConfigBuilder()
config = builder.parse_config('config.json')

a = 1
banner = ("""
───╔╗────────────────────╔╗────────╔═╗╔═╗
───║║───────────────────╔╝╚╗───────║╔╝║╔╝
╔╗╔╣║╔╗╔══╦══╦╗╔╦╗╔╦══╦═╬╗╔╬══╗╔══╦╝╚╦╝╚╗
║╚╝║╚╝╝║╔═╣╔╗║╚╝║╚╝║║═╣╔╗╣║║══╣║╔╗╠╗╔╩╗╔╝
╚╗╔╣╔╗╗║╚═╣╚╝║║║║║║║║═╣║║║╚╬══║║╚╝║║║─║║
─╚╝╚╝╚╝╚══╩══╩╩╩╩╩╩╩══╩╝╚╩═╩══╝╚══╝╚╝─╚╝
Author: Klimenko&Ofkotov\n""")
token = config.token
rts = config.owner_id
post = config.post_id
message = config.message
attachments = config.attachments
sticker_id = config.sticker_id

vk = vk_api.VkApi(token=token)
vk._auth_token()

def vibor():
    os.system('cls||clear')
    print(Fore.MAGENTA + banner + Fore.RESET + 'Выберите функцию:')
    print('[1] обычная накрутка')
    print('[2] накрутка вложениями(attachments)')
    print('[3] накрутка стикерами')
    v = input(">>> ")
    if v == "1":
        vkcomm()
    elif v == "2":
        attach()
    elif v == "3":
        stik()
    else:
        print('Выбрана не верная функция')
        sleep(2)
        vibor()


def vkcomm():
    global a
    while True:
        try:
            response = vk.method("wall.createComment", {"owner_id": rts, "post_id": post, "message": message})
            os.system('cls||clear')
            print(Fore.MAGENTA + banner)
            print(Fore.GREEN + f'Оставлен комментарий с текстом "{message}" #' + str(a))
            a += 1
            sleep(5)
        except vk_api.exceptions.Captcha:
            os.system('cls||clear')
            print(Fore.RED + banner)
            print(f'Ошибка! Небходимо решить капчу\nЗадержка 30 сек.\n[Err!]#' + str(a))
            a += 1
            sleep(30)
        except vk_api.exceptions.ApiError:
            os.system('cls||clear')
            print(Fore.RED + banner)
            print(f'Ошибка! Токен не валиден или введен не верно\n[Err!]#' + str(a))
            a += 1
            sleep(30)

def attach():
    global a
    while True:
        try:
            response = vk.method("wall.createComment", {"owner_id": rts, "post_id": post, "message": message, "attachments": attachments})
            os.system('cls||clear')
            print(Fore.MAGENTA + banner)
            print(Fore.GREEN + f'Оставлен комментарий с текстом "{message}" #' + str(a))
            a += 1
            sleep(5)
        except vk_api.exceptions.Captcha:
            os.system('cls||clear')
            print(Fore.RED + banner)
            print(f'Ошибка! Небходимо решить капчу\nЗадержка 30 сек.\n[Err!]#' + str(a))
            a += 1
            sleep(30)
        except vk_api.exceptions.ApiError:
            os.system('cls||clear')
            print(Fore.RED + banner)
            print(f'Ошибка! Токен не валиден или введен не верно\n[Err!]#' + str(a))
            a += 1
            sleep(30)


def stik():
    global a
    while True:
        try:
            response = vk.method("wall.createComment", {"owner_id": rts, "post_id": post, "sticker_id": sticker_id})
            os.system('cls||clear')
            print(Fore.MAGENTA + banner)
            print(Fore.GREEN + f'Оставлен стикер с айди: {sticker_id} #' + str(a))
            a += 1
            sleep(5)
        except vk_api.exceptions.Captcha:
            os.system('cls||clear')
            print(Fore.RED + banner)
            print(f'Ошибка! Небходимо решить капчу\nЗадержка 30 сек.\n[Err!]#' + str(a))
            a += 1
            sleep(30)
        except vk_api.exceptions.ApiError:
            os.system('cls||clear')
            print(Fore.RED + banner)
            print(f'Ошибка! Токен не валиден или введен не верно\n[Err!]#' + str(a))
            a += 1
            sleep(30)


vibor()
