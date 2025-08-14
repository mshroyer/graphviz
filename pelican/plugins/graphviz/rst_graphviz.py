"""reStructuredText extension for the Graphviz plugin for Pelican."""

import base64

from docutils import nodes
from docutils.parsers.rst import Directive

from .mdx_graphviz import run_graphviz


class GraphvizDirective(Directive):
    """RST directive for embedded Graphviz."""

    required_arguments = 1
    has_content = True

    def run(self):
        program = self.arguments[0]
        src = "\n".join(self.content)
        output = run_graphviz(program, src, format="svg")

        img = '<img alt="GraphViz graph" src="data:image/svg+xml;base64,{}">'.format(
            base64.b64encode(output).decode("ascii")
        )
        svg_node = nodes.raw("", img, format="html")
        container = nodes.container("", svg_node, classes=["graphviz"])
        return [container]
