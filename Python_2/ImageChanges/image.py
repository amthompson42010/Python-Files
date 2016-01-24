class Color:
    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b

    def get_red(self):
        return self.red

    def get_green(self):
        return self.green

    def get_blue(self):
        return self.blue

    def __eq__(self, other):
        return self.red == other.red and self.green == other.green and self.blue == other.blue

    def __str__(self):
        return ' '.join([str(self.red), str(self.green), str(self.blue)])

    def __repr__(self):
        return str(self)

class PortablePixmap:
    def __init__(self, magic, w, h, m, p):
        # this is so dumb.
        self.magic_number = magic
        self.width = w
        self.height = h
        self.max_color = m
        if p:
            if type(p[0]) is list:
                self.pixels = p
            elif type(p[0]) is Color:
                self.pixels = list()
                counter = self.width
                for c in p:
                    if counter == self.width:
                        counter = 0
                        self.pixels.append(list())

                    self.pixels[-1].append(c)
                    counter += 1
        else:
            self.pixels = list()

    def flop(self):
        for i in self.pixels:
            i.reverse()
        s = self.magic_number + '\n'
        s += str(self.width) + ' ' + str(self.height) + '\n'
        s += str(self.max_color) + '\n'
        for row in self.pixels:
            for c in row:
                s += str(c) + '\n'
        return s

    def flip(self):
        for i in self.pixels:
            i.reverse()
        s = self.magic_number + '\n'
        s += str(self.width) + ' ' + str(self.height) + '\n'
        s += str(self.max_color) + '\n'
        for row in self.pixels:
            for c in row:
                s += str(c) + '\n'
        return s

    def grayscale(self):
        s = self.magic_number + '\n'
        s += str(self.width) + ' ' + str(self.height) + '\n'
        s += str(self.max_color) + '\n'
        for row in self.pixels:
            for c in row:
                s += str(c) + '\n'
        return s

def read_ppm(fl):
    with open(fl) as fp:
        r = grayscale_reader(fp)
    
    return r

def read_ppm2(fl2):
    with open(fl2) as f:
        r = reader2(f)
    return r

def read_ppm3(fl3):
    with open(fl3) as fa:
        r = reader3(fa)
    return r

def grayscale_reader(fp):
    tokens = list()
    pixels = list()
    for line in fp:
        tokens.extend(line.split())

    assert len(tokens) >= 4

    magic_number = tokens[0]
    assert magic_number == 'P3'

    width = int(tokens[1])
    assert width >= 0

    height = int(tokens[2])
    assert height >= 0

    max_color = int(tokens[3])
    assert max_color > 0

    rgbs = zip(tokens[4::3], tokens[5::3], tokens[6::3])

    for r,g,b in rgbs:
        red = int(int(r) * 0.2126)
       # assert red >= 0
       # assert red <= max_color

        green = int(int(g) * 0.7152)
       # assert green >= 0
       # assert green <= max_color

        blue = int(int(b) * 0.0722)
       # assert blue >= 0
       # assert blue <= max_color

        grey = red + green + blue
        pixels.append(Color(grey, grey, grey))
    
    a = PortablePixmap(magic_number, width, height, max_color, pixels)
    return a.grayscale()

def reader2(fp):
    tokens = list()
    pixels = list()
    for line in fp:
        tokens.extend(line.split())

    assert len(tokens) >= 4

    magic_number = tokens[0]
    assert magic_number == 'P3'

    width = int(tokens[1])
    assert width >= 0

    height = int(tokens[2])
    assert height >= 0

    max_color = int(tokens[3])
    assert max_color > 0

    rgbs = zip(tokens[4::3], tokens[5::3], tokens[6::3])

    for r,g,b in rgbs:
        red = int(r)
        assert red >= 0
        assert red <= max_color

        green = int(g)
        assert green >= 0
        assert green <= max_color

        blue = int(b)
        assert blue >= 0
        assert blue <= max_color

        pixels.append(Color(red, green, blue))
    
    a = PortablePixmap(magic_number, width, height, max_color, pixels)
    return a.flip()

def reader3(fp):
    tokens = list()
    pixels = list()
    for line in fp:
        tokens.extend(line.split())

    assert len(tokens) >= 4

    magic_number = tokens[0]
    assert magic_number == 'P3'

    width = int(tokens[1])
    assert width >= 0

    height = int(tokens[2])
    assert height >= 0

    max_color = int(tokens[3])
    assert max_color > 0

    rgbs = zip(tokens[4::3], tokens[5::3], tokens[6::3])

    for r,g,b in rgbs:
        red = int(r)
        assert red >= 0
        assert red <= max_color

        green = int(g)
        assert green >= 0
        assert green <= max_color

        blue = int(b)
        assert blue >= 0
        assert blue <= max_color

        pixels.append(Color(red, green, blue))
    
    a = PortablePixmap(magic_number, width, height, max_color, pixels)
    return a.flop()
