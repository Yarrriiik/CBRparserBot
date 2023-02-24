import logging
import aiogram

from aiogram import types, Bot, Dispatcher, executor
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, message

bot = Bot(token="5595250602:AAHGvDIF1cwozhvk5PymIR3I1ayx99GfxtU")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

osmenu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Проверить финансовую организацию'), KeyboardButton(text='Warning list Банка России')],
    [KeyboardButton(text='Интернет-приёмная'), KeyboardButton(text='Контактная информация'), KeyboardButton(text='Проект финансовая культура')]
])



menu1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Выбрать', callback_data='quick_earnings')]
])
menu2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Выбрать', callback_data='lending_loans')]
])
menu8 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Выбрать', callback_data='broker')]
])
menu3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='В меню выбора', callback_data='selection_menu')]
])
menu4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Справочник финансовых организаций', callback_data='directory_of_organizations')]
])
menu5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Название', callback_data='name_menu')],
    [InlineKeyboardButton(text='ИНН', callback_data='inn_menufix')],
    [InlineKeyboardButton(text='Номер', callback_data='number_menu')],
    [InlineKeyboardButton(text='Предположительно, организации нет в реестрах:', callback_data='no_reestr')]
])
menu6 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Проверка на нелегальную деятельность', callback_data='neleg_deyat')]
])
menu7 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Наименование', callback_data='name_menu2')],
    [InlineKeyboardButton(text='ИНН', callback_data='inn_menu')],
    [InlineKeyboardButton(text='Сайт', callback_data='site_menu')],
    [InlineKeyboardButton(text='Адрес', callback_data='adres_menu')]
])
menu9 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Справочник финансовых организаций', callback_data='directory_of_organizations')],
    [InlineKeyboardButton(text='Warning list Банка России', callback_data='neleg_deyat')],
    [InlineKeyboardButton(text='В меню выбора', callback_data='selection_menu')]
])
menudel1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Убрать', callback_data='delmenu')]
])
tran1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Интернет-приёмная', url='https://cbr.ru/reception/')]
])
tran2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Контактная информация', url='https://cbr.ru/contacts/')]
])
tran3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Проект финансовая культура', url='https://fincult.info/')]
])


@dp.message_handler(commands= 'start', state='*')
async def start_commands(message: types.Message):
    to_pin = await bot.send_message(message.chat.id, 'Текст для закрепа')
    await bot.pin_chat_message(chat_id=message.chat.id, message_id=to_pin['message_id'])
    await bot.send_message(chat_id=message.from_user.id,
                           text='Что вас интересует?',
                           reply_markup=osmenu)
    await bot.send_message(chat_id=message.from_user.id,
                           text='Быстрый заработок, инвестиционные проекты, пассивный доход:',
                           parse_mode='HTML',
                           reply_markup=menu1)
    await bot.send_message(chat_id=message.from_user.id,
                           text='Кредитование, выдача займов, займы под залог ПТС / недвижимости:',
                           parse_mode='HTML',
                           reply_markup=menu2)
    await bot.send_message(chat_id=message.from_user.id,
                           text='Брокер, форекс-дилер, доверительное управление (профессиональные участники рынка ценных бумаг):',
                           parse_mode='HTML',
                           reply_markup=menu8)



@dp.message_handler(content_types='text')
async def internet_processing(message: types.Message):
    if message.text == 'Проверить финансовую организацию':
        await message.delete()
        await message.answer('Проверить финансовую организацию',
                             reply_markup=menu4)
    if message.text == 'Warning list Банка России':
        await message.delete()
        await message.answer('Warning list Банка России',
                             reply_markup=menu6)
    if message.text == 'Интернет-приёмная':
        await message.answer('Для перехода на интернет-приёмную:',
                             reply_markup=tran1)
    if message.text == 'Контактная информация':
        await message.answer('Для перехода на контактную информацию:',
                             reply_markup=tran2)
    if message.text == 'Проект финансовая культура':
        await message.answer('Для перехода на проект финансовой культуры:',
                             reply_markup=tran3)
    else:
        pass

@dp.callback_query_handler(Text(equals='quick_earnings'))
async def quick_earnings_processing(call: types.CallbackQuery):
    await call.answer()
    await bot.send_message(chat_id=call.from_user.id,
                           text='Если вам поступило предложение инвестировать денежные средства в какую-либо компанию или проект,'
                                ' запомните - участник рынка для предоставления большинства финансовых услуг на территории'
                                ' Российской Федерации должен иметь лицензию Банка России или быть включенным в реестр регулятора.\n\n'
                                'С особой настороженностью отнеситесь к предложениям, обосновывающим свою доходность за счет деятельности,'
                                ' не регулируемой законодательством Российской Федерации. К такой деятельности может относиться обещание'
                                ' заработка за счет роста цены криптоактива (токена); ”криптовалютный арбитраж” - перепродажа монет'
                                ' по более выгодному курсу; бинарные опционы; бизнес-курсы и тренинги и т.д.\n\n'
                                'Зачастую предложенные варианты быстрого и сверхдоходного заработка обладают признаками финансовой пирамиды (схема Понци, HYIP-проект, экономические игры и т.д.).\n\n'
                                'Существует несколько общих признаков финансовых пирамид:\n\n'
                                '    ▪️обещание высокой доходности, в несколько раз превышающей рыночный уровень;\n'
                                '    ▪️гарантирование доходности (что запрещено на рынке ценных бумаг);\n'
                                '    ▪️агрессивная реклама в средствах массовой информации, сети Интернет с обещанием высокой доходности;\n'
                                '    ▪️отсутствие какой-либо информации о финансовом положении организации;\n'
                                '    ▪️выплата денежных средств за счет новых привлеченных участников;\n'
                                '    ▪️отсутствие собственных основных средств, других дорогостоящих активов;\n'
                                '    ▪️нет точного определения деятельности организации;\n'
                                '    ▪️отсутствие лицензии на осуществление деятельности на финансовом рынке / информации в реестрах Банка России.\n\n'
                                'Но наличие этих признаков финансовой пирамиды не является достаточным основанием для однозначного (безошибочного)'
                                ' вывода об отнесении той или иной организации к ней.  Для правоохранительных и надзорных органов они являются лишь'
                                ' одним из сигналов для проведения в отношении организации, которая обладает такими признаками, проверочных мероприятий.\n\n'
                                'Подробно с деятельностью финансовых пирамид также можно ознакомиться <a href="https://fincult.info/article/finansovaya-piramida-kak-ee-raspoznat/">здесь</a>.',
                           parse_mode=types.ParseMode.HTML)
    await bot.send_message(chat_id=call.from_user.id,
                           text='Чтобы узнать находится ли компания в реестре Банка России (имеет ли лицензию), воспользуйтесь кнопкой "Проверить финансовую организацию".'
                                ' Также проверьте сведения о компании в Списке компаний с выявленными признаками нелегальной деятельности". Для этого выберите в меню "Warning list Банка России".',
                           reply_markup=menu9)


@dp.callback_query_handler(Text(equals='lending_loans'))
async def lending_loans_processing(call: types.CallbackQuery):
    await call.answer()
    await bot.send_message(chat_id=call.from_user.id,
                           text='Быть профессиональным кредитором, то есть выдавать кредиты и займы в денежной форме, могут'
                                ' только банки, микрофинансовые организации (МФО), кредитные потребительские кооперативы (КПК и СКПК) и ломбарды.\n\n'
                                'Если разрешения у компании (или лицензии у банка) нет, а она все равно привлекает клиентов, выдает себя за лицензированную'
                                ' и кредитует потребителей, то это нелегальный, или черный, кредитор. Такие нелегальные кредиторы могут действовать по-разному.'
                                ' Например, выдавать деньги под очень высокие проценты, но при этом не прибегать к откровенному криминалу.'
                                ' А могут использовать преступные схемы, чтобы обманом завладеть деньгами и имуществом клиентов.\n\n'
                                'Обратите внимание на сделки, совершаемые под видом финансовой аренды (лизинга). Обычно это связано'
                                ' с кредитованием под залог ПТС автомобиля. Зачастую указанные сделки могут быть притворными,'
                                ' т.е. сделками, которые совершаются с целью прикрыть другую сделку, в том числе сделку на иных условиях.\n\n'
                                'Подробно с деятельностью финансовых пирамид также можно ознакомиться <a href="https://fincult.info/article/kak-ne-stat-zhertvoy-chernykh-kreditorov/">здесь</a>.',
                           parse_mode=types.ParseMode.HTML)
    await bot.send_message(chat_id=call.from_user.id,
                           text='Чтобы узнать находится ли компания в реестре Банка России (имеет ли лицензию), воспользуйтесь кнопкой "Проверить финансовую организацию".'
                                ' Также проверьте сведения о компании в Списке компаний с выявленными признаками нелегальной деятельности". Для этого выберите в меню "Warning list Банка России".',
                           reply_markup=menu9)


@dp.callback_query_handler(Text(equals='broker'))
async def lending_loans_processing(call: types.CallbackQuery):
    await call.answer()
    await bot.send_message(chat_id=call.from_user.id,
                           text='Брокеры, форекс-дилеры, доверительные управляющие (или те, кто ими прикидывается) часто ссылаются'
                                ' на то, что рынок валюты — международный. И торговать на нем можно дистанционно откуда угодно'
                                ' и через кого угодно. Это действительно так, технических ограничений нет, но есть одно «но».\n\n'
                                'Если иностранный дилер нарушит ваши права, например не будет вовремя и правильно выполнять ваши'
                                ' поручения, вам придется отстаивать свои интересы самостоятельно. Все споры будут решаться в той'
                                ' стране и по законам той страны, где зарегистрирована эта компания. Российские регулятор и суд не смогут вам помочь.\n\n'
                                'Именно поэтому по закону зарубежные компании не имеют права работать на российском финансовом рынке.'
                                ' Так что если вы увидите рекламу иностранного форекс-дилера в рунете, то он уже нарушает закон.'
                                ' Вам решать: стоит ли работать с компанией, которая нелегально привлекает клиентов.\n\n'
                                'Часто «иностранными форекс-дилерами» себя называют откровенные мошенники. Они пользуются тем,'
                                ' что обычному человеку трудно проверить зарубежную компанию. Вам дают доступ к «торговому терминалу»,'
                                ' вы совершаете «сделки», количество денег на счете растет как на дрожжах. На самом деле вы получаете'
                                ' доступ к игре, имитирующей торговлю. Ее цель — разбудить ваш азарт и заставить внести'
                                ' на счет как можно больше денег. Но как только вы захотите вывести деньги со счета,'
                                ' возникнут непреодолимые проблемы: сбой программы, технические задержки и так далее.\n\n'
                                'При этом мошенники не только не возвращают деньги, но и побуждают клиентов заплатить'
                                ' еще больше. Часто требуют комиссию за срочный вывод денег. Или объясняют, что вывести'
                                ' можно только круглую сумму, например, 10 000 $. А если у вас на счете 6700, $ то нужно'
                                ' внести еще 3300, $ и только тогда вам все вернут. Но затем появляются «новые обстоятельства», и эту сумму тоже не выплачивают.\n\n'
                                'Подробнее о том как не попасться на нелегального участника рынка ценных бумаг прочитайте <a href="https://fincult.info/article/nelegalnyy-foreks-kak-ne-popastsya-na-udochku-moshennikov/">здесь</a>.\n\n'
                                '<a href="https://fincult.info/article/chto-takoe-foreks-forex-kak-rabotaet-torgovlya-na-etom-rynke/">Гайд</a>: как начать пользоваться услугами легального форекс-дилера.',
                           parse_mode=types.ParseMode.HTML)
    await bot.send_message(chat_id=call.from_user.id,
                           text='Чтобы узнать находится ли компания в реестре Банка России (имеет ли лицензию), воспользуйтесь кнопкой "Проверить финансовую организацию".'
                                ' Также проверьте сведения о компании в Списке компаний с выявленными признаками нелегальной деятельности". Для этого выберите в меню "Warning list Банка России".',
                           reply_markup=menu9)


@dp.callback_query_handler(Text(equals='next_menu'))
async def next_menu_processing(call: types.CallbackQuery):
    await call.answer()
    await bot.send_message(chat_id=call.from_user.id,
                           text='Для начала работы проверьте наличие компании в справочнике финансовых организаций',
                           reply_markup=menu4)


@dp.callback_query_handler(Text(equals='selection_menu'))
async def selection_menu_processing(call: types.CallbackQuery):
    await call.answer()
    await call.message.delete()
    await bot.send_message(chat_id=call.from_user.id,
                           text='Что вас интересует?',
                           reply_markup=osmenu)
    await bot.send_message(chat_id=call.from_user.id,
                           text='Быстрый заработок, инвестиционные проекты, пассивный доход:',
                           parse_mode='HTML',
                           reply_markup=menu1)
    await bot.send_message(chat_id=call.from_user.id,
                           text='Кредитование, выдача займов, займы под залог ПТС / недвижимости:',
                           parse_mode='HTML',
                           reply_markup=menu2)
    await bot.send_message(chat_id=call.from_user.id,
                           text='Брокер, форекс-дилер, доверительное управление (профессиональные участники рынка ценных бумаг):',
                           parse_mode='HTML',
                           reply_markup=menu8)


@dp.callback_query_handler(Text(equals='delmenu'))
async def selection_menu_processing(call: types.CallbackQuery):
    await call.answer()
    await call.message.delete()


@dp.callback_query_handler(Text(equals='directory_of_organizations'))
async def directory_of_organizations(call: types.CallbackQuery):
    await call.answer()
    await bot.send_message(chat_id=call.from_user.id,
                     text='В справочнике финансовых организаций можно узнать информации по: названию, ИНН, регистраионному номеру. Через что осуществить поиск?',
                     reply_markup=menu5)


@dp.callback_query_handler(Text(equals='name_menu'))
async def name_menu_processing(call: types.CallbackQuery):
    await call.answer()
    await bot.send_message(chat_id=call.from_user.id,
                           text='Укажите название организации\n\n'
                           'здесь вы укажите название, и вам выведут, есть ли организация или нет\n\n'
                                'В доработке')

@dp.callback_query_handler(Text(equals='inn_menufix'))
async def ogrn_menu_processing(call: types.CallbackQuery):
    await call.answer()
    await bot.send_message(chat_id=call.from_user.id,
                           text='Укажите ИНН организации\n\n'
                                'здесь вы укажите ИНН, и вам выведут, есть ли организация или нет\n\n'
                                'В доработке')

@dp.callback_query_handler(Text(equals='number_menu'))
async def number_menu_processing(call: types.CallbackQuery):
    await call.answer()
    await bot.send_message(chat_id=call.from_user.id,
                           text='Укажите номер организации\n\n'
                                'здесь вы укажите номер, и вам выведут, есть ли организация или нет)\n\n'
                                'В доработке')


@dp.callback_query_handler(Text(equals='no_reestr'))
async def no_reestr_processing(call: types.CallbackQuery):
    await call.answer()
    await bot.send_message(chat_id=call.from_user.id,
                           text='Компания не найдена в реестрах Банка России, проверьте наличие компании в списке компаний с выявленными нелегальной деятельности на финансовом рынке.',
                           reply_markup=menu6)


@dp.callback_query_handler(Text(equals='neleg_deyat'))
async def neleg_deyat_processing(call: types.CallbackQuery):
    await call.answer()
    await bot.send_message(chat_id=call.from_user.id,
                           text='В справочнике нелегальной деятельности организаций можно узнать информации по: названию, ИНН, адресу сайта. Через что осуществить поиск?',
                           reply_markup=menu7)


@dp.callback_query_handler(Text(equals='name_menu2'))
async def name_menu2_processing(call: types.CallbackQuery):
    await call.answer()
    await bot.send_message(chat_id=call.from_user.id,
                           text='Укажите название организации\n\n'
                                'здесь вы укажите название, и вам выведут, есть ли организация или нет)\n\n'
                                'В доработке')


@dp.callback_query_handler(Text(equals='inn_menu'))
async def name_menu2_processing(call: types.CallbackQuery):
    await call.answer()
    await bot.send_message(chat_id=call.from_user.id,
                           text='Укажите инн организации\n\n'
                                'здесь вы укажите ИНН, и вам выведут, есть ли организация или нет)\n\n'
                                'В доработке')


@dp.callback_query_handler(Text(equals='site_menu'))
async def name_menu2_processing(call: types.CallbackQuery):
    await call.answer()
    await bot.send_message(chat_id=call.from_user.id,
                           text='Укажите сайт организации\n\n'
                                'здесь вы укажите сайт, и вам выведут, есть ли организация или нет)\n\n'
                                'В доработке')


@dp.callback_query_handler(Text(equals='adres_menu'))
async def name_menu2_processing(call: types.CallbackQuery):
    await call.answer()
    await bot.send_message(chat_id=call.from_user.id,
                           text='Укажите адрес организации\n\n'
                                'здесь вы укажите адрес, и вам выведут, есть ли организация или нет)\n\n'
                                'В доработке')


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
