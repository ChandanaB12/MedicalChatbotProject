import React, { useState } from "react";
import axios from "axios";
import { useNavigate ,Link} from "react-router-dom";

function Login() {
  
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const res = await axios.post("https://medicalchatbotproject.onrender.com/login"), {
        email: email,
        password: password,
      });

      alert(res.data.message);
if (res.data.message === "Login Successful") {

    localStorage.setItem("user", res.data.user);

    alert("Welcome " + res.data.user);

    navigate("/dashboard");
}

    } catch (error) {
      alert("Login Failed");
      console.log(error);
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">

      <div className="bg-white shadow-lg rounded-xl p-8 w-96">

        <h2 className="text-3xl font-bold text-center text-blue-700 mb-6">
          Login
        </h2>

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
          onClick={handleLogin}
          className="w-full bg-blue-600 text-white p-3 rounded-lg"
        >
          Login
        </button>

<p className="text-center mt-4">
  Don't have an account?{" "}
  <Link to="/register" className="text-blue-600 font-semibold">
    Register
  </Link>
</p>
      </div>

    </div>
  );
}

export default Login;