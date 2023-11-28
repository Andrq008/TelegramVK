from pyrogram import Client

api_id = 1...
api_hash = ''
app_version="Android 8.7.4"
device_model="LM-Q720"
system_version="Android"

app = Client('Andre', api_id, api_hash, app_version, device_model, system_version)

with app:
    for member in app.get_chat_members(chat_id='ru_python_beginners'):
        print(member.user.username, ' -- id: ', member.user.id)
