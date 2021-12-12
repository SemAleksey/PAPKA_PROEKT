class Tag:
    pass

    
class TagFactory:
    def create_tag(self, tag):
        self.tag = tag
        a = '<' + self.tag + '>' + '</' + self.tag + '>'
        return a


class Image(Tag):
    def get_image(self):
        return self.get_image


class Input(Tag):
    def get_input(self):
        return self.get_input
         

class Text(Tag):
    def get_text(self):
        return self.get_text


class Link(Tag):
    def get_link(self):
        return self.get_link


factory = TagFactory()
element = ['image', 'input', 'p', 'a', '']
for el in element:
    print(factory.create_tag(el))
