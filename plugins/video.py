# -*- coding: utf-8 -*-
"""
Adds support for embedding Youtube and Vimeo videos.

To use, include ``videos`` in the list of modules in your ``config.yml``.

There are two directives added: ``youtube`` and ``vimeo``. The only
argument is the video id of the video to include.

Both directives have three optional arguments: ``height``, ``width``
and ``align``. Default height is 281 and default width is 500. If ``align``
is not set, it defaults to ``none``.

Example::

    .. youtube:: anwy2MPT5RE
        :height: 315
        :width: 560
        :align: left

:copyright: (c) 2012 by Danilo Bargen.
:license: MIT
"""
from __future__ import absolute_import
from docutils import nodes
from docutils.parsers.rst import Directive, directives


def align(argument):
    """Conversion function for the "align" option."""
    return directives.choice(argument, ('left', 'center', 'right', 'none'))


class IframeVideo(Directive):
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'height': directives.nonnegative_int,
        'width': directives.nonnegative_int,
        'align': align,
    }
    default_width = 500
    default_height = 281

    def run(self):
        self.options['video_id'] = directives.uri(self.arguments[0])
        if not self.options.get('width'):
            self.options['width'] = self.default_width
        if not self.options.get('height'):
            self.options['height'] = self.default_height
        if not self.options.get('align'):
            self.options['align'] = 'none'
        return [nodes.raw('', self.html % self.options, format='html')]


class Youtube(IframeVideo):
    html = '<iframe src="http://www.youtube.com/embed/%(video_id)s" \
    width="%(width)u" height="%(height)u" frameborder="0" \
    webkitAllowFullScreen mozallowfullscreen allowfullscreen \
    class="align-%(align)s"></iframe>'


class Vimeo(IframeVideo):
    html = '<iframe src="http://player.vimeo.com/video/%(video_id)s" \
    width="%(width)u" height="%(height)u" frameborder="0" \
    webkitAllowFullScreen mozallowfullscreen allowFullScreen \
    class="align-%(align)s"></iframe>'


def register():
    """Plugin registration."""
    directives.register_directive('youtube', Youtube)
    directives.register_directive('vimeo', Vimeo)
