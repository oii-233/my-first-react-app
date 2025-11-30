import React from 'react'

const MovieCard = ({ movie:{ title,vot}}) => {
  return (
    <div>
        <p className='text-white'>{title}</p>
    </div>
  )
}

export default MovieCard