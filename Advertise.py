

class Advertise():

    def is_forwards(text: str) -> bool:
        if 'forwarded_from' in text:
            return True

    def is_RubinoPost(text: str) -> bool:
        if 'RubinoPost' in text:
            return True

    def is_StoryRubino(text: str) -> bool:
        if 'RubinoStory' in text:
            return True

    def is_link(text: str) -> bool:
        links: list = ['@', 'rubika']
        for link in links:
            if link in text:
                return True


