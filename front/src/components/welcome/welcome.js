import React from "react";

export class Welcome extends React.Component{

    render () {
        return(
            <div>
                <div className="card" style={{width: "18rem"}}>
                  <img src="https://scontent.fgua3-1.fna.fbcdn.net/v/t1.6435-9/215278960_4096888383721957_5057494979382707356_n.jpg?_nc_cat=100&ccb=1-5&_nc_sid=09cbfe&_nc_ohc=Im-Xfz58YFAAX872kt9&_nc_ht=scontent.fgua3-1.fna&oh=843959fcfa9ce058bbf1a6ca623cbc01&oe=6142E83F" alt="" className="card-img-top"></img>
                  <div className="card-body">
                    <h5 className="card-title">Edson Avila</h5>
                    <p className="card-text">201902302
                        Compiladores 2 Seccion C
                        Proyecto 1
                    </p>
                  </div>
                </div>
            </div>
        );
    }
}