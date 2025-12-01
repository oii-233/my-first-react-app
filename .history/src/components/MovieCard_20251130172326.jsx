import React from 'react'

const MovieCard = ({ movie:{ title,vote_average, poster_path, release_data, original_language}}) => {
  return (
    <div className='movie-card'>
        <img src={poster_path ? 'https://image.tmdb.org/t/p/w500/${poster_path}'}/>
    </div>
  )
}

export default MovieCard