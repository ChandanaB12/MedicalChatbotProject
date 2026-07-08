import { useNavigate } from "react-router-dom";

function Navbar() {

  const navigate = useNavigate();

  const user = localStorage.getItem("user");

  const handleLogout = () => {

    localStorage.removeItem("user");

    alert("Logged out successfully");

    navigate("/");
  };

  return (
    <nav className="bg-gradient-to-r from-blue-700 via-blue-600 to-cyan-600 text-white px-8 py-4 shadow-2xl flex justify-between items-center">
      <div>
  <h1 className="text-3xl font-extrabold tracking-wide">
    🩺 AI Healthcare Assistant
  </h1>

  <p className="text-blue-100 text-sm">
    Your Personal Health Companion
  </p>
</div>

      <div className="flex items-center gap-4">

        <div className="bg-white/20 px-4 py-2 rounded-full">
  <span className="font-semibold">
    👤 Welcome, {user}
  </span>
</div>

        <button
          onClick={handleLogout}
          className="bg-red-500 hover:bg-red-600 transition duration-300 px-5 py-2 rounded-xl font-semibold shadow-lg"
        >
          Logout
        </button>

      </div>

    </nav>
  );
}

export default Navbar;