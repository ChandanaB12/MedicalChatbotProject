import React, { useState } from "react";
import axios from "axios";
import { useNavigate,Link } from "react-router-dom";

function Register() {
    <p className="text-center mt-4">
  Already have an account?{" "}
  <Link to="/" className="text-green-600 font-semibold">
    Login
  </Link>
</p>

  const navigate = useNavigate();

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async () => {

    try {

      const res = await axios.post("https://medicalchatbotproject.onrender.com/register"), {
        name,
        email,
        password
      };

      alert(res.data.message);

      if (res.data.message === "Registration Successful") {
        navigate("/");
      }

    } catch (error) {
      alert("Registration Failed");
      console.log(error);
    }

  };

  return (

    <div className="flex justify-center items-center min-h-screen bg-gray-100">

      <div className="bg-white shadow-lg rounded-xl p-8 w-96">

        <h2 className="text-3xl font-bold text-center text-green-700 mb-6">
          Register
        </h2>

        <input
          type="text"
          placeholder="Full Name"
          className="w-full border p-3 rounded-lg mb-4"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <input
          type="email"
          placeholder="Email"
          className="w-full border p-3 rounded-lg mb-4"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="password"
          placeholder="Password"
          className="w-full border p-3 rounded-lg mb-4"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button
          onClick={handleRegister}
          className="w-full bg-green-600 text-white p-3 rounded-lg"
        >
          Register
        </button>

      </div>

    </div>

  );

}

export default Register;