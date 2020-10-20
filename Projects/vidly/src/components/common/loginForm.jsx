import React, { Component } from 'react';
import Input from "./input";

class LoginForm extends Component {

    state = {
        account : {username: '' , password: ''}
    }

    username =React.createRef();

    handleChange = e => {
        const account = {...this.state.account};
        account[e.currentTarget.name] = e.currentTarget.value;
        this.setState({account});
    }

    handleSubmit = e => {
        e.preventDefault();
        console.log("submited");
    }
    
    render() { 
        return ( 
            <div>
                <br/><br/>
                <Input 
                    name="username"
                    value={this.state.account.username}
                    label="Username"
                    onChange={this.handleChange}
                />
                <Input 
                    name="password"
                    value={this.state.account.password}
                    label="Password"
                    onChange={this.handleChange}
                />
                <br/>
                <button onSubmit={this.handleSubmit} className="btn btn-primary">Submit</button>
                
            </div>
          );
    }
}
 
export default LoginForm;