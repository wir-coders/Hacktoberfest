import React, { Component } from "react";
import Square from "./SquareComponent";

class Board extends Component {
  renderSquare(i) {
    return (
      <Square
        value={this.props.squares[i]}
        onClick={() => this.props.onClick(i)}
      />
    );
  }

  render() {
    return (
      <>
        <div className="container board">
          <div className="row r1">
            <div className="col c1">
              {this.renderSquare(0)}
              {this.renderSquare(1)}
              {this.renderSquare(2)}
            </div>
            <div className="col c2">
              {this.renderSquare(3)}
              {this.renderSquare(4)}
              {this.renderSquare(5)}
            </div>
            <div className="col c3">
              {this.renderSquare(6)}
              {this.renderSquare(7)}
              {this.renderSquare(8)}
            </div>
          </div>

          <div className="row r2">
            <div className="col c1">
              {this.renderSquare(9)}
              {this.renderSquare(10)}
              {this.renderSquare(11)}
            </div>
            <div className="col c2">
              {this.renderSquare(12)}
              {this.renderSquare(13)}
              {this.renderSquare(14)}
            </div>
            <div className="col c3">
              {this.renderSquare(15)}
              {this.renderSquare(16)}
              {this.renderSquare(17)}
            </div>
          </div>

          <div className="row r3 pb-2">
            <div className="col c1">
              {this.renderSquare(18)}
              {this.renderSquare(19)}
              {this.renderSquare(20)}
            </div>
            <div className="col c2">
              {this.renderSquare(21)}
              {this.renderSquare(22)}
              {this.renderSquare(23)}
            </div>
            <div className="col c3">
              {this.renderSquare(24)}
              {this.renderSquare(25)}
              {this.renderSquare(26)}
            </div>
          </div>

          <div className="row r4">
            <div className="col c1">
              {this.renderSquare(27)}
              {this.renderSquare(28)}
              {this.renderSquare(29)}
            </div>
            <div className="col c2">
              {this.renderSquare(30)}
              {this.renderSquare(31)}
              {this.renderSquare(32)}
            </div>
            <div className="col c3">
              {this.renderSquare(33)}
              {this.renderSquare(34)}
              {this.renderSquare(35)}
            </div>
          </div>

          <div className="row r5">
            <div className="col c1">
              {this.renderSquare(36)}
              {this.renderSquare(37)}
              {this.renderSquare(38)}
            </div>
            <div className="col c2">
              {this.renderSquare(39)}
              {this.renderSquare(40)}
              {this.renderSquare(41)}
            </div>
            <div className="col c3">
              {this.renderSquare(42)}
              {this.renderSquare(43)}
              {this.renderSquare(44)}
            </div>
          </div>

          <div className="row r6 pb-2">
            <div className="col c1">
              {this.renderSquare(45)}
              {this.renderSquare(46)}
              {this.renderSquare(47)}
            </div>
            <div className="col c2">
              {this.renderSquare(48)}
              {this.renderSquare(49)}
              {this.renderSquare(50)}
            </div>
            <div className="col c3">
              {this.renderSquare(51)}
              {this.renderSquare(52)}
              {this.renderSquare(53)}
            </div>
          </div>

          <div className="row r7">
            <div className="col c1">
              {this.renderSquare(54)}
              {this.renderSquare(55)}
              {this.renderSquare(56)}
            </div>
            <div className="col c2">
              {this.renderSquare(57)}
              {this.renderSquare(58)}
              {this.renderSquare(59)}
            </div>
            <div className="col c3">
              {this.renderSquare(60)}
              {this.renderSquare(61)}
              {this.renderSquare(62)}
            </div>
          </div>

          <div className="row r8">
            <div className="col c1">
              {this.renderSquare(63)}
              {this.renderSquare(64)}
              {this.renderSquare(65)}
            </div>
            <div className="col c2">
              {this.renderSquare(66)}
              {this.renderSquare(67)}
              {this.renderSquare(68)}
            </div>
            <div className="col c3">
              {this.renderSquare(69)}
              {this.renderSquare(70)}
              {this.renderSquare(71)}
            </div>
          </div>

          <div className="row r9">
            <div className="col c1">
              {this.renderSquare(72)}
              {this.renderSquare(73)}
              {this.renderSquare(74)}
            </div>
            <div className="col c2">
              {this.renderSquare(75)}
              {this.renderSquare(76)}
              {this.renderSquare(77)}
            </div>
            <div className="col c3">
              {this.renderSquare(78)}
              {this.renderSquare(79)}
              {this.renderSquare(80)}
            </div>
          </div>
        </div>
      </>
    );
  }
}

export default Board;
