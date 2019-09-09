#!/usr/bin/env python3.6

#
# Run with python 3.6+
#

import csv
import markdown
from jinja2 import Environment, FileSystemLoader, Markup, select_autoescape

env = Environment(
        loader = FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml']),
        extensions=['jinja2_highlight.HighlightExtension']
        )

env.extend(jinja2_highlight_cssclass = 'highlight')

common_pages = [
        'index',
]

for p in common_pages:
    print("Processing " + p)
    md = open(p + ".md", "r")
    content = markdown.markdown(md.read(),
            extensions = ['extra', 'smarty'],
            output_format='html5')
    template = env.get_template(p + ".html")
    file = open(p + ".html", "w")
    file.write(template.render(page = p, content = Markup(content)))
    file.close()

