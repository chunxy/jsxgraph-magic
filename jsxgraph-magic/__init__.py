from IPython.core.interactiveshell import InteractiveShell
from IPython.display import display, Javascript
from IPython.core.magic import Magics, magics_class, cell_magic
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring

@magics_class
class JSXGraph(Magics):
    
    @magic_arguments()
    @argument(
        'id', type=str,
        help="the id of the <div> element that embeds the board"
    )    
    @argument(
        '-w', '--width', type=int, default=600,
        help="the width of the output frame (default: 600)"
    )
    @argument(
        '-h', '--height', type=int, default=600,
        help="the height of the output frame (default: 600)"
    )
    
    @cell_magic
    def jsxgraph(self, line: str, cell: str = None):

        args = parse_argstring(self.jsxgraph, line)

        template = str('let div = document.createElement("div");\n'
                    'div.id = "{}"\n'
                    'div.style = "width:{}px;height:{}px"\n'
                    'element.append(div);\n')
        insert_dom = template.format(args.id, args.width, args.height)

        # These two scripts will invalidate the RequireJS context
        # when importing the JSXGraph in Jupyter Notebook
        # and restore the RequireJS after execution.
        nullify = str('if (typeof define === "function" && define.amd) {{\n'
                    'var old_define = define;\n'
                    'define = null\n'
                    '}}')
        restore = str('if (typeof define === "function" && define.amd) {{\n'
                    'define = old_define\n'
                    'old_define = null;\n'
                    '}}')

        lib = 'https://cdn.jsdelivr.net/npm/jsxgraph/distrib/jsxgraphcore.js'
        css = 'https://jsxgraph.org/distrib/jsxgraph.css'

        # These two steps must be separated, or else
        # the JSXGraph cannot find the binding HTMLElement.
        display(Javascript(insert_dom + nullify))
        display(Javascript(cell + restore, lib=lib, css=css))
        return None

def load_ipython_extension(ipython: InteractiveShell):
    """
    Register the magics with a running IPython so the magics can be loaded via
     `%load_ext jsxgraph` or be configured to be autoloaded by IPython at startup time.
    """
    ipython.register_magics(JSXGraph)