import React from 'react';
import { NavLink } from 'react-router-dom';
import './Navigator.css';
import logoImage from '../../assets/budget_fox.png'; // Adjust the path based on your file structure

const Navigator = () => {
    return (
        <nav className="navigator">
            <div className="logo">
                <img src={logoImage} alt="Logo" className="logo-img" />
            </div>
            <ul className="nav-links">
                <li><NavLink to="/index/dashboard" activeClassName="active">Dashboard</NavLink></li>
                <li><NavLink to="/index/profile" activeClassName="active">Profile</NavLink></li>
                <li><NavLink to="/index/subscribe" activeClassName="active">Subscribe</NavLink></li>
                <li><NavLink to="/accounts/logout/" activeClassName="active">Logout</NavLink></li>
            </ul>
        </nav>
    );
};

export default Navigator;
