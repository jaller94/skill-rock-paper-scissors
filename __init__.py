from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'christian'

LOGGER = getLogger(__name__)


class RockPaperScissorsSkill(MycroftSkill):
    def __init__(self):
        super(RockPaperScissorsSkill, self).__init__(name="RockPaperScissorsSkill")

    def initialize(self):
        rock_intent = IntentBuilder("RockIntent"). \
            require("ChoiceRock").build()
        self.register_intent(rock_intent, self.handle_choice_rock)

        paper_intent = IntentBuilder("PaperIntent"). \
            require("ChoicePaper").build()
        self.register_intent(paper_intent, self.handle_choice_paper)

        scissors_intent = IntentBuilder("ScissorsIntent"). \
            require("ChoiceScissors").build()
        self.register_intent(scissors_intent, self.handle_choice_scissors)

    def handle_choice_rock(self, message):
        self.speak_dialog("choice.rock")

    def handle_choice_paper(self, message):
        self.speak_dialog("choice.paper")

    def handle_choice_scissors(self, message):
        self.speak_dialog("choice.scissors")

    def stop(self):
        pass

def create_skill():
    return RockPaperScissorsSkill()
