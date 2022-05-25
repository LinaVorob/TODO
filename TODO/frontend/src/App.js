import React from 'react';
import axios from 'axios';
import Footer from './components/Footer';
import './App.css';
import UserList from './components/User';
import MenuList from './components/Menu';
import ProjectList from './components/Project';
import TodoList from './components/ToDo';
import {HashRouter, Route, Switch} from 'react-router-dom';


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
      'todos': []
    }
  }


  componentDidMount(){
    axios.get('http://127.0.0.1:8000/users')
      .then(response => {
        const users = response.data.results
          this.setState(
            {
              'users': users
            }
          )
      }).catch(error => console.log(error))
    axios.get('http://127.0.0.1:8000/projects')
      .then(response => {
        const projects = response.data.results
          this.setState(
            {
              'projects': projects
            }
          )
      }).catch(error => console.log(error))
    axios.get('http://127.0.0.1:8000/todo')
      .then(response => {
        const todos = response.data.results
          this.setState(
            {
              'todos': todos
            }
          )
      }).catch(error => console.log(error))
        
  }

  render () {
    return (
      <div class='App'>
        <body>
        <div>
          <HashRouter>
            <MenuList items={this.state.menu}/>
            <Switch>
              <Route exact path='/' component={() => <TodoList todos={this.state.todos} />} />
              <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} />} />
              <Route exact path='/users' component={() => <UserList users={this.state.users} />} />
              <Route component={NotFound404} />
            </Switch>
        </HashRouter>
        </div>  
        </body>
        <Footer/>
      </div>
    )
  }
}

export default App;
