function Sidebar() {
  return (
    <div className="w-64 bg-white shadow-md p-5">
      <h2 className="text-xl font-bold mb-4 text-blue-700">
        Features
      </h2>

      <ul className="space-y-3">
        <li>💬 AI Chat</li>
        <li>🩺 Symptom Checker</li>
        <li>📋 Health Reports</li>
        <li>📊 Disease Prediction</li>
      </ul>
    </div>
  );
}

export default Sidebar;