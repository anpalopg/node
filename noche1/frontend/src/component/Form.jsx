import React, { useState } from 'react';

import "./styles.css"

const Form = () => {
    const [formData, setFormData] = useState(
        {
            nombre: '',
            email: ''

        }
    )
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({ ...prev, [name]: value }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(formData);
    }

    return (
        <form onSubmit={handleSubmit}>
            <h2> Datos</h2>
            <label>
                nombre
                <input type=' text' name="nombre" value={formData.nombre} onChange={handleChange}></input>
            </label>
            <label>
                correo
                <input type=' text' email="nombre" value={formData.email} onChange={handleChange}></input>
            </label>
            <button type='submit'>Enviar </button>
            <button type='submit'>Cancelar</button>



        </form >

    );








};

export default Form;