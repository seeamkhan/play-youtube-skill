from mycroft import MycroftSkill, intent_file_handler


class PlayYoutube(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('youtube.play.intent')
    def handle_youtube_play(self, message):
        self.speak_dialog('youtube.play')


def create_skill():
    return PlayYoutube()

