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
                <h2>JOLC Editor</h2>
                <div className='editor'>
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
            </div>
        );
    }
}