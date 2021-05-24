# from covidClass import Welcome, welcome_to_dict
from apikey import apikey
import logging

from telegram.ext import *
import coviddata
API_KEY = apikey()


def handle_text(msg):
    return (msg.split("-"))

# welcomeClass=Welcome()


def custom_command(update, context):
    logging.info(update.message.text)
    update.message.reply_text(
        'This is Covac Bot \n type -- covac-(pincode) -- command to get Vaccine Details')


def handle_sessions(ses):
    sessions_string = "\n-----------Sessions-----------\n"
    for ses_val in ses:
        new_str = f"\nDate: { ses_val['date']} ,\nAvailable_Capacity:{ses_val['available_capacity']},\n   ----Slots Timings---- \n{'    '.join([str(elem) for elem in ses_val['slots']])} \n"
        sessions_string += new_str
    return sessions_string


def handle_msg(update, context):
    # if update.message.text
    data = handle_text(update.message.text)
    if data[0] == "covac":
        response = coviddata.getCovidData(data[1])["centers"]
        if len(response)>0:
            for res in response:
                # print(welcome_to_dict(response))
                mod_res = f' Center Id : {str(res["center_id"])},\nCenter Name : {res["name"]},\nAddress : {res["address"] +  "  " + res["state_name"]},\n{handle_sessions(res["sessions"])}'
                update.message.reply_text(mod_res)
        else:
            update.message.reply_text("No Centers Available To this Pin Code")
    if data[0] == "help":
        update.message.reply_text(
            'This is Covac Bot\ntype -- covac-(pincode) -- command to get Vaccine Details')


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


if __name__ == "__main__":
    updater = Updater(API_KEY, use_context=True)
    tm = updater.dispatcher
    tm.add_handler(MessageHandler(Filters.text, handle_msg))
    tm.add_handler(CommandHandler('help', custom_command))

    updater.start_polling(1.0)
    updater.idle()
