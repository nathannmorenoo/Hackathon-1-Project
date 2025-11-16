import React from 'react'
import { useState, useEffect } from 'react'

function Login() {
  const [username, setUsername] = useState("Guest");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {
  e.preventDefault();

  // this url is for the backend, not frontend 
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
   <div className='h-screen bg-cover flex items-center justify-center' style={{backgroundImage: "url('https://wallpaperswide.com/download/pixel_art-wallpaper-2560x1440.jpg')" }}>
     <div className=''>
       <div className="flex-1"></div>
       <h2 className='text-red-500 font-extrabold font-extrabold text-3xl'>SDSU</h2>
       <h3 className='font-black text-8xl opacity-80'>THRIVE</h3>
     </div>
     <div className="ml-60"></div>
     <div className='w-80 bg-white opacity-50 rounded-xl p-8 m-10 '>
       <form className="" action="" onSubmit={handleSubmit}>
         <input className="border-2 p-1 rounded mb-3" type="text" placeholder='Username' onChange={(e) => setUsername(e.target.value)} />
         <input className="border-2 p-1 rounded mb-3" type="text" placeholder='Email' onChange={(e) => setEmail(e.target.value)} />
         <input className="border-2 p-1 rounded mb-3" type="text" placeholder='Password' onChange={(e) => setPassword(e.target.value)} />
         <button className='border-2 p-1 rounded transition mx-auto flex hover: cursor-pointer' type='submit'>Login</button>
       </form>
     </div>
   </div>
 )
}

export default Login