import React, { Component } from 'react';
import {getMovies} from '../services/fakeMovieService';
import ListGroup from './common/listGroup';
import Pagination from './common/pagination';
import { paginate } from '../utils/paginate';
import { getGenres } from '../services/fakeGenreService';
import MoviesTable from './moviesTable';
import _ from 'lodash';

class Movies extends Component {
    state = { 
        movies : [],
        genres: [],
        pageSize : 4,
        currentPage : 1,
        sortColumn:{ path :'title', order:'asc'}
    };

    componentDidMount() {
        const genres = [{_id:"",name:'AllGenres'}, ...getGenres()]
        this.setState({movies: getMovies(), genres: genres});
    }

    handleGenreSelect = genre =>{
       this.setState({selectedGenre:genre, currentPage:1});
    }

    handleDelete = (movie) => {
        const movies = this.state.movies.filter(m =>m._id !== movie._id);
        this.setState({movies});
    };

    handleLike = movie => {
        const movies = [...this.state.movies];
        const index = movies.indexOf(movie);
        movies[index]={...movies[index]};
        movies[index].liked=!movies[index].liked;
        this.setState({movies});
    };

    handlePageChange = page => {
        this.setState({currentPage:page});
    };

    handleSort = sortColumn => {
        
        this.setState({sortColumn});
    };

    

    render() { 
        const {length: count} = this.state.movies;
        const{pageSize,currentPage, movies:allMovies, selectedGenre, sortColumn} = this.state;

        if(count===0 ) 
            return <h6 className="m-3">There are no movies in the database</h6>
        
        const filtered = selectedGenre && selectedGenre._id ? allMovies.filter(
            m=>m.genre._id===selectedGenre._id
        ):allMovies;

        const sorted= _.orderBy(filtered,[sortColumn.path], [sortColumn.order]);
        const movies =paginate(sorted,currentPage,pageSize);
        return ( 

            <div>
                 <h6 className="m-4">Showing {filtered.length} movies in the database</h6>
            
            <div className="row">
            <div className="col-2 m-4">
                    <ListGroup 
                        selectedItem={this.state.selectedGenre}
                        items={this.state.genres}
                        onItemSelect={this.handleGenreSelect} />
            </div>
            <div className="col">
            <MoviesTable
                movies={movies}
                onLike={this.handleLike}
                onDelete={this.handleDelete}
                onSort={this.handleSort}
                sortColumn={sortColumn}
            />

            <div className="m-3">
            <Pagination currentPage={currentPage} itemsCount ={filtered.length}
                pageSize={pageSize}
                onPageChange={this.handlePageChange}
            />
            </div>
            </div> 
            </div>
            
        </div>

        );
    }
}
 
export default Movies ;


// Random comment