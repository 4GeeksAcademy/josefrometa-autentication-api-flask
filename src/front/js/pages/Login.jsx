import React, { useState, useContext } from "react";
import { Context } from "../store/appContext";
import { Navigate, useNavigate } from "react-router-dom";

const Login = () => {
    const navigate = useNavigate();
    const { actions } = useContext(Context);
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = async (event) => {
        event.preventDefault();
        const user = { email, password };
        const result = await actions.login(user);
        console.log(result);
        if (result === 400) {
            alert("Bad credentials");
        }
        if (result === 200) {
            navigate("/private");
        }
    };

    return (
        <div className="container">
            <form onSubmit={handleLogin}>
                <input
                    type="text"
                    placeholder="email"
                    className="form-control border border-rounded"
                    name="email"
                    value={email}
                    onChange={(event) => setEmail(event.target.value)}
                />
                <input
                    type="password"
                    placeholder="password"
                    className="form-control border border-rounded"
                    name="password"
                    value={password}
                    onChange={(event) => setPassword(event.target.value)}
                />
                <button className="btn btn-success">Login</button>
            </form>
        </div>
    );
};

export default Login;
