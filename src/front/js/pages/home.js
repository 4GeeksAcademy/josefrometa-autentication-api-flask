import React, { useContext } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";

export const Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="d-flex justify-content-center align-items-center" style={{ height: "70vh" }}>
			<h1 className="display-1">Authentication System</h1>
		</div>

	);
};
