import React, {useEffect, useState} from 'react';
import axios from "axios";

const App = () => {
    const [pizzas,setPizzas]=useState
    useEffect(() => {
        axios.get('/api/pizzas').then(({data})=> {
            setPizzas(data.data)
        }
        )
    }, []);
    return (
        <div>
            {
                pizzas.map(pizza=><div key={pizza.id}><h>{pizza.name}</h><p>{pizza.price}</p><p>{pizza.size}</p></div>)
            }
        </div>
    );
};

export {App};