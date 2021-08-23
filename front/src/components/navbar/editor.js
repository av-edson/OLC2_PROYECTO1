import React from "react";
import { UnControlled as CodeMirror } from 'react-codemirror2';
import 'codemirror/mode/javascript/javascript';
import 'codemirror/theme/material.css';
import 'codemirror/lib/codemirror.css';
import './nav.css';

export class Editor extends React.Component{
    state={
        value:'',
    }

    onChange = (editor, data, value) => {
      this.setState({
        code:'',
        console:'',
        stado:false,
      });
    };
    render(){
        return(
            <div className='todo'>
                <h2 style={{backgroundColor:"#27AE60"}}>JOLC Editor</h2>
                <div className="editor">
                  <CodeMirror
                    value={this.state.code}
                    options={{
                      mode: 'javascript',
                      theme: 'material',
                      lineNumbers: true
                    }}
                    onChange={(editor, data, value) => {
                      this.setState({code:value})
                    }}
                  />
                </div>
                <div className="editor">
                  <CodeMirror
                    value={this.state.console}
                    options={{
                      mode: 'javascript',
                      theme: 'material',
                      lineNumbers: true
                    }}
                    onChange={(editor, data, value) => {
                      this.setState({console:value})
                    }}
                  />
                </div>
                   <br></br> 
                <div className="d-grid gap-2">
                  <button className="btn btn-outline-success btn-lg " type="button" onClick={()=>this.compilar()}>Compilar
                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" className="bi bi-window-dock" viewBox="0 0 16 16">
                      <path fillRule="evenodd" d="M15 5H1v8a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V5zm0-1H1V3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v1zm1-1a2 2 0 0 0-2-2H2a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V3z"/>
                      <path d="M3 11.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm4 0a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm4 0a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1z"/>
                    </svg>
                  </button>
                </div>
                <br></br>
            </div>
        );
    }

    compilar(){
      this.setState({estado:true})
      //console.log(jsonEnviar)
      fetch('https://apinuevajeje.herokuapp.com/',{
                method:'POST',
                headers: {"Content-Type":"application/json"},
                body:JSON.stringify({"code":this.state.code})
              }).then(async response =>{
                    const json = await response.json() 
                    //console.log(json)
                    this.setState({console:"es: "+json.mensaje,estado:false})
                  })
    }
    
}