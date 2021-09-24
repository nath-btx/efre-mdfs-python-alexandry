import React, { useState } from "react"


export default function BookCard(props){

    const addBook = () => {        
        var myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");
        
        var raw = JSON.stringify({
          "title": title,
          "author": author,
          "description": description
        });
        
        var requestOptions = {
          method: 'POST',
          headers: myHeaders,
          body: raw,
          redirect: 'follow'
        };
        
        fetch("http://localhost:8000/api/addBook", requestOptions)
          .then(response => response.text())
          .then(result => console.log(result))
          .catch(error => console.log('error', error));
        window.location.reload(false);
    }

    const [title, setTitle] = useState("")
    const [author, setAuthor] = useState("")
    const [description, setDescription] = useState("")



    return(
        <div key={props.id} className="mission-card">
            <div className="card-body">
                <div className="upper">
                    <form>
                        <label>
                            Titre :
                            <input type="text" name="title" value={title} onChange={(e) => setTitle(e.target.value)} />
                        </label>
                        <input type="text" name="title" value={author} onChange={(e) => setAuthor(e.target.value)} />
                        <input type="text" name="title" value={description} onChange={(e) => setDescription(e.target.value)} />


                        <input type="submit" onClick={() => addBook} />
                    </form>
                </div>
            </div>
        </div>
    )
}