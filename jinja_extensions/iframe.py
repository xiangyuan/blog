# -*- coding: utf-8 -*-
"""
    rstblog.modules.iframe
    ~~~~~~~~~~~~~~~~~~~~~~

    Adds support for embedding iframes (e.g. for HTML presentations).

    To use, include ``iframe`` in the list of modules in your ``config.yml``.

    There is a new directive added: ``iframe``. The only argument is the source
    url of the iframe to include.

    The directive has eight optional arguments: ``height``, ``width`` ``id``,
    ``name``, ``class``, ``sandbox``, ``seamless`` and ``allowfullscreen``.
    They correspond to the html attributes of an iframe tag. Default height is
    500 and default width is 100%.

    Example::

        .. iframe:: http://github.com/

    Example 2::

        .. iframe:: http://google.com/
            :height: 315
            :width: 50%
            :id: my-iframe
            :name: my-iframe
            :class: iframe-type-3
            :sandbox: allow-popups allow-pointer-lock

    :copyright: (c) 2013 by Danilo Bargen.
    :license: BSD, see LICENSE for more details.
"""
from __future__ import absolute_import
from string import Template
from collections import defaultdict
from docutils import nodes
from docutils.parsers.rst import Directive, directives


class Iframe(Directive):
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'height': directives.unchanged_required,
        'width': directives.unchanged_required,
        'id': directives.class_option,
        'name': directives.class_option,
        'class': directives.class_option,
        'sandbox': directives.class_option,
        'seamless': directives.flag,
        'allowfullscreen': directives.flag,
    }
    default_width = '100%'
    default_height = '500'

    html = Template('<iframe src="$src" id="$id" name="$name" ' +
            'width="$width" height="$height" class="$class" ' +
            'sandbox="$sandbox" $seamless $allowfullscreen></iframe>')

    def run(self):
        options = defaultdict(str, self.options)
        options['src'] = directives.uri(self.arguments[0])
        if not options['width']:
            options['width'] = self.default_width
        if not options['height']:
            options['height'] = self.default_height
        options['id'] = '-'.join(options['id'])
        options['name'] = '-'.join(options['name'])
        options['class'] = ' '.join(options['class'])
        options['sandbox'] = ' '.join(options['sandbox'])
        if options['seamless'] is None:
            options['seamless'] = 'seamless'
        if options['allowfullscreen'] is None:
            options['allowfullscreen'] = 'allowfullscreen'
        return [nodes.raw('', self.html.substitute(options), format='html')]


def setup(builder):
    directives.register_directive('iframe', Iframe)
