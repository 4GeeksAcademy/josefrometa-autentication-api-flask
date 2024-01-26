import React from "react";
import { Link } from "react-router-dom";

export const Navbar = () => {
	return (
		<nav className="navbar navbar-light bg-light">
			<div className="container">
				<Link to="/">
					<span className="navbar-brand mb-0 h1">React Boilerplate</span>
				</Link>
				<div className="ml-auto">
				<Link to="/signup">
						<button className="btn btn-primary">Signup</button>
					</Link>
					<Link to="/private">
						<button className="btn btn-success ms-3">Private</button>
					</Link>
					<button className="btn btn-danger ms-3" onClick={()=>{actions.logout()}}>
						Logout
					</button>
				</div>
			</div>
		</nav>
	);
};
