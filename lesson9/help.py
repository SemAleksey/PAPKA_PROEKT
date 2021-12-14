class TagFactory:
    def __init__(self):
        pass

    def create_tag(self, tag, *args, **kwargs):
        created_tag = self._create_tag(tag, args, kwargs)
        return created_tag

    def _create_tag(self, tag, *args, **kwargs):
        if tag == 'image':
            src = input('Enter src for image tag: ')
            return Image(tag, src)
        else:
            raise ValueError('that kind of tags is not supported yet')


class Tag:
    def __init__(self, name, *args, **kwargs):
        print('creating new tag {}'.format(name))
        self.name = name
        self.tag = ''

    def get_html(self):
        return "<{0}></{0}>".format(self.tag)


class Image(Tag):
    def __init__(self, name, src):
        super().__init__(name)
        self.tag = 'img'
        self.src = src

        

    def get_html(self):
        return "<{0} src='{1}'>".format(self.tag, self.src)


factory = TagFactory()
elements = ['image', 'p']
for el in elements:
    print(factory.create_tag(el).get_html())