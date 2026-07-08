import { useNavigate } from "react-router-dom";

function Dashboard() {

  const navigate = useNavigate();

  const user = localStorage.getItem("user");

  return (

    <div className="min-h-screen bg-gray-100 p-8">

      <h1 className="text-4xl font-bold text-blue-700">
        🩺 AI Healthcare Assistant
      </h1>

      <h2 className="text-2xl mt-4">
        👋 Welcome, {user}
      </h2>

      <div className="grid grid-cols-2 gap-6 mt-8">

  <div className="bg-white shadow-lg rounded-xl p-6 text-center">
    <h2 className="text-3xl">💬</h2>
    <h3 className="font-bold mt-2">Total Chats</h3>
    <p className="text-blue-700 text-2xl mt-2">0</p>
  </div>

  <div className="bg-white shadow-lg rounded-xl p-6 text-center">
    <h2 className="text-3xl">❤️</h2>
    <h3 className="font-bold mt-2">Health Tip</h3>
    <p className="mt-2 text-sm">
      Drink at least 2–3 litres of water every day.
    </p>
  </div>

  <div className="bg-white shadow-lg rounded-xl p-6 text-center">
    <h2 className="text-3xl">🏥</h2>
    <h3 className="font-bold mt-2">Hospitals</h3>
    <p className="mt-2 text-sm">
      Find Nearby Hospitals
    </p>
  </div>

  <div className="bg-white shadow-lg rounded-xl p-6 text-center">
    <h2 className="text-3xl">👤</h2>
    <h3 className="font-bold mt-2">My Profile</h3>
    <p className="mt-2 text-sm">
      View Profile
    </p>
  </div>

</div>

      <div className="flex gap-4 mt-8">

        <button
          onClick={() => navigate("/home")}
          className="bg-blue-600 text-white px-6 py-3 rounded-lg"
        >
          🩺 Start New Chat
        </button>

        <button
          onClick={() => navigate("/profile")}
          className="bg-green-600 text-white px-6 py-3 rounded-lg"
        >
          👤 My Profile
        </button>

      </div>

    </div>

  );

}

export default Dashboard;