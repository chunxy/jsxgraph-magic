from IPython.core.interactiveshell import InteractiveShell
from IPython.display import display, Javascript

def jsxgraph(line: str, cell: str):
    args = line.strip().split()
    if len(args) == 0:
        return 'Please input like <num_boards> <height_1> ... <height_num_boards>!'
    for arg in args:
        if not arg.isnumeric():
            return 'Please input numeric values!'

    template = str('let div{0} = document.createElement("div");\n'
                   'div{0}.id = "board{0}"\n'
                   'div{0}.style = "height:{1}px;"\n'
                   'element.append(div{0});\n')
    num_boards = int(args[0])
    heights = args[1:]
    heights.extend([300 for i in range(num_boards - len(heights))])

    insert_dom = ''.join(template.format(i, heights[i]) for i in range(num_boards))

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
    ipython.register_magic_function(jsxgraph, 'cell')
