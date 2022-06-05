import React from "react";
import './bootstrap/css/bootstrap.min.css'

const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                {user.username}
            </td>
            <td>
                {user.firstname}
            </td>
            <td>
                {user.lastname}
            </td>
            <td>
                {user.email}
            </td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table class="table .table-bordered">
            <thead class="table-light">
                <th>
                    Username
                </th>
                <th>
                    First name
                </th>
                <th>
                    Last name
                </th>
                <th>
                    Email
                </th>
            </thead>
            {users.map((user) => <UserItem user={user} />)}
        </table>
    )
}

export default UserList;