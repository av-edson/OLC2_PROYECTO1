import React from "react";

import '../navbar/nav.css'

export class Ast extends React.Component{
    state={
        dot:'',
        imagen:''
    }
    componentDidMount = () => {
        this.setState({dot:String(this.props.ast)})
        //console.log(this.props.ast)
        var dot = String(this.props.ast)
        dot = dot.split("\n").join("");
        //console.log(dot)
        const body = {
            "graph": dot        ,
            "layout": "dot",
            "format": "svg"
          };
        var url = "https://quickchart.io/graphviz?graph="+String(dot)
        fetch('https://quickchart.io/graphviz',{
            method:'POST',
            body: JSON.stringify(body),
            headers: {"Content-Type":"application/json"}
        }).then(async response =>{
            const svg = await response.text();
            //console.log(svg);
            this.setState({imagen:svg,dot:url})
            console.log(this.state.imagen)
            })
      };

    render (){
        //console.log(this.state.dot)
        return(
            <div className="ast">
                <p>hola</p>
            </div>
        );
    }
}