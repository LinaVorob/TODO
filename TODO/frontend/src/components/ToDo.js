import React from "react";
import './bootstrap/css/bootstrap.min.css'

const TodoItem = ({todo}) => {
    return (
        <tr>
            <td>
                {todo.project}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.author}
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
        </tr>
    )
}

const TodoList = ({todos}) => {
    return (
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
            </thead>
            <tbody>
            {todos.map((todo) => <TodoItem todo={todo} />)}
            </tbody>
        </table>
    )
}

export default TodoList;