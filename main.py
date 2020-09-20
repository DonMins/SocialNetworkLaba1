import json
import vk
from telethon import TelegramClient
# ---------------------------- VK API ----------------------------------------------------------------------------------
def getApi():
    login = 'Какой-то логин' # Ваш login
    password = 'Какой-то пароль'  # Ваш password
    session = vk.AuthSession(app_id='000000', # Ваш app_id
                             user_login=login,
                             user_password=password,
                             scope=['offline', 'messages', 'friends', 'wall'])
    return vk.API(session, v='5.62')


"""
Публикует запись на вашей стене
"""
def postEntry(api):
    api.wall.post(message='Hello world!')


"""
Получает посты по id группы (81824379) и записывает в файл 
"""
def getPosts(api):
    wall = api.wall.get(owner_id=81824379)
    print('Posts count:', wall['count'])
    f = open(r" wall_asp.txt", 'a')
    f.write(json.dumps(wall))
    f.close()

# ----------------------------------------------------------------------------------------------------------------------


# ---------------------------- TELEGRAM API ----------------------------------------------------------------------------

def getApiTg():
    api_id = 0000000 # Ваш api_id
    api_hash = '000000000000000000000000'# api_hash
    client = TelegramClient('session_name1', api_id, api_hash)
    client.start()
    return  client

"""
Отправляет сообщение самому себе. Можно в качестве 
1 параметра передать имя пользователя , которому нужно отправить сообщение 
"""
def sendMessage(client):
    client.loop.run_until_complete(client.send_message('me', 'Hello to myself!'))

"""
Получаем информацию об одном из чатов пользователя , в данном случаем из чата "KANGAROO" с id = 432956342
Выводит кол - во участников и их имена
"""
def getGroupInfo(client):
    info = client.loop.run_until_complete(client.get_participants(432956342))
    print("Всего участников: " + str(len(info)))
    for dialog in info:
        first_name = "" if dialog.first_name == None else dialog.first_name
        last_name = "" if dialog.last_name == None else dialog.last_name
        print(first_name + " " + last_name)

"""
Получаем  список сообщений из часа по id , в данном случаеи их чата (KANGAROO с id = 432956342)
"""
def getMessages(client):
    with client:
        for message in client.iter_messages(432956342):
            print(message.sender_id, ':', message.text)


#-----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    api = getApi()
    postEntry(api)
    getPosts(api)

    client = getApiTg()
    sendMessage(client)
    getGroupInfo(client)
    getMessages(client)


