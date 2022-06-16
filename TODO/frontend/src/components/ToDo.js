import React from "react";
import './bootstrap/css/bootstrap.min.css';
import {Link} from 'react-router-dom';

const TodoItem = ({todo, deleteTodo}) => {
    return (
        <tr>
            <td>
                {todo.project.name}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.author.username}
            </td>
            <td>
                {todo.users}
            </td>
            <td>
                {todo.status}
            </td>
            <td>
                {todo.updated_at}
            </td>
            <td>
                <button onClick={() => deleteTodo(todo.uuid)} type='button'>X</button>
            </td>
        </tr>
    )
}

const TodoList = ({todos, deleteTodo}) => {
    return (
        <div>
        <table class="table .table-bordered">
            <thead class="table-light">
                <th>
                    Project
                </th>
                <th>
                    Text
                </th>
                <th>
                    Author
                </th>
                <th>
                    Users
                </th>
                <th>
                    Status
                </th>
                <th>
                    Updated
                </th>
                <th></th>
            </thead>
            <tbody>
            {todos.map((todo) => <TodoItem todo={todo} deleteTodo={deleteTodo}/>)}
            </tbody>
        </table>
         <Link to='/todo/create/'>Create new todo</Link>
        </div>
    )
}

export default TodoList;