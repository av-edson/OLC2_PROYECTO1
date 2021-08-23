import React from "react";
import { TablaErrores } from "../reportes/TablaErrores";
import { TablaSimbolos } from "../reportes/TablaSimbolos";

export class Resports extends React.Component{

    state={
        noReporte:1,
        tipoReporte:'Tabla de Errores'
    }

    render(){
        return(
            <div >
                <h2 style={{backgroundColor:"#27AE60"}}>Zona de Reportes</h2>
                <h3 style={{backgroundColor:"#27AE60"}}>Actual: {this.state.tipoReporte}</h3>
                <br></br>
                <div className="btn-group btn-group-lg" role="group" aria-label="Basic radio toggle button group">
                  <input type="button" className="btn-check" name="btnradio" id="btnradio1" autoComplete="off"
                  onClick={()=>this.cambio(1)}></input>
                  <label className="btn btn-outline-info" htmlFor="btnradio1">Tabla de Errores</label>

                  <input type="button" className="btn-check" name="btnradio" id="btnradio2" autoComplete="off"
                  onClick={()=>this.cambio(2)}></input>
                  <label className="btn btn-outline-info" htmlFor="btnradio2">Tabla de Simbolos</label>

                  <input type="button" className="btn-check" name="btnradio" id="btnradio3" autoComplete="off"
                  onClick={()=>this.cambio(3)}></input>
                  <label className="btn btn-outline-info" htmlFor="btnradio3">AST</label>
                </div> 
                <br></br>
                <br></br>
                {this.state.noReporte===1 &&
                    <TablaErrores></TablaErrores>
                }   
                {this.state.noReporte=== 2 &&
                    <TablaSimbolos></TablaSimbolos>
                }  
                {this.state.noReporte===3 && 
                    <div>
                        <h2>Gerardo hijo de puta</h2>
                        <div className="card" style={{width: "18rem"}}>
                          <img src="https://scontent.fgua3-2.fna.fbcdn.net/v/t1.18169-9/1385193_523307391084915_997128073_n.jpg?_nc_cat=109&ccb=1-5&_nc_sid=ba80b0&_nc_ohc=ZQ9IUO6vbw4AX8kF7jd&_nc_ht=scontent.fgua3-2.fna&oh=5d7b547aba81e2f97eaf9f667a1ff0ce&oe=61449C0E" className="card-img-top" alt=""></img>
                          <div className="card-body">
                            <h5 className="card-title">Card title</h5>
                          </div>
                        </div>
                    </div>
                }  
                <br></br>       
            </div>
        );
    }

    cambio(a){
        this.setState({noReporte:a})
        switch (a) {
            case 1:
                this.setState({tipoReporte:'Tabla de Errores'})
                break;
            case 2:
                this.setState({tipoReporte:'Tabla de Simbolos'})
                break;
            case 3:
                this.setState({tipoReporte:'AST'})
                break;
            default:
                break;
        }
    }
}