"""↓ collaborations ↓"""
# import re
#
# string = "Bangalore office number 1234567891, " \
#          "My number is 8884278690, emergency " \
#          "contact 3456789123 invalid number 898883456"
# regexp = '\d{10}'  # Регулярное выражение, соответствующее числу из ровно 10 цифр
# match = re.findall(regexp, string)
# print(match)


"""↓ personal work ↓"""
import re

string = "Специалист контактного центра: +7-900-000-00-00\n " \
         "Добрый день, чем могу вам помочь ?\n " \
         "Я бы хотел посмотреть состояние лицевого счёта по номеру +7-900-017-02-58\n" \
         "Такой-то такой-то счёт\nСпасибо"
regexp = r"((\+7)-(\d{3})-(\d{3})-(\d{2})-(\d{2}))"
match = re.findall(regexp, string)
print(match)
