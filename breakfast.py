## Breakfast

def cook():
    print('Get the ingredients\nMix the ingredients\nPut the pan on fire')
    print('Pour mixture into the pan\nFlip to the other side')

def serve_special(extra, breakfast):
    print('Yummy {0} with {1}'.format(breakfast, extra))

def serve_normal(breakfast):
    print('Yummy', breakfast)



def make_breakfast():
    b = input('What would you like for breakfast? Eggs or Pancakes? ')
    if b.lower() == 'eggs':
        t = input('Special or normal {}? (s/n) '.format(b))
        if t.lower() == 'n':
            cook()
            serve_normal(b)
        elif t.lower() == 's':
            e = input('What extra ingredient would you like? ')
            cook()
            serve_special(e, b)

    elif b.lower() == 'pancakes':
        t = input('Special or normal {}? (s/n) '.format(b))
        if t.lower() == 'n':
            cook()
            serve_normal(b)
        elif t.lower() == 's':
            e = input('What extra ingredient would you like? ')
            cook()
            serve_special(e, b)

def main():
    make_breakfast()

if __name__ == '__main__':
    main()
