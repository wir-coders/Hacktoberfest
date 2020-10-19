import React, { Component } from 'react';

class Main extends Component {

    // This code is very bekar

    state = {
        clicks : 0,
        tie : "",
        game : "",
        put : "put",
        btn1 : 0,
        btn2 : 0,
        btn3 : 0,
        btn4 : 0,
        btn5 : 0,
        btn6 : 0,
        btn7 : 0,
        btn8 : 0,
        btn9 : 0,
        btn1clr : "m-2 btn btn-outline-primary",
        btn2clr : "m-2 btn btn-outline-primary",
        btn3clr : "m-2 btn btn-outline-primary",
        btn4clr : "m-2 btn btn-outline-primary",
        btn5clr : "m-2 btn btn-outline-primary",
        btn6clr : "m-2 btn btn-outline-primary",
        btn7clr : "m-2 btn btn-outline-primary",
        btn8clr : "m-2 btn btn-outline-primary",
        btn9clr : "m-2 btn btn-outline-primary",
        disable1 : false,
        disable2 : false,
        disable3 : false,
        disable4 : false,
        disable5 : false,
        disable6 : false,
        disable7 : false,
        disable8 : false,
        disable9 : false,
        disableDelete : false,
        winOf1: 0,
        winOf2: 0,
        
    }

   handlePlay = () => {
       
       this.setState({clicks : 0});
       this.setState({tie : ""});
       this.setState({game : ""});
       this.setState({put : "put"});
       this.setState({btn1 : 0});
       this.setState({btn2 : 0});
       this.setState({btn3 : 0});
       this.setState({btn4 : 0});
       this.setState({btn5 : 0});
       this.setState({btn6 : 0});
       this.setState({btn7 : 0});
       this.setState({btn8 : 0});
       this.setState({btn9 : 0});
       this.setState({disable1 : false});
       this.setState({disable2 : false});
       this.setState({disable3 : false});
       this.setState({disable4 : false});
       this.setState({disable5 : false});
       this.setState({disable6 : false});
       this.setState({disable7 : false});
       this.setState({disable8 : false});
       this.setState({disable9 : false});
       this.setState({btn1clr : "m-2 btn btn-outline-primary"});
       this.setState({btn2clr : "m-2 btn btn-outline-primary"});
       this.setState({btn3clr : "m-2 btn btn-outline-primary"});
       this.setState({btn4clr : "m-2 btn btn-outline-primary"});
       this.setState({btn5clr : "m-2 btn btn-outline-primary"});
       this.setState({btn6clr : "m-2 btn btn-outline-primary"});
       this.setState({btn7clr : "m-2 btn btn-outline-primary"});
       this.setState({btn8clr : "m-2 btn btn-outline-primary"});
       this.setState({btn9clr : "m-2 btn btn-outline-primary"});
       
       this.setState({winOf1 : this.state.winOf1 + 1});
       
       this.setState({winOf2 : this.state.winOf2 + 1});
       
   }

    handelBtn1 = () => {
        
        if(this.state.clicks===9){
            this.setState({tie : <h1>Tie</h1>});
        }
        if (this.state.clicks < 9){
            this.setState({clicks : this.state.clicks + 1});
            console.log("btn1");
        }
        if((parseInt(this.state.clicks))%2===0) {
            this.setState({btn1 : 1});
            this.setState({btn1clr : "m-2 btn btn-warning"});
            this.setState({disable1 : true});
            console.log("if called");
        }
        else {
            this.setState({btn1 : 2});
            this.setState({btn1clr : "m-2 btn btn-success"});
            this.setState({disable1 : true});
            console.log("else called");
        }

        console.log(this.state.btn1);
    }

    handelBtn2 = () => {
        if(this.state.clicks===9){
            this.setState({tie : <h1>Tie</h1>});
        }
        if (this.state.clicks < 9){
            this.setState({clicks : this.state.clicks + 1});
            console.log("btn2");
        }
        if((parseInt(this.state.clicks))%2===0) {
            this.setState({btn2 : 1});
            this.setState({btn2clr : "m-2 btn btn-warning"});
            this.setState({disable2 : true});
        }
        else {
            this.setState({btn2 : 2});
            this.setState({btn2clr : "m-2 btn btn-success"});
            this.setState({disable2 : true});
        }
        console.log(this.state.btn2);
    }

    handelBtn3 = () => {
        if(this.state.clicks===9){
            this.setState({tie : <h1>Tie</h1>});
        }
        if (this.state.clicks < 9){
            this.setState({clicks : this.state.clicks + 1});
            console.log("btn3");
        }
        if((parseInt(this.state.clicks))%2===0) {
            this.setState({btn3 : 1});
            this.setState({btn3clr : "m-2 btn btn-warning"});
            this.setState({disable3 : true});
        }
        else {
            this.setState({btn3 : 2});
            this.setState({btn3clr : "m-2 btn btn-success"});
            this.setState({disable3 : true});
        }
        console.log(this.state.btn3);
    }

    handelBtn4 = () => {
        if(this.state.clicks===9){
            this.setState({tie : <h1>Tie</h1>});
        }
        if (this.state.clicks < 9){
            this.setState({clicks : this.state.clicks + 1});
            console.log("btn4");
        }
        if((parseInt(this.state.clicks))%2===0) {
            this.setState({btn4 : 1});
            this.setState({btn4clr : "m-2 btn btn-warning"});
            this.setState({disable4 : true});
        }
        else {
            this.setState({btn4 : 2});
            this.setState({btn4clr : "m-2 btn btn-success"});
            this.setState({disable4 : true});
        }
    }

    handelBtn5 = () => {
        if(this.state.clicks===9){
            this.setState({tie : <h1>Tie</h1>});
        }
        if (this.state.clicks < 9){
            this.setState({clicks : this.state.clicks + 1});
            console.log("btn5");
        }
        if((parseInt(this.state.clicks))%2===0) {
            this.setState({btn5 : 1});
            this.setState({btn5clr : "m-2 btn btn-warning"});
            this.setState({disable5 : true});
        }
        else {
            this.setState({btn5 : 2});
            this.setState({btn5clr : "m-2 btn btn-success"});
            this.setState({disable5 : true});
        }
    }

    handelBtn6 = () => {
        if(this.state.clicks===9){
            this.setState({tie : <h1>Tie</h1>});
        }
        if (this.state.clicks < 9){
            this.setState({clicks : this.state.clicks + 1});
            console.log("btn6");
        }
        if((parseInt(this.state.clicks))%2===0) {
            this.setState({btn6 : 1});
            this.setState({btn6clr : "m-2 btn btn-warning"});
            this.setState({disable6 : true});
        }
        else {
            this.setState({btn6 : 2});
            this.setState({btn6clr : "m-2 btn btn-success"});
            this.setState({disable6 : true});
        }
    }

    handelBtn7 = () => {
        if(this.state.clicks===9){
            this.setState({tie : <h1>Tie</h1>});
        }
        if (this.state.clicks < 9){
            this.setState({clicks : this.state.clicks + 1});
            console.log("btn7");
        }
        if((parseInt(this.state.clicks))%2===0) {
            this.setState({btn7 : 1});
            this.setState({btn7clr : "m-2 btn btn-warning"});
            this.setState({disable7 : true});
        }
        else {
            this.setState({btn7 : 2});
            this.setState({btn7clr : "m-2 btn btn-success"});
            this.setState({disable7 : true});
        }
    }

    handelBtn8 = () => {
        if(this.state.clicks===9){
            this.setState({tie : <h1>Tie</h1>});
        }
        if (this.state.clicks < 9){
            this.setState({clicks : this.state.clicks + 1});
            console.log("btn8");
        }
        if((parseInt(this.state.clicks))%2===0) {
            this.setState({btn8 : 1});
            this.setState({btn8clr : "m-2 btn btn-warning"});
            this.setState({disable8 : true});
        }
        else {
            this.setState({btn8 : 2});
            this.setState({btn8clr : "m-2 btn btn-success"});
            this.setState({disable8 : true});
        }
    }

    handelBtn9 = () => {
        if(this.state.clicks===9){
            this.setState({tie : <h1>Tie</h1>});
        }
        if (this.state.clicks < 9){
            this.setState({clicks : this.state.clicks + 1});
            console.log("btn9");
        }
        if((parseInt(this.state.clicks))%2===0) {
            this.setState({btn9 : 1});
            this.setState({btn9clr : "m-2 btn btn-warning"});
            this.setState({disable9 : true});
        }
        else {
            this.setState({btn9 : 2});
            this.setState({btn9clr : "m-2 btn btn-success"});
            this.setState({disable9 : true});
        }
    }

    resetCount = () => {
        this.setState({winOf1: 0});
    }
    

    render() { 
        let answer = "";
        let gameOver = "";
        if(this.state.btn1=== 1 && this.state.btn2=== 1 && this.state.btn3=== 1){
            answer+= "Player 1 won";
            gameOver+="Over";
            
            // return "Player 1 won";
        }
        else if(this.state.btn1=== 2 && this.state.btn2=== 2 && this.state.btn3=== 2){
            // return "Player 2 won";
            answer+= "Player 2 won";
            gameOver+="Over";
        } 
        //row1
        else if(this.state.btn4=== 1 && this.state.btn5=== 1 && this.state.btn6=== 1){
            // return "Player 1 won";
            answer+= "Player 1 won";
            gameOver+="Over";
        }
        else if(this.state.btn4=== 2 && this.state.btn5=== 2 && this.state.btn6=== 2){
            // return "Player 2 won";
            answer+= "Player 2 won";
            gameOver+="Over";
        }
        //row2
        else if(this.state.btn7=== 1 && this.state.btn8=== 1 && this.state.btn9=== 1){
            // return "Player 1 won";
            answer+= "Player 1 won";
            gameOver+="Over";
        }
        else if(this.state.btn7=== 2 && this.state.btn8=== 2 && this.state.btn9=== 2){
            // return "Player 2 won";
            answer+= "Player 2 won";
            gameOver+="Over";
        }
        //row3
        else if(this.state.btn1=== 1 && this.state.btn4=== 1 && this.state.btn7=== 1){
            // return "Player 1 won";
            answer+= "Player 1 won";
            gameOver+="Over";
        }
        else if(this.state.btn1=== 2 && this.state.btn4=== 2 && this.state.btn7=== 2){
            // return "Player 2 won";
            answer+= "Player 2 won";
            gameOver+="Over";
        }
        //col1
        else if(this.state.btn2=== 1 && this.state.btn5=== 1 && this.state.btn8=== 1){
            // return "Player 1 won";
            answer+= "Player 1 won";
            gameOver+="Over";
        }
        else if(this.state.btn2=== 2 && this.state.btn5=== 2 && this.state.btn8=== 2){
            // return "Player 2 won";
            answer+= "Player 2 won";
            gameOver+="Over";
        }
        //col2
        else if(this.state.btn3=== 1 && this.state.btn6=== 1 && this.state.btn9=== 1){
            // return "Player 1 won";
            answer+= "Player 1 won";
            gameOver+="Over";
        }
        else if(this.state.btn3=== 2 && this.state.btn6=== 2 && this.state.btn9=== 2){
            // return "Player 2 won";
            answer+= "Player 2 won";
            gameOver+="Over";
        }
        //col3
        else if(this.state.btn1=== 1 && this.state.btn5=== 1 && this.state.btn9=== 1){
            // return "Player 1 won";
            answer+= "Player 1 won";
            gameOver+="Over";
        }
        else if(this.state.btn1=== 2 && this.state.btn5=== 2 && this.state.btn9=== 2){
            // return "Player 2 won";
            answer+= "Player 2 won";
            gameOver+="Over";
        }//cross1
        else if(this.state.btn3=== 1 && this.state.btn5=== 1 && this.state.btn7=== 1){
            // return "Player 1 won";
            answer+= "Player 1 won";
            gameOver+="Over";
        }
        else if(this.state.btn3=== 2 && this.state.btn5=== 2 && this.state.btn7=== 2){
            // return "Player 2 won"
            answer+= "Player 2 won";
            gameOver+="Over";
        }//cross2
        else if(this.state.clicks===9 && answer==="") {
            answer+= "Tie hogaya bro";
            gameOver+="Over";
        }
        
        
        return ( 
            <div>
                <nav className="navbar navbar-expand-lg navbar-light bg-light">
                <button type="button" className="btn btn-info">
                 <span>Number Of Matches Played : </span>
                 <span className="badge badge-light "> {this.state.winOf1}</span>
                </button>
                <button onClick={() => this.resetCount()} className="btn btn-success btn-sm m-3" disabled={this.state.winOf1===0}> Reset Count</button>
                <div className="offset-2">
                <div className="m-4">
                <span className="badge badge-warning m-1">T</span>
                <span className="badge badge-dark m-1">I</span>
                <span className="badge badge-warning m-1">C</span>
                <span className="badge badge-dark m-1">T</span>
                <span className="badge badge-warning m-1">A</span>
                <span className="badge badge-dark m-1">C</span>
                <span className="badge badge-warning m-1">T</span>
                <span className="badge badge-dark m-1">O</span>
                <span className="badge badge-warning">E</span>
                </div>
                </div>
                </nav>
                <div className="App">
                <br/><br/><br/>
                <h4>Press any button to start the game noobs !</h4>
                <br/>
                {/* <h3>{this.state.clicks === 9 ? <span class="badge badge-light">{answer}</span> : 
                <span class="badge badge-light">Come on noobs</span>}</h3> */}
                <h3><span className="badge badge-light">{answer}</span></h3>
                <br/>
                
                <button onClick={() => this.handelBtn1()} 
                    className={this.state.btn1clr} disabled={this.state.disable1}>{this.state.btn1}</button>
                <button onClick={() => this.handelBtn2()} 
                    className={this.state.btn2clr} disabled={this.state.disable2}>{this.state.btn2}</button>
                <button onClick={() => this.handelBtn3()} 
                    className={this.state.btn3clr} disabled={this.state.disable3}>{this.state.btn3}</button>
                <br/>
                
                <button onClick={() => this.handelBtn4()} 
                    className={this.state.btn4clr} disabled={this.state.disable4}>{this.state.btn4}</button>
                <button onClick={() => this.handelBtn5()} 
                    className={this.state.btn5clr} disabled={this.state.disable5}>{this.state.btn5}</button>
                <button onClick={() => this.handelBtn6()} 
                    className={this.state.btn6clr} disabled={this.state.disable6}>{this.state.btn6}</button>
                <br/>

                <button onClick={() => this.handelBtn7()} 
                    className={this.state.btn7clr} disabled={this.state.disable7}>{this.state.btn7}</button>
                <button onClick={() => this.handelBtn8()} 
                    className={this.state.btn8clr} disabled={this.state.disable8}>{this.state.btn8}</button>
                <button onClick={() => this.handelBtn9()} 
                    className={this.state.btn9clr} disabled={this.state.disable9}>{this.state.btn9}</button>
                <br/>
                

                <button onClick={() => this.handlePlay()} className="btn btn-danger m-2" disabled={gameOver !== "Over"}>PLAY AGAIN</button>
                <br/><br/><br/>
                </div>
                <span className="badge badge-light offset-4"><h6>Instructions : </h6></span><br/>
                <span className="offset-4"><span className="badge badge-dark">1 </span> Consider 1 as "X" and 2 as "O"</span><br/>
                <span className="offset-4"><span className="badge badge-dark">2 </span> Every game will start from player 1 </span><br/>
                <span className="offset-4"><span className="badge badge-dark">3 </span> Don't reload the game </span><br/>
                {/* <span className="offset-4"><span className="badge badge-dark">4 </span> CSS itna nahi lagaya kyoki boor maar raha tha </span><br/> */}
                {/* <span className="offset-4"><span className="badge badge-danger">5 </span> Code bohot ganda likha hai please matt dekhna</span> */}
            </div>
        );
    }
}
 
export default Main;