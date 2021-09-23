import React from "react";

import '../navbar/nav.css'

export class Ast extends React.Component{
    state={
        dot:''
    }
    componentDidMount = () => {
        this.setState({dot:String(this.props.arbol)})
      };

    render (){
       // var gap = this.state.dot
        return(
                <div className="input-group ast">
                  <span className="input-group-text">Resultado AST</span>
                  <textarea className="form-control" aria-label="With textarea" defaultValue={this.state.dot}>
                  </textarea>
                </div>
        );
    }
}