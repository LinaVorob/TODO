import React from 'react';
import axios from 'axios';
import Footer from './components/Footer';
import './components/bootstrap/css/bootstrap.min.css'
import './App.css';
import UserList from './components/User';
import MenuList from './components/Menu';
import ProjectList from './components/Project';
import TodoList from './components/ToDo';
import {BrowserRouter, Route, Switch, Link} from 'react-router-dom';
import LoginForm from './components/Auth';
import Cookies from 'universal-cookie';

const NotFound404 = ({ location }) => {
  return (
  <div>
  <h1>Страница по адресу '{location.pathname}' не найдена</h1>
  </div>
  )
  }

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'menu': [
        {name: 'ToDo', href:'/'},
        {name: 'Проекты', href:'/projects'},
        {name: 'Пользователи', href:'/users'},
      ],
      'users': [],
      'projects': [],
      'todos': [],
      'token': '',
    }
  }

  set_token(token){
      const cookies = new Cookies()
      cookies.set('token', token)
      localStorage.setItem('token', token)
      this.setState({'token': token}, () => this.load_data())
  }

  get_token(login, password){
    axios.post('http://127.0.0.1:8000/api-token-auth/', {username: login, password:password})
      .then(response => {
        this.set_token(response.data['token'])
        }).catch(error => alert("Неверный пароль"))
  }

  get_headers(){
    let headers = {
      'Content-Type': 'application/json',
    }
    if (this.is_authenticated()) {
      headers['Authorization'] = 'Token '+this.state.token
    }
    return headers
  }

  is_authenticated(){
    return this.state.token != ''
  }

  logout(){
    this.set_token('')
  }

  get_token_from_storage(){
    const cookie = new Cookies()
    const token = cookie.get('token')
    this.setState({'token': token}, () => this.load_data())
  }

  load_data(){
    const headers = this.get_headers()
    axios.get('http://127.0.0.1:8000/users', {headers})
      .then(response => {
        const users = response.data.results
          this.setState(
            {
              'users': users
            }
          )
      }).catch(error => console.log(error))

    axios.get('http://127.0.0.1:8000/projects', {headers})
      .then(response => {
        const projects = response.data.results
          this.setState(
            {
              'projects': projects
            }
          )
      }).catch(error => console.log(error))

    axios.get('http://127.0.0.1:8000/todo', {headers})
      .then(response => {
        const todos = response.data.results
          this.setState(
            {
              'todos': todos
            }
          )
      }).catch(error => console.log(error))
  }

  componentDidMount(){
    this.get_token_from_storage()
        
  }

  render () {
    return (
      <div class='App'>
        <body>
        <div>
          <BrowserRouter>
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
              <div class="container-fluid">
                  <a class="navbar-brand" href="/">TODO</a>
                  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                      <span class="navbar-toggler-icon"></span>
                  </button>
                  <div class="collapse navbar-collapse" id="navbarNav">
                  <ul class="navbar-nav">
                    
                    <MenuList items={this.state.menu}/>
                    <il>
                      {this.is_authenticated() ? <button onClick={() => this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                    </il>
                  </ul>
                </div>
            </div>
        </nav>
            <Switch>
              <Route exact path='/' component={() => <TodoList todos={this.state.todos} />} />
              <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} />} />
              <Route exact path='/users' component={() => <UserList users={this.state.users} />} />
              <Route exact path='/login' component={() => <LoginForm get_token={(login, password) => this.get_token(login, password)}/>} />
              <Route component={NotFound404} />
            </Switch>
        </BrowserRouter>
        </div>  
        </body>
        <Footer/>
      </div>
    )
  }
}

export default App;
