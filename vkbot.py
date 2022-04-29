import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random


def main():
    vk_session = vk_api.VkApi(
        token='e8f15d1c188db9059042347dc6b3e209db66735727cf8aea40d2272eff2a4e23ba764c3e9e590e39c2ff2')

    longpoll = VkBotLongPoll(vk_session, '212703029')
    print('sdfsdf')
    for event in longpoll.listen():
        print('sdfsdf')
        print(event)
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])
            vk = vk_session.get_api()
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Спасибо, что написали нам. Мы обязательно ответим",
                             random_id=random.randint(0, 2 ** 64))
        if event.type == VkBotEventType.MESSAGE_TYPING_STATE:
            print(f'Печатает {event.obj.from_id} для {event.obj.to_id}')
        if event.type == VkBotEventType.GROUP_JOIN:
            print(f'{event.obj.user_id} вступил в группу!')
    print('sdfsdf')


if __name__ == '__main__':
    main()