import React from "react";
import CodeMirror from '@uiw/react-codemirror';
import 'codemirror/keymap/sublime';
import 'codemirror/theme/monokai.css';
import './nav.css';

export class Editor extends React.Component{
    state={
        code:'const a = \'Gerardo Hueco\';',
        console:''
    }

    render(){
        return(
            <div className='todo'>
                <h2 style={{backgroundColor:"#27AE60"}}>JOLC Editor</h2>
                <div className='editor'>
                  <h5>Input</h5>
                  <CodeMirror
                    value={this.state.code}
                  lazyLoadMode={true}
                  options={{
                    theme: 'monokai',
                    tabSize: 2,
                    keyMap: 'sublime',
                    mode: 'js',
                    }}
                  />
                </div>
                <div className='editor'>
                  <h5>Input</h5>
                  <CodeMirror
                    value={this.state.console}
                    lazyLoadMode={false}
                    options={{
                      theme: 'monokai',
                      tabSize: 2,
                      keyMap: 'sublime',
                      mode: 'js',
                    }}
                  />
                </div>
                   <br></br> 
                <div class="d-grid gap-2">
                  <button class="btn btn-outline-success btn-lg " type="button">Compilar
                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-window-dock" viewBox="0 0 16 16">
                      <path fill-rule="evenodd" d="M15 5H1v8a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V5zm0-1H1V3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v1zm1-1a2 2 0 0 0-2-2H2a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V3z"/>
                      <path d="M3 11.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm4 0a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm4 0a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1z"/>
                    </svg>
                  </button>
                </div>
                <br></br>
            </div>
        );
    }
}