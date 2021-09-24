import React, { useEffect, useState } from "react"

export default function CardView(){


    
    const [books, setBooks] = useState([])
    useEffect(() => {
        getBooks()
        console.log(books)
    })
    let getBooks = () =>{
        fetch('http://localhost:8000/api/getBooks').then(
            response => response.json()).then(
                resData => {
                    console.log(resData)
                }
            
        )
    }
    return(
        <p>hello</p>
    )

}
