from IPython.display import display, Javascript, Pretty
from IPython.core.magic import register_line_cell_magic

@register_line_cell_magic
def jsxgraph(line: str, cell: str = None):

    info = str('The cell magic should be used as:\n\n'
               '%%jsxgraph height1 ... heightn\n'
               '<drawboard binding and JSXGraph description>\n')
    erro = 'Please pass positive numeric value for heights!\n'

    if cell is None:
        return display(Pretty(info))
    args = line.strip().split()
    if len(args) == 0:
        return display(Pretty(info))

    for arg in args:
        if not arg.isnumeric() or arg[0] == '-':
            return display(Pretty(erro + info))

    template = str('let div{0} = document.createElement("div");\n'
                   'div{0}.id = "board{0}"\n'
                   'div{0}.style = "height:{1}px;"\n'
                   'element.append(div{0});\n')
    insert_dom = ''.join(template.format(i, args[i]) for i in range(len(args)))

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
