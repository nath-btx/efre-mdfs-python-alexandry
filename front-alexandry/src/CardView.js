import React, { useEffect, useState } from "react"
import BookCard from "./BookCard"

export default function CardView(){    
    const [books, setBooks] = useState([])
    useEffect(() => {
        getBooks()
        // eslint-disable-next-line react-hooks/exhaustive-deps
    },[])
    const getBooks = async () => {
        console.log('hello')
        fetch('http://localhost:8000/api/getBooks').then(
            response => response.json()).then(
                resData => {
                    setBooks(resData)
                }
            
        )
    }
    return(
        <div className="cards">
            {books === [] ? (
                <div>
                </div>
            ) : (
                <div className="cards-list">
                    {books.map((book, index) =>
                            <BookCard 
                                key={index}
                                id={book[0]}
                                title={book[1]}
                                author={book[2]}
                                description={book[3]}
                            />
                    )}     
                </div>

            )}
        </div>

    )

}
