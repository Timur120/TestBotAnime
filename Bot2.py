import telebot
import codecs


from telebot.types import Message

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('По алфавиту', 'По рейтингу')


bot = telebot.TeleBot('1428981663:AAFNNDORhKGkkiFb_umQB4JZfyEvt5HIibg')
Users = set()

@bot.message_handler(commands=['start'])
def command_hendler(message:Message):
    bot.send_message(message.chat.id, 'Для просмотра команд напишите /help')


@bot.message_handler(commands=['showlist'])
def start_message(message):
    bot.send_message(message.chat.id, 'Выберите, как вам удобно просматривать список', reply_markup=keyboard1)

@bot.message_handler(commands=['help'])
def command_hendler(message: Message):
    print (message.message_id,message.from_user.id, message.from_user.first_name,message.text)
    bot.send_message(message.chat.id, '1) /search+Название - найти аниме. Например:\n/search Наруто. \n\n2) /add+Название+Рейтинг - добавить аниме. Например:\n/add Наруто 10. \n\n3) /showlist - посмотреть список аниме.')

@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_gigits(message: Message):
    print (message.message_id,message.from_user.id, message.from_user.first_name,message.text)
    k=message.text
    c=''
    n=''
    a=''
    q=''
    s=0
    y=0
    r=0
    w=0
    e=0
    for g in k:
        y = y+1
    x=y
    d = y-2
    if k[d:y] == '10':
        y = y-3
        o = k[5:y]
    else:
        y= y-2
        o = k[5:y]
    if  message.from_user.first_name == 'Даня':
        bot.send_message(message.chat.id, 'Пидорам не отвечаю')
    elif k[0:8] == '/search ':
        with codecs.open ('loh.txt',encoding='utf-8', errors='ignore') as file:
            for i in file:
                if k[8:x] in i:
                    a = i
                    break
                else:
                    a = 'Такого аниме в списке нет'
        bot.send_message(message.chat.id, a)
        file.close()
    elif k[0:5] == '/add ' :

        with codecs.open ('loh.txt','r+',encoding='utf-8', errors='ignore') as file:
            for i in file:
                if o in i:
                    n = i
                    w=0
                    for j in n:
                        w = w+1
                    p = w
                    s=w-4
                    if n[s:w] =='10\n':
                        w=w-4
                        a= n[0:w]
                    else:
                        w = w-3
                        a = n[0:w]
                    if n[s:p] == '10/n':
                        p = p-1
                        m = int(n[s:p])
                    else:
                        s = s+1
                        p = p-1
                        m= int(n[s:p])
                    if k[d:x] == '10':
                        r = int(k[d:x])
                    else:
                        d = d+1
                        r= int(k[d:x])
                    q = str(int((r+m)/2))
                    e = 2
                    break
            if e == 0:
                file.write(k[5:x]+'\n')
        file.close()

        with codecs.open ('loh.txt','r',encoding='utf-8', errors='ignore') as file:
            lines = file.readlines()
        file.close()

        with codecs.open ('loh.txt','w',encoding='utf-8', errors='ignore') as file:
            for i in lines:
                if i != n:
                    file.write(i)
            file.write(a +' '+ q + '\n')
        file.close()
        bot.send_message(message.chat.id,'Спасибо,' + ' ' + a + 'добавлен в список')

    elif k == 'По алфавиту':
        a=''
        q=0
        w=0
        with codecs.open ('loh.txt',encoding='utf-8', errors='ignore') as file:
            for i in file:
                q += 1
        file.close()

        q = int(q/2)

        with codecs.open ('loh.txt',encoding='utf-8', errors='ignore') as file:
            for i in sorted(file):
                a = a + i
        file.close()

        for b in a:
            w += 1

        with codecs.open ('loh.txt','w',encoding='utf-8', errors='ignore') as file:
            file.write(a[q:w])
        file.close()

        with codecs.open ('loh.txt',encoding='utf-8', errors='ignore') as file:
            lines=file.readlines()
        file.close()

        with codecs.open ('loh.txt','w',encoding='utf-8', errors='ignore') as file:
            for i in lines:
                file.write(i + '\n')
        file.close()
        with codecs.open ('loh.txt',encoding='utf-8', errors='ignore') as file:
            c += file.read()
        file.close()
        bot.send_message (message.chat.id, c)

    elif k =='По рейтингу':
        n=''
        q=0
        s=0
        a=''
        lines=''
        w=0
        r =''
        o=''
        with codecs.open ('loh.txt','r+',encoding='utf-8', errors='ignore') as file:
            for i in file:
                q = 0
                n = i
                for j in n:
                    q += 1
                s = q-3
                if n[s:q] == '10\n':
                    q = q-1
                    a = n[s:q]
                    s = s-1
                    n = a + ' ' + n[0:s]
                elif n != '\n':
                    q = q-1
                    s = s+1
                    a = n[s:q]
                    s = s-1
                    n = a + ' ' + n[0:s]
                lines =lines + n
        file.close()
        with codecs.open ('loh.txt','w',encoding='utf-8', errors='ignore') as file:
            file.write(lines)
        file.close()
        with codecs.open('loh.txt',encoding='utf-8',errors='ignore') as file:
            lines = file.readlines()
        file.close()
        a = sorted(lines, reverse = True)
        for i in a:
            if i[0:2] == '10':
                o += i +'\n'
        with codecs.open('loh.txt','w',encoding='utf-8',errors='ignore') as file:
            file.write(o)
            for i in a:
                if i[0:2] != '10':
                    file.write(i +'\n')
        file.close()
        lines=''
        with codecs.open('loh.txt',encoding='utf-8',errors='ignore') as file:
            for i in file:
                n = i
                q = 0
                for j in n:
                    q += 1
                q = q-1
                if n[0:2] == '10':
                    a = n[0:2]
                    n = n[3:q] + ' ' + a
                elif n != '\n':
                    a = n[0:1]
                    n = n[2:q] + ' ' + a
                lines = lines + n
        file.close()
        with codecs.open ('loh.txt','w',encoding='utf-8', errors='ignore') as file:
            file.write(lines)
        file.close()
        with codecs.open('loh.txt',encoding='utf-8',errors='ignore') as file:
            lines = file.readlines()
        file.close()
        with codecs.open('loh.txt','w',encoding='utf-8',errors='ignore') as file:
            for i in lines:
                file.write(i+ '\n')
        file.close()
        with codecs.open('loh.txt',encoding='utf-8',errors='ignore') as file:
            a = file.read()
        file.close()
        bot.send_message(message.chat.id, a)
    else:
        bot.send_message(message.chat.id, 'Такой команды нет. /help')

bot.polling(none_stop=True)
