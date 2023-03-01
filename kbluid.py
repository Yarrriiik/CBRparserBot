from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

osmenu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Справочник финансовых организаций'), KeyboardButton(text='Warning list Банка России')],
    [KeyboardButton(text='Интернет-приёмная'), KeyboardButton(text='Контактная информация'), KeyboardButton(text='Возврат в меню выбора')]
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
menu11 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Выбрать', callback_data='osago')]
])
menu4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Справочник финансовых организаций', url='https://www.cbr.ru/fmp_check/')]
])
menu5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Наименование', callback_data='name_menu')],
    [InlineKeyboardButton(text='ИНН', callback_data='inn_menufix')],
    [InlineKeyboardButton(text='Номер', callback_data='number_menu')],
    [InlineKeyboardButton(text='Предположительно, организации нет в реестрах:', callback_data='no_reestr')]
])
menu6 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Проверка на нелегальную деятельность', callback_data='neleg_deyat')]
])
menu7 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Поиск', callback_data='name_menu2')]
])
menu9 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Справочник финансовых организаций', url='https://www.cbr.ru/fmp_check/')],
    [InlineKeyboardButton(text='Warning list Банка России', callback_data='neleg_deyat')],
    [InlineKeyboardButton(text='В меню выбора', callback_data='selection_menu')]
])
tran1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Интернет-приёмная', url='https://www.cbr.ru/reception/')]
])
tran2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Контактная информация', url='https://www.cbr.ru/contacts/')]
])
tran3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Возврат к меню выбора', callback_data='selection_menu')]
])
tran4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Warning list Банка России', callback_data='neleg_deyat')]
])