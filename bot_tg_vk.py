from pyrogram import Client
import vk_api

api_id = 1..
api_hash = ''
bot_token = ''
app_version="Android 8.7.4"
device_model="LM-Q720"
system_version="Android"

vk_session = vk_api.VkApi('itnt_andre@mail.ru', '_13508gotQW')
vk_session.auth()
vk = vk_session.get_api()
print(vk.wall.post(message='Hello world!'))

app = Client('bot', api_id, api_hash, bot_token)

app.start()
# app.send_message(-1001794193522, 'Hello TEST')
app.send_message('me', 'Hello TEST')
app.stop()

# app.run()
