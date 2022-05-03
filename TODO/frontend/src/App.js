import React from 'react';
import axios from 'axios';
import Footer from './components/Footer';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User';
import MenuList from './components/Menu';


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'menu': [
        {name: 'Главная', href:'/'},
        {name: 'Просмотр дел', href:'/'},
        {name: 'Пользователи', href:'#'},
        {name: 'О нас', href:'#'}
      ],
      'users': []
    }
  }


  componentDidMount(){
    axios.get('http://127.0.0.1:8000/users')
      .then(response => {
        const users = response.data
          this.setState(
            {
              'users': users
            }
          )
      }).catch(error => console.log(error))
  }

  render () {
    return (
      <div>
        <header>
          <MenuList items={this.state.menu}/>
        </header>
        <body>
          <div>
            <UserList users={this.state.users} />
          </div>
        </body>
        <Footer/>
      </div>
    )
  }
}

export default App;
