import React, { useState,useEffect } from 'react'
import Search from './components/Search';

TMBD_API_KEY='eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxNWQwM2E3NDA4NjVmYzJiMjE1OGMyNDliNzVjOTM1MyIsIm5iZiI6MTc2NDQ3MjQwMS42ODgsInN1YiI6IjY5MmJiNjUxN2IzODZkYzAxYzI0N2Q5MCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.JJBEMZCXDlkVlviUoe5CtJcG3ykZrP7zAE6poxCiG7k'

const App = () => {
  const [searchTerm, setSearchTerm] = useState('');

  
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