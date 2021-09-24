export default function BookCard(props){

    const remove = (index) => {        
        var myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");
        
        var raw = JSON.stringify({
          "id": index.toString()
        });
        
        var requestOptions = {
          method: 'DELETE',
          headers: myHeaders,
          body: raw,
          redirect: 'follow'
        };
        
        fetch("http://localhost:8000/api/deleteBook", requestOptions)
          .then(response => response.text())
          .then(result => console.log(result))
          .catch(error => console.log('error', error));
        window.location.reload(false);
    }

    return(
        <div key={props.id} className="mission-card">
            <div className="card-body">
                <div className="upper">
                        <div className="icon" onClick={() => remove(props.id)}>
                            <div className="remove"/>
                        </div>
                        <h1>
                            {props.title}                        
                        </h1>
                        <h2>
                            {props.author}
                        </h2>
                        <p className="description">
                            {props.description}
                        </p>
                </div>
            </div>
        </div>
    )
}