from json import dumps
from httplib2 import Http

def send_notif(env_build, message):
    spaces = 'https://chat.googleapis.com/v1/spaces/<spaces-name>/messages?key=<key>'
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()

    bot_message = {
        'text' : <message>
    }
    http_obj.request(
        uri=spaces,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message)
    )
