#! /bin/python3

from rb_tree import RbTree

class Dump:
    def __init__(self):
        self.variants = []

    def output(self, name, values, combine = None):
        a = RbTree()
        iorder = ''

        html = '<html>\n<head>\n<title>{}</title>\n</head>\n\n<body>\n'.format(name)

        for v in values:
            a.insert(v)
            iorder += '_{}'.format(v)
            a.dot('dump/' + name + iorder + '.dot', 'insert order: ' + iorder)
            html += '<img src="{}"/><br/>\n'.format(name + iorder + '.dot.png')

        if combine is not None:
            a.delete(combine)
            a.dot('dump/'+ name +'comb.dot', 'combine: {}'.format(combine))
            html += '<img src="{}"/><br/>\n'.format(name + 'comb.dot.png')

        html += '</body>\n</html>\n'

        filename = 'dump/{}.html'.format(iorder)

        with open(filename, 'w') as f:
            f.write(html)

        a.dot('dump/' + name, iorder)

        self.variants.append((filename, name))

    def make_main(self):
        with open('main.html', 'w') as f:
            html = '<html>\n<head>\n<title>Main</title>\n</head>\n\n<body>\n'

            for (filename, name) in self.variants:
                html += '<a href="{}">{}</a><br/>'.format(filename, name)

            html += '</body>\n</html>\n'

            f.write(html)

a = Dump()

a.output('rb_2_2_1_v1', [1, 5, 6, 2, 4, 3])
a.output('rb_2_2_1_v2', [1, 5, 6, 2, 3, 4])
a.output('rb_2_2_1_v3', [1, 2, 6, 5, 4, 3])
a.output('rb_2_2_1_v4', [1, 2, 6, 5, 3, 4])
a.output('d', [1, 2])

a.output('rb', [1, 4, 5, 2, 3], 5)

a.make_main()
