import React from "react";
import './bootstrap/css/bootstrap.min.css'
import { Link } from "react-router-dom";

const MenuItem = ({item}) => {
    return (

        <li class="nav-item">
          <Link to={item.href} class="nav-link active" aria-current="page">{item.name}</Link>
        </li>
    )
}

const MenuList = ({items}) => {
    return (
        items.map((item) => <MenuItem item={item} />)
    )
}

export default MenuList;