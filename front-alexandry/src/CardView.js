import React, { useEffect, useState } from "react"
import DotLoader from "react-spinners/DotLoader"
export default function CardView(){


    
    const [books, setBooks] = useState([])
    useEffect(() => {
        getBooks()
        // eslint-disable-next-line react-hooks/exhaustive-deps
    },[])

    const getBooks = async () => {
        fetch('http://localhost:8000/api/getBooks').then(
            response => response.json()).then(
                resData => {
                    setBooks(resData)
                }
            
        )
    }
    return(
        <div className="">
            {books === [] ? (
                <div>
                </div>
            ) : (
                <div>
                    {books.map((book, index) => 
                        <div className="">
                        </div>
                    )}        
                </div>

            )}
        </div>

    )

}
