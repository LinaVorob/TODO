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
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container-fluid">
                <a class="navbar-brand" href="/">TODO</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    {items.map((item) => <MenuItem item={item} />)}
                </ul>
                </div>
            </div>
        </nav>
    )
}

export default MenuList;