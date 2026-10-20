from data_manager import DataManager
from template_manager import TemplateManager
from email_manager import EmailManager

from datetime import datetime
from random import randint

TEMPLATES_FOLDER = 'letter_templates'

dm = DataManager('birthdays.csv')
tm = TemplateManager(TEMPLATES_FOLDER)

today = datetime.today()
today_tuple = (today.month, today.day)
person_record = dm.search_data(today_tuple)
if person_record is not None:
    letter = tm.get_template(randint(1, 3)).replace(
        '[NAME]', person_record['name'])
    em = EmailManager()
    em.send_email('Happy Birthday !', letter, person_record['email'])
