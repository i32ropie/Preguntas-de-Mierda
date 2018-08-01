import telebot
from telebot import types
import json
import random

bot = telebot.TeleBot('token')

with open('preguntas.json') as f: preguntas = json.load(f)

@bot.message_handler(commands = ['start', 'ayuda', 'help'])
def reglas_handler(m):
    cid = m.chat.id
    mensaje = "Bienvenido al bot, para empezar a jugar haz click en /jugar y recibirás una carta aleatoria que tendrá 6 preguntas, cada una de una categoría distinta. Las categorías son:\n- *VC*: Vida cotidiana\n- *I*: Imaginario\n- *S*: Sexo\n- *C*: Cultura\n- *G*: Gore\n- *FP*: Filosofía y Progreso.\n\nLas reglas para jugar puedes inventártelas pero unas básicas serían que uno de los jugadores 'sacara' una carta e hiciera la pregunta que quiera de las que le han salido, entonces todos los presentes responden y la persona que sacó la carta decide qué respuesta es la que más le ha gustado y las demás personas beben un trago.\n\nLo importante es pasarlo bien, a si que juega como te de la gana.\n\nBot desarrollado por @Edurolp"
    bot.send_message(cid, mensaje, parse_mode = "Markdown")

@bot.message_handler(commands = ['jugar'])
def jugar_handler(m):
    cid = m.chat.id
    p = random.choice(preguntas)
    teclado = types.InlineKeyboardMarkup()
    teclado.add(types.InlineKeyboardButton("Sacar otra carta", callback_data="carta"))
    mensaje = "Estas son tus preguntas:\n\n- *VC* - _{}_\n- *I*: _{}_\n- *S*: _{}_\n- *C*: _{}_\n- *G*: _{}_\n- *FP*: _{}_\n\nHaz click en *'Sacar otra carta'* para que el siguiente jugador vea nuevas preguntas."
    bot.send_message(cid, mensaje.format(p['vida_cotidiana'],
                                         p['imaginario'],
                                         p['sexo'],
                                         p['cultura'],
                                         p['gore'],
                                         p['filosofia_progreso']), reply_markup = teclado, parse_mode = "Markdown")

@bot.callback_query_handler(func = lambda call: call.data == "carta")
def carta_hander(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    p = random.choice(preguntas)
    teclado = types.InlineKeyboardMarkup()
    teclado.add(types.InlineKeyboardButton("Sacar otra carta", callback_data="carta"))
    mensaje = "Estas son tus preguntas:\n\n- *VC* - _{}_\n- *I*: _{}_\n- *S*: _{}_\n- *C*: _{}_\n- *G*: _{}_\n- *FP*: _{}_\n\nHaz click en *'Sacar otra carta'* para que el siguiente jugador vea nuevas preguntas."
    bot.edit_message_text(mensaje.format(p['vida_cotidiana'],
                                             p['imaginario'],
                                             p['sexo'],
                                             p['cultura'],
                                             p['gore'],
                                             p['filosofia_progreso']), cid, mid, reply_markup = teclado, parse_mode = "Markdown")

bot.polling()