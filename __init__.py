from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class RockPaperScissorsSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder().require('RockPaperScissors'))
    def handle_rock_paper_scissors(self, message):
        self.speak_dialog('rock.paper.scissors')


def create_skill():
    return RockPaperScissorsSkill()

