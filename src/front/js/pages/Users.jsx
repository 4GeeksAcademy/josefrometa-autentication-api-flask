import React, { useContext, useEffect, useState } from "react"
import { Context } from "../store/appContext"
import { Navigate } from "react-router-dom"


const Users = () => {
    const { store, actions } = useContext(Context)




    useEffect(() => {
        actions.getUser()
    }, [])


    return (
        <>
            {
                store.token == null ?
                    <Navigate to={"/login"} /> :
                    <>
                    <div className="container">
                        <h1 className="m-5">Registered Users</h1>
                        {store.users.map((item) => {
                            return (
                                <p className="border rounded border-primary p-2">{item.email}</p>
                            )
                        })}
                    </div>
                    </>
            }
        </>
    )
}


export default Users