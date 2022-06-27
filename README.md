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

- This repo contains the cell magic named as **jsxgraph**. The magic should be used as:

  ```
   %%jsxgraph [-w WIDTH] [-h HEIGHT] id
   <JSXGraph descriptions>
  ```
  
  where **id** is the `id` of the HTML element to embed the JSXGraph board, **width** and **height** is the width and height of the board in `px` respectively,  **\<JSXGraph descriptions\>** is the usual JavaScript code to describe the graph using the JSXGraph library.
  
  You may also run the following magic to see the description:
  
  ```
  %%jsxgraph?
  ```

A simple example of [Five-circle Theorem](https://en.wikipedia.org/wiki/Five_circles_theorem) (code from JSXGrpah website) will be

```
%%load_ext jsxgraph-magic
```

```
%%jsxgraph jxgbox -w 400 -h 400
var brd = JXG.JSXGraph.initBoard('jxgbox',{boundingbox:[-5,5,5,-5]});
var p = [], l = [], i = [], c = [], j = [], k;

p[0] = brd.create('point',[-2.5,-3],{name:'',strokeColor:'#7355ff',fillColor:'#7355ff'});
p[1] = brd.create('point',[-0,4],{name:'',strokeColor:'#7355ff',fillColor:'#7355ff'});
p[2] = brd.create('point',[2.5,-3],{name:'',strokeColor:'#7355ff',fillColor:'#7355ff'});
p[3] = brd.create('point',[-4,0],{name:'',strokeColor:'#7355ff',fillColor:'#7355ff'});
p[4] = brd.create('point',[4,0],{name:'',strokeColor:'#7355ff',fillColor:'#7355ff'});

for (k=0;k<5;k++) {
   l[k] = brd.create('segment',[p[k],p[(k+1)%5]],{strokeColor:'black',strokeWidth:1});
}

for (k=0;k<5;k++) {
   i[k] = brd.create('intersection',[l[k],l[(k+2)%5],0],{name:'',strokeColor:'#EAEA00',fillColor:'#EAEA00'});
}

for (k=0;k<5;k++) {
   c[k] = brd.create('circumcircle',[p[k],i[k],i[(k+2)%5]],{strokeColor:'gray', strokeWidth:1, point: {visible: false}});
}
for (k=0;k<5;k++) {
   j[k] = brd.create('intersection',[c[k],c[(k+2)%5],0],{name:'',strokeColor:'#EA0000',fillColor:'#EA0000'});
}

cc = brd.create('circumcircle',[j[0],j[2],j[3]],{strokeColor:'red',strokeWidth:2,point:{strokeColor:'#000000',fillColor:'#000000',size:1}});
brd.update();
```





