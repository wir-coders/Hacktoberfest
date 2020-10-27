import React, { Component } from "react";
import Board from "./BoardComponent";

class Game extends Component {
  constructor(props) {
    super(props);
    this.state = {
      squares: Array(81).fill(null),
      digits_1: [1, 2, 3, 4, 5],
      digits_2: [6, 7, 8, 9],
      isActive: null,
    };
  }

  isValidInput = (i, n, squares) => {
    let colNo = i % 9;
    let rowNo = Math.floor(i / 9);

    for (let j = 0; j < 9; j++) {
      if (squares[9 * j + colNo] === n || squares[9 * rowNo + j] === n) {
        console.log("colNo=", colNo, "rowNo", rowNo, " j=" + j);
        return false;
      }
    } // rows and cols check done!, But same block check remaining...

    let p = Math.floor(rowNo / 3),
      q = Math.floor(colNo / 3);
    p *= 3;
    q *= 3;

    //console.log("p=" + p + " q=" + q + " n=" + n + " i=" + i + " j=" + j);

    for (let k = p; k < p + 3; k++) {
      for (let l = q; l < q + 3; l++) {
        if (squares[9*k + l] === n) {
          return false;
        }
      }
    }

    return true;
  };

  handleCellClick = (i) => {
    if (this.state.isActive === null) {
      let newSquares = [...this.state.squares];
      newSquares[i] = this.state.isActive;
      this.setState({ squares: newSquares });
    } else if (this.isValidInput(i, this.state.isActive, this.state.squares)) {
      let newSquares = [...this.state.squares];
      newSquares[i] = this.state.isActive;
      this.setState({ squares: newSquares });
    } else {
      console.log("Invalid Input", i, this.state.isActive);
    }
  };

  handleNumClick = (i) => {
    this.setState({ isActive: i });
  };

  erase = (i) => {
    let newSquares = [...this.state.squares];
    newSquares[i] = "";
    this.setState({ squares: newSquares, isActive: "" });
  };

  reset = () => {
    let newSquares = Array(81).fill(null);
    this.setState({ squares: newSquares });
  }; // end-reset

  solve = () => {
    console.log(" 'Solve it' is called...");
    let board = Array(9);
    for (let i = 0; i < 9; i++) {
      board[i] = Array(9);
      for (let j = 0; j < 9; j++) {
        board[i][j] = this.state.squares[i * 9 + j]
          ? this.state.squares[i * 9 + j]
          : 0;
      }
    }

    if (this.solveSudoku(board)) {
      console.log("Misson Successful");

      let newSquares = Array(81).fill(0),
        p = 0;

      for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
          newSquares[p] = board[i][j];
          p++;
        }
      }

      this.setState({ squares: newSquares });
    } else {
      console.log("Invalid Input");

      alert("Invalid input");
    }
  }; // end-solve

  render() {
    let digits1 = this.state.digits_1.map((n) => {  // Number buttons from 1 to 5
      if (n === this.state.isActive) {
        return (
          <button
            key={n}
            className="badge badge-primary m-1 digit"
            onClick={() => this.handleNumClick(n)}
          >
            {n}
          </button>
        );
      } else {
        return (
          <button
            key={n}
            className="badge badge-warning m-1 digit"
            onClick={() => this.handleNumClick(n)}
          >
            {n}
          </button>
        );
      }
    });

    let digits2 = this.state.digits_2.map((n) => { // Number buttons from 6 to 9 for second row
      if (n === this.state.isActive) {
        return (
          <button
            key={n}
            className="badge badge-primary m-1 digit"
            onClick={() => this.handleNumClick(n)}
          >
            {n}
          </button>
        );
      } else {
        return (
          <button
            key={n}
            className="badge badge-warning m-1 digit"
            onClick={() => this.handleNumClick(n)}
          >
            {n}
          </button>
        );
      }
    });

    return (
      <div className="game">
        <div className="game-board pl-2">
          <Board
            squares={this.state.squares}
            onClick={(i) => this.handleCellClick(i)}
          />
        </div>

        <center>
          <div className="game-digits mt-2 pl-0">
            {digits1}
          </div>
          <div className="game-digits ml-0 pl-0">
            {digits2}
            <button
              className={
                this.state.isActive === null
                  ? "badge badge-primary m-1 digit digit-erase"
                  : "badge badge-warning m-1 digit digit-erase"
              }
              onClick={() => this.handleNumClick(null)}
            >
              Erase
            </button>
          </div>
        </center>

        <div>
          <center>
            <button
              className="solveitBtn btn btn-md btn-success m-2"
              onClick={this.solve}
            >
              Solve it!
            </button>
            <button
              className="solveitBtn btn btn-md btn-info m-2"
              onClick={this.reset}
            >
              Reset
            </button>
          </center>
        </div>
      </div>
    );
  } // end-render

  isValidTOPut = (i, j, n, board) => {
    for (let k = 0; k < 9; k++) {
      if (board[i][k] === n || board[k][j] === n) {
        return false;
      }
    }

    let p = Math.floor(i / 3),
      q = Math.floor(j / 3);
    p *= 3;
    q *= 3;

    //console.log("p=" + p + " q=" + q + " n=" + n + " i=" + i + " j=" + j);

    for (let k = p; k < p + 3; k++) {
      for (let l = q; l < q + 3; l++) {
        if (board[k][l] === n) {
          return false;
        }
      }
    }

    return true;
  }; // end-isValidTOPut

  solveSudoku(board) {
    let row = -1,
      col = -1,
      foundNull = false;

    for (let i = 0; i < 9; i++) {
      for (let j = 0; j < 9; j++) {
        if (board[i][j] === 0) {
          row = i;
          col = j;
          foundNull = true;
          break;
        }
      }
      if (foundNull) {
        break;
      }
    } // end-for1

    if (row === -1) {
      return true;
    }

    for (let i = 1; i < 10; i++) {
      if (this.isValidTOPut(row, col, i, board)) {
        board[row][col] = i;
        if (this.solveSudoku(board)) {
          return true;
        }
        board[row][col] = 0;
      }
    }

    return false;
  } // end-solveSudoku

  print = (board) => {
    for (let i = 0; i < 9; i++) {
      for (let j = 0; j < 9; j++) {
        console.log(board[i][j] + " ");
      }
      console.log("\n");
    }
  };
} // end-class

export default Game;
