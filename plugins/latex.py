# -*- coding: utf-8 -*-
"""
Latex Plugin For Pelican
========================

This plugin allows you to write mathematical equations in your articles using Latex.
It uses the MathJax Latex JavaScript library to render latex that is embedded in
between `$..$` for inline math and `$$..$$` for displayed math. It also allows for
writing equations in by using `\begin{equation}`...`\end{equation}`.
"""

from pelican import signals
from docutils import nodes
from docutils.parsers.rst import Directive, directives


latexScript = """
    <script src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type= "text/javascript">
       MathJax.Hub.Config({
           config: ["MMLorHTML.js"],
           jax: ["input/TeX", "input/MathML", "output/HTML-CSS", "output/NativeMML"],
           TeX: {
               extensions: ["AMSmath.js", "AMSsymbols.js", "noErrors.js", "noUndefined.js"],
               equationNumbers: { autoNumber: "AMS" }
           },
           extensions: ["tex2jax.js", "mml2jax.js", "MathMenu.js", "MathZoom.js"],
           tex2jax: {
               inlineMath: [ [\'$\',\'$\'] ],
               displayMath: [ [\'$$\',\'$$\'] ],
               processEscapes: true },
           "HTML-CSS": {
               styles: { ".MathJax .mo, .MathJax .mi": {color: "black ! important"}}
           }
       });
    </script>
"""


class LatexBlock(Directive):
    """This directive does absolutely nothing with the input. It gets outputted
    directly without processing."""

    option_spec = {'class': directives.class_option}
    has_content = True

    def run(self):
        self.assert_has_content()
        # join lines, separate blocks
        content = '\n'.join(self.content)
        return [nodes.raw('', '<div class="docutils">{}</div>'.format(content), format='html')]


def add_latex(gen, metadata):
    """The registered handler for the latex plugin.
    It will add the latex script to the article metadata."""
    if 'LATEX' in gen.settings.keys() and gen.settings['LATEX'] == 'article':
        if 'latex' in metadata.keys():
            metadata['latex'] = latexScript
    else:
        metadata['latex'] = latexScript


def register():
    """Plugin registration."""
    signals.article_generator_context.connect(add_latex)
    signals.page_generator_context.connect(add_latex)
    directives.register_directive('latex', LatexBlock)
