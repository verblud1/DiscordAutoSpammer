from http.client import OK
import pyautogui as q
import time
import sys


class Auto():

    def typeMes():
        conf = q.confirm('Начинаем? (Убедитесь, что вы сейчас в Discord)', title='Автоматический режим', buttons=['OK', 'Cancel'])

        if conf == 'OK':     
            Auto.input_text()
        if conf=="Cancel":
            main()

    def input_text():
        num = q.prompt('Введите необходимое число букв')

        try:
            for i in range(int(num)):
                q.write('0')
                q.PAUSE = 0.001
            q.press('enter')
            Auto.typeMes()
        except Exception as e:
            q.alert(f'ОШИБКА! {e}')
            main()

class Custom():
    
    def typeMes():
        conf = q.confirm('Начинаем? (Убедитесь, что вы сейчас в Discord)', title='Настраиваемый режим', buttons=['OK', 'Cancel'])

        if conf == 'OK':     
            Custom.input_text()
        if conf=="Cancel":
            main()

    def input_text():
        st=q.confirm('Отправлять все одним сообщением?', buttons=['Yes', 'No'])

        if st == 'Yes':
            Custom.one_mes()
        else:
            Custom.some_mes()

    def some_mes():
        text = q.prompt('Введите текст')
        num= q.prompt('Сколько кругов?')
        delay= q.prompt('Сколько секунд задержка? (от 1 до бесконечности)')

        try:
            for i in range(int(num)):
                q.write(text)
                q.press('enter')
                q.PAUSE = int(delay)
            Custom.typeMes()
        except Exception as e:
            q.alert(f'ОШИБКА! {e}')
            main()

    def one_mes():
        text = q.prompt('Введите текст')
        num= q.prompt('Сколько кругов?')

        try:
            for i in range(int(num)):
                q.write(text)
                q.PAUSE = 0.01
            q.press('enter')
            Custom.typeMes()
        except Exception as e:
            q.alert(f'ОШИБКА! {e}')
            main()

def main():
        main_text = q.confirm('''
        -------------------------------------------
        Made Verblud1 (https://github.com/verblud1)
        -------------------------------------------
        Внимание!
        1.Не выключайте дискорд во время работы программы.
        2.Удачи! =).
        -------------------------------------------------
        ''', title='DiscordAutoSpammer', buttons=['Продолжить', 'Выход'])
        if main_text=='Продолжить':
            choose()

def choose():
    auto='Автоматический(рекомендуется для накрутки Комбо)'
    custom='Настраиваемый'
    ch=q.confirm('Выберите режим', title='DiscordAutoSpammer', buttons=[auto,custom])

    if ch==auto:
        Auto.typeMes()
    else:
        Custom.typeMes()

main()