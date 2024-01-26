import React, { useState, useContext } from "react";
import { Context } from "../store/appContext";
import { Navigate, useNavigate } from "react-router-dom";

const Signup = () => {
    const navigate = useNavigate();
    const { actions } = useContext(Context);
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleSignUp = async (event) => {
        event.preventDefault();
        const user = { email, password };
        const response = await actions.registerUser(user);
        console.log(user);
        if (response) {
            navigate("/login");
        }
        console.log(response);
    };

    return (
        <form className="container" onSubmit={handleSignUp}>
            <h1 className="m-2 p-2">Sign Up</h1>
            <label>Email</label>
            <input
                type="text"
                placeholder="Email"
                className="form-control border border-rounded"
                name="email"
                value={email}
                onChange={(event) => setEmail(event.target.value)}
            />
            <label>Password</label>
            <input
                type="password"
                placeholder="Password"
                className="form-control border border-rounded"
                name="password"
                value={password}
                onChange={(event) => setPassword(event.target.value)}
            />
            <button className="m-2 btn btn-success">Sign Up</button>
        </form>
    );
};

export default Signup;
