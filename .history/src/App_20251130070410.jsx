import React, { useState,useEffect } from 'react'
import Search from './components/Search';

const API_BASE_URL = 'https://api.themoviedb.org/3/discover/movie';
const VITE_TMDB_API_KEY = import.meta.env.VITE_TMDB_API_KEY;

const API_OPTIONS = {
  method: "GET",
  headers: {
    accept: 'application/json',
    Autorization: 'Bearer ${API_KEY}'
  }
}


const App = () => {
  const [searchTerm, setSearchTerm] = useState('');

  const fetchMovies = async () =>{}
  return (
    <main>
      <div className=' pattern'/>
       <div className='wrapper'>
        <header>
          <img src='./hero.png' alt='Hero Banner'/>
          <h1>Find <span className='text-gradient'>Movies</span> You'll Enjoy Without the Hasstle</h1>
        </header>
        <Search searchTerm={searchTerm} setSearchTerm={setSearchTerm}/>
       </div> 
      
    </main>
     
  )
}

export default App