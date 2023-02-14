from pyrogram import Client

api_id = 14576105
api_hash = 'a8e164ef42511799656592b2bf96d87d'
app_version="Android 8.7.4"
device_model="LM-Q720"
system_version="Android"

app = Client('Andre', api_id, api_hash, app_version, device_model, system_version)

with app:
    for member in app.get_chat_members(chat_id='ru_python_beginners'):
        print(member.user.username, ' -- id: ', member.user.id)
