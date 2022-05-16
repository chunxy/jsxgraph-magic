# jsxgraph-magic

**jsxgraph-magic** is an **IPython** magic wrapper for the famous JavaScript math-sketching package [JSXGraph](https://github.com/jsxgraph/jsxgraph). **jsxgraph-magic** enables you to use **JSXGraph** in Notebook and see the sketching in the output cell.

## Requirements
- A network connection is required to fetch the **JavaScript** and **CSS** file for **JSXGraph**.
- **IPython** is required since the magics are concept from the **IPython**.
- **IPython** alone cannot be much useful. It is usually accompanied with Jupyter Notebook or Jupyter Lab. Please try either.

## Installation

- From source code
  
  ```shell
  git clone https://github.com/chunxy/jsxgraph-magic.git
  cd jsxgraph-magic
  pip install ./
  ```

## Usage

- As with usual **IPython** magic, remember to `%load_ext jsxgraph-magic` before using this magic.

- This repo contains two magics: one line magic and one cell magic, both named as **jsxgraph**. 

  - The line magic requires no arguments and simply prompt the help message. 

    ```
    %jsxgraph
    ```
  
  - The cell magic should be used as:
  
    ```
    %%jsxgraph height1 ... heightn
    <JSXGraph descriptions>
    ```

    It will create `n ` `div`s in the output cell, with `id` being `board0`, `board1`, ..., `board${n-1}`, and height being  `height1 ... heightn` in the unit of `px`.  `<JSXGraph descriptions>`  is the JavaScript code to bind the drawboard with corresponding `HTMLElement` as well as to describe the graphs.
  
    ```
    %%jsxgraph 300 300
    // Initialize board
    var drawboard0 = JXG.JSXGraph.initBoard('board0');
    var drawboard1 = JXG.JSXGraph.initBoard('board1');
    // More code
    ```
    
    As an example, the above code will create two `div`s with height both being `300px`. Their `id`s will be `board0`, `board1` respectively. Then we bind them with the corresponding `drawboard`s.



