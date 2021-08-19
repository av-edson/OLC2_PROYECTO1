import React  from "react";

export class TablaSimbolos extends React.Component{

    render(){
        return(
            <div className="resultados">
          <table className="table table-striped table-hover table-light">
          <thead>
            <tr>
            <th scope="col">##</th>
              <th scope="col">Jugador</th>
              <th scope="col">Tier</th>
              <th scope="col">P 10</th>
              <th scope="col">P 5</th>
              <th scope="col">P 3</th>
              <th scope="col">P 0</th>
              <th scope="col"> Total</th>
              <th scope="col">Incremento</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td >...</td>
              <td >...</td>
              <td >...</td>
              <td >...</td>
              <td >...</td>
              <td >...</td>
              <td >...</td>
              <td >...</td>
              <td >...</td>
            </tr>
          </tbody>
          </table>
        </div> 
        );
    }
}