from config.apiKey import ACCESS_TOKEN, ID_CHAT
from tkinter import messagebox
from telebot import TeleBot
from telebot import types
from io import BytesIO
from PIL import Image
import subprocess
import webbrowser
import pyautogui
import requests
import psutil

bot = TeleBot(ACCESS_TOKEN, parse_mode=None)

waiting_for_url = {}
waiting_for_text = {}
waiting_for_program_name = {}

@bot.message_handler(["help","start"])
def SendMessage(message):
    text = "My Device Is On 🟢"
    markup = types.InlineKeyboardMarkup()
    screenshot = markup.add(types.InlineKeyboardButton("Screenshot 🖥",callback_data="screenshot"))
    tasklist   = markup.add(types.InlineKeyboardButton("Tasklist 📱",callback_data="tasklist"))
    showInbox  = markup.add(types.InlineKeyboardButton("Show Text 📦",callback_data="showinbox"))
    url        = markup.add(types.InlineKeyboardButton("Open Url 〽️",callback_data="url"))
    killApp    = markup.add(types.InlineKeyboardButton("End Application 👏",callback_data="killapp"))
    shutdown   = markup.add(types.InlineKeyboardButton("Shutdown 🚀",callback_data="shutdown"))
    restart    = markup.add(types.InlineKeyboardButton("Restart 🛑",callback_data="restart"))
    bot.send_message(message.chat.id,text=text,reply_markup=markup)
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.data == "screenshot":
        screenshot = pyautogui.screenshot()
        image_stream = BytesIO()
        screenshot.save(image_stream, format='PNG')
        image_stream.seek(0)

        # Gửi ảnh qua Telegram
        bot.send_photo(call.message.chat.id, image_stream, caption="Here's Screenshot !")
    elif call.data == "tasklist":
        running_apps = {proc.info['name'] for proc in psutil.process_iter(['pid', 'name'])}
        if running_apps:
            bot.send_message(call.message.chat.id, str('\n'.join(running_apps)))
        else:
            bot.send_message(call.message.chat.id, "Không có ứng dụng nào đang chạy.")
    elif call.data == "showinbox":
        bot.reply_to(call.message, "Nhập thông báo :")
        waiting_for_text[call.message.chat.id] = "Inbox"
    elif call.data == "url":
        bot.reply_to(call.message, "Nhập URL :")
        waiting_for_url[call.message.chat.id] = True
    elif call.data == "killapp":
        bot.reply_to(call.message, "Nhập tên chương trình để kết thúc : ")
        waiting_for_program_name[call.message.chat.id] = "KillApp"
    elif call.data == "shutdown":
        import os
        os.system("shutdown /s")
        bot.send_message(call.chat.message.id,"Shutdown thành công!")
    elif call.data == "restart":
        import os
        os.system("shutdown /r")
        bot.send_message(call.chat.message.id,"Shutdown thành công!")
    else:pass
@bot.message_handler(func=lambda message: waiting_for_url.get(message.chat.id, False))
def open_url(message):
    try:
        url = message.text
        webbrowser.open(url)
        bot.send_message(message.chat.id, f"Đã mở URL: {url}")
        waiting_for_url[message.chat.id] = False  # Đặt trạng thái chờ URL về False
    except Exception as e:
        bot.send_message(message.chat.id, f"Có lỗi xảy ra khi mở URL.")
@bot.message_handler(func=lambda message: waiting_for_text.get(message.chat.id) == "Inbox")
def show_inbox(message):
    messagebox.showinfo("Thông báo", message.text)
    waiting_for_text[message.chat.id] = None
@bot.message_handler(func=lambda message: waiting_for_program_name.get(message.chat.id) == "KillApp")
def end_application(message):
    try:
        program_name = message.text
        for proc in psutil.process_iter(['pid', 'name']):
            if program_name.lower() in proc.info['name'].lower():
                psutil.Process(proc.info['pid']).terminate()
                bot.send_message(message.chat.id, f"Đã kết thúc chương trình: {proc.info['name']}")
                break
        else:
            bot.send_message(message.chat.id, f"Không tìm thấy chương trình có tên: {program_name}")
        waiting_for_program_name[message.chat.id] = None
    except Exception as e:
        bot.send_message(message.chat.id, f"Có lỗi xảy ra khi kết thúc chương trình.")
if __name__ == "__main__":
    bot.infinity_polling()
