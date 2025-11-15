import React from 'react'
import { useState, useEffect } from 'react'

function Login() {
  const [username, setUsername] = useState("Guest");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {
  e.preventDefault();

  try {
    const response = await fetch("http://localhost:8000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username,
        email,
        password,
      }),
    });

    const data = await response.json();
    console.log("Backend Response:", data);
  } catch (err) {
    console.error("Fetch error:", err);
  }
};

  return (
    <div className='border'>
      <div>
        <h2 className='text-red-500 font-extrabold'>SDSU</h2>
        <h3 className='font-extrabold font-black'>THRIVE</h3>
      </div>
      <div>
        <form action="" onSubmit={handleSubmit}>
          <input className="border-2" type="text" placeholder='Username' onChange={(e) => setUsername(e.target.value)} />
          <input className="border-2" type="text" placeholder='Email' onChange={(e) => setEmail(e.target.value)} />
          <input className="border-2" type="text" placeholder='Password' onChange={(e) => setPassword(e.target.value)} />
          <button className='border-2' type='submit'>Login</button>
        </form>
      </div>
    </div>
  )
}

export default Login