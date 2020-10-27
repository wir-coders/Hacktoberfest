import React from "react";
import ReactDOM from "react-dom";
import "bootstrap/dist/css/bootstrap.css";
import "./index.css";
import * as serviceWorker from "./serviceWorker";
import Game from "./components/GameComponent";

ReactDOM.render(
  <React.StrictMode>
    <Game />
    <div>
      <p>This website will give you correct solution of a valid<br></br> sudoku problem.</p><i><p>"Note that one particular sudoku problem may have<br></br>many multiple solutions but in this website, it is<br></br>showing only one of them so dont fear that its<br></br>not correct, it is, Believe me."</p></i>
      <b><p>How to use:</p></b><p>To fill input in the boxes firstly you<br></br>have to select the number which you want to fill<br></br>from below the matrix and then click on all the boxes<br></br>which should contain that number.<br></br>Once you are done with one number then select<br></br>another number from below the matrix, and click on<br></br>those boxes which should contain the another number.</p>
      <p>If you filled the number in a wrong box then select<br></br>Erase button from the below and then reclick on the<br></br>wrongly selected box.</p>
      <b><p>You will NOT BE ABLE TO FILL a number in any<br></br>box if that number is already present in that same<br></br>row/column or the 9-cell group. So illegal sudoku<br></br>problems can't be rendered and the app<br></br>won't crash :)</p></b>
      <p>When you have filled every number from the sudoku<br></br>problem then click "Solve it!" button to get the solution.</p>
    </div>
  </React.StrictMode>,
  document.getElementById("root")
);

serviceWorker.unregister();
