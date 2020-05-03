from mycroft import MycroftSkill, intent_file_handler


class CheckGpio(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('gpio.check.intent')
    def handle_gpio_check(self, message):
        self.speak_dialog('gpio.check')


def create_skill():
    return CheckGpio()

