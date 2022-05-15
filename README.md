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
  cd dimagic
  pip install ./
  ```

## Usage

- As with usual **IPython** magic, remember to `%load_ext jsxgraph` before using this magic.

- This repo contains two magics: one line magic and one cell magic, both named as **jsxgraph**. 

  - The line magic requires no arguments and simply prompt the help message. 

  - The cell magic should be used as:

    ```
    %%jsxgraph n height1 ... heightn
    <JSXGraph descriptions>
    ```

    where `n` is the number of boards to create and `height1 ... heightn` are the heights of `n` boards in the unit of `px`. `<JSXGraph descriptions>` should be the JavaScript to describe the graphs. 

    It will return you `n ` `HTMLELement`s in the output cell, with `id` being `board0`, `board1`, ..., `board${n}` which you can use to bind the drawing board. 

    For example, `%%jsxgraph 2 300 300` will create two boards with height being `300px`. Their ids will be `board0`, `board1` respectively. 



