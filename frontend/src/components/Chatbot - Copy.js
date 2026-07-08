import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import { jsPDF } from "jspdf";
import SpeechRecognition, {
  useSpeechRecognition,
} from "react-speech-recognition";

function Chatbot() {

  const [symptom, setSymptom] = useState("");
  const [messages, setMessages] = useState([]);
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const [showHistory, setShowHistory] = useState(false);

  const {
    transcript,
    listening,
    resetTranscript,
    browserSupportsSpeechRecognition,
  } = useSpeechRecognition();

  const messagesEndRef = useRef(null);

  // Load Chat History
  const loadHistory = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:8000/history");
      setHistory(res.data);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    loadHistory();
  }, []);

  useEffect(() => {
    if (transcript) {
      setSymptom(transcript);
    }
  }, [transcript]);

 useEffect(() => {
  messagesEndRef.current?.scrollIntoView({
    behavior: "smooth",
  });
}, [messages]);

// Download PDF Report
const downloadReport = (msg) => {
    const doc = new jsPDF();

    const currentDate = new Date();

    doc.setFontSize(20);
    doc.text("Healthcare AI Medical Report", 20, 20);

    doc.setFontSize(11);
    doc.text(`Date: ${currentDate.toLocaleDateString()}`, 20, 35);
    doc.text(`Time: ${currentDate.toLocaleTimeString()}`, 20, 45);

    let y = 60;

    doc.text(`Symptoms: ${msg.user}`, 20, y);
    y += 10;

    doc.text(`Disease: ${msg.response.prediction}`, 20, y);
    y += 10;

    doc.text(`Specialist: ${msg.response.specialist || "-"}`, 20, y);
    y += 10;

    doc.text(`Severity: ${msg.response.severity}`, 20, y);
    y += 15;

    doc.text("Description:", 20, y);
    y += 10;

    doc.text(msg.response.description || "-", 20, y);
    y += 15;

    doc.text("Medical Suggestions:", 20, y);

    if (msg.response.medical_suggestion) {
      msg.response.medical_suggestion.forEach((item) => {
        y += 8;
        doc.text("- " + item, 25, y);
      });
    }

    y += 15;
    doc.text("Recommended Medicines:", 20, y);

    if (msg.response.medicine) {
      msg.response.medicine.forEach((medicine) => {
        y += 8;
        doc.text("- " + medicine, 25, y);
      });
    }

    y += 15;
    doc.text("Diet Recommendation:", 20, y);

    if (msg.response.diet) {
      msg.response.diet.forEach((food) => {
        y += 8;
        doc.text("- " + food, 25, y);
      });
    }

    y += 15;
    doc.text("Precautions:", 20, y);

    if (msg.response.precaution) {
      msg.response.precaution.forEach((item) => {
        y += 8;
        doc.text("- " + item, 25, y);
      });
    }

    doc.save("Medical_Report.pdf");

  };
  

  // Predict Disease
  const handlePredict = async () => {

    if (!symptom.trim()) return;

    setLoading(true);

    try {

      const res = await axios.post(
        "http://127.0.0.1:8000/predict",
        {
          symptom: symptom,
        }
      );

      setMessages((prev) => [
        ...prev,
        {
          user: symptom,
          response: res.data,
        },
      ]);

      setSymptom("");

      loadHistory();

    } catch (error) {

      console.log(error);

    }

    setLoading(false);

  };

  return (
   
  <div className="flex-1 bg-white/90 backdrop-blur-md rounded-3xl shadow-2xl border border-blue-100 p-6 flex flex-col">

    <div className="flex justify-between items-start mb-6">

      <div>
        <h2 className="text-4xl font-extrabold text-blue-700 tracking-wide">
          🩺 Healthcare AI Chatbot
        </h2>

        <p className="text-gray-500 text-sm">
          AI Powered Healthcare Assistant
        </p>
      </div>

      <div className="flex gap-2">

        <button
          onClick={() => setShowHistory(!showHistory)}
          className="bg-green-600 text-white px-4 py-2 rounded-lg"
        >
          {showHistory ? "❌ Hide History" : "📜 View History"}
        </button>

        <button
          onClick={() => setMessages([])}
          className="bg-red-500 text-white px-4 py-2 rounded-lg"
        >
          Clear Chat
        </button>

      </div>

    </div>

    <div className="flex-1 overflow-y-auto mb-4">

     {loading && (
  <div className="flex items-center gap-4 bg-blue-50 border border-blue-200 rounded-2xl p-4 mb-4 shadow">

    <div className="animate-spin rounded-full h-8 w-8 border-4 border-blue-600 border-t-transparent"></div>

    <div>

      <h3 className="font-bold text-blue-700">
        🤖 AI Doctor is analyzing...
      </h3>

      <p className="text-gray-600 text-sm">
        Please wait while we analyze your symptoms.
      </p>

    </div>

  </div>
)} 

      {messages.length === 0 ? (

       <div className="bg-gradient-to-br from-blue-50 via-cyan-50 to-white border border-blue-200 rounded-3xl p-8 shadow-xl">

  <div className="text-center">

    <div className="text-6xl mb-4">
      🩺
    </div>

    <h2 className="text-3xl font-extrabold text-blue-700">
      Welcome to AI Healthcare Assistant
    </h2>

    <p className="text-gray-600 mt-3 text-lg">
      Your smart healthcare companion for quick symptom analysis and medical guidance.
    </p>

  </div>

  <div className="grid grid-cols-2 gap-4 mt-8">

    <div className="bg-white rounded-2xl p-4 shadow text-center">
      <div className="text-3xl">🩺</div>
      <p className="font-semibold mt-2">Disease Prediction</p>
    </div>

    <div className="bg-white rounded-2xl p-4 shadow text-center">
      <div className="text-3xl">👨‍⚕️</div>
      <p className="font-semibold mt-2">Specialist</p>
    </div>

    <div className="bg-white rounded-2xl p-4 shadow text-center">
      <div className="text-3xl">💊</div>
      <p className="font-semibold mt-2">Medicines</p>
    </div>

    <div className="bg-white rounded-2xl p-4 shadow text-center">
      <div className="text-3xl">🥗</div>
      <p className="font-semibold mt-2">Diet Plan</p>
    </div>

    <div className="bg-white rounded-2xl p-4 shadow text-center">
      <div className="text-3xl">🏥</div>
      <p className="font-semibold mt-2">Hospitals</p>
    </div>

    <div className="bg-white rounded-2xl p-4 shadow text-center">
      <div className="text-3xl">🚨</div>
      <p className="font-semibold mt-2">Emergency Alert</p>
    </div>

  </div>

  <div className="mt-8 bg-green-50 border border-green-200 rounded-2xl p-4">

    <h3 className="text-green-700 font-bold">
      💡 Daily Health Tip
    </h3>

    <p className="text-gray-700 mt-2">
      Drink enough water, eat a balanced diet, exercise regularly, and consult a doctor if symptoms persist.
    </p>

  </div>

  <p className="text-center text-gray-500 mt-6">
    👇 Enter your symptoms below to get started.
  </p>

</div> 


      ) : (

        messages.map((msg, index) => (

          <div key={index} className="mb-6">

           <div className="flex justify-end mb-4">

  <div className="max-w-md">

    <p className="text-right text-sm text-gray-500 mb-1">
      👤 You
    </p>

    <div className="bg-gradient-to-r from-blue-600 to-cyan-500 text-white px-5 py-3 rounded-2xl rounded-br-md shadow-lg">
      {msg.user}
    </div>

  </div>

</div>

            <div className="mt-3 bg-white border border-gray-200 rounded-3xl p-6 shadow-xl">

             <div className="flex items-center gap-3 mb-5">

  <div className="w-12 h-12 rounded-full bg-blue-100 flex items-center justify-center text-2xl">
    🤖
  </div>

  <div>

    <h3 className="text-xl font-bold text-blue-700">
      AI Doctor
    </h3>

    <p className="text-sm text-gray-500">
      Healthcare Assistant
    </p>

  </div>

</div>
             <div className="bg-red-50 border-l-4 border-red-500 rounded-xl p-4 mt-3 shadow-sm">
  <h3 className="text-red-700 font-bold text-lg">
    🩺 Disease Prediction
  </h3>

  <p className="mt-2 text-gray-700">
    {msg.response.prediction}
  </p>
</div>
             <div className="bg-blue-50 border-l-4 border-blue-500 rounded-xl p-4 mt-3 shadow-sm">
  <h3 className="text-blue-700 font-bold">
    👨‍⚕ Recommended Specialist
  </h3>

  <p className="mt-2">
    {msg.response.specialist}
  </p>
</div>

             <div className="bg-yellow-50 border-l-4 border-yellow-500 rounded-xl p-4 mt-3 shadow-sm">
  <h3 className="text-yellow-700 font-bold">
    📊 Severity
  </h3>

  <p className="mt-2 font-semibold">
    {msg.response.severity}
  </p>
</div>
              <p className="mt-2">
                <strong>📋 Description:</strong>
              </p>

              <p>{msg.response.description}</p>

              <button
                onClick={() => downloadReport(msg)}
                className="mt-4 bg-indigo-600 text-white px-4 py-2 rounded-lg"
              >
                📄 Download Medical Report
              </button>
                 <div className="mt-4 bg-green-50 border border-green-300 rounded-2xl p-5 shadow-md">

  <h3 className="text-xl font-bold text-green-700 mb-3">
    💊 Recommended Medicines
  </h3>

  <ul className="list-disc ml-6 space-y-2">
    {msg.response.medicine?.map((item, i) => (
      <li key={i}>{item}</li>
    ))}
  </ul>

</div>           

                <div className="mt-5 bg-green-50 border border-green-300 rounded-2xl p-5 shadow-md hover:shadow-lg transition duration-300">

  <h3 className="text-xl font-bold text-green-700 mb-3">
    💊 Recommended Medicines
  </h3>


</div>

             
                <ul className="list-disc ml-6 mt-2">
                  {msg.response.medicine?.map((item, i) => (
                    <li key={i}>{item}</li>
                  ))}
                </ul>
              </div>

              <div className="mt-4 bg-orange-50 border border-orange-200 rounded-lg p-3">
                <h3 className="font-bold text-orange-700">
                  🥗 Diet Recommendation
                </h3>

                <ul className="list-disc ml-6 mt-2">
                  {msg.response.diet?.map((item, i) => (
                    <li key={i}>{item}</li>
                  ))}
                </ul>
              </div>

              <div className="mt-4 bg-yellow-50 border border-yellow-300 rounded-lg p-3">
                <h3 className="font-bold text-yellow-700">
                  🛡️ Precautions
                </h3>

                <ul className="list-disc ml-6 mt-2">
                  {msg.response.precaution?.map((item, i) => (
                    <li key={i}>{item}</li>
                  ))}
                </ul>
              </div>

              {msg.response.hospital &&
                msg.response.hospital.length > 0 && (
                  <div className="mt-4">

                    <h3 className="font-bold text-green-700 text-lg">
                      🏥 Recommended Hospitals
                    </h3>

                    {msg.response.hospital.map((hospital, i) => (
                     <div
  key={i}
  className="mt-4 bg-white border border-green-200 rounded-2xl p-5 shadow-md hover:shadow-xl transition duration-300"
>
                      
                        <h3 className="text-xl font-bold text-green-700">
  🏥 {hospital.hospital_name}
</h3>
                        <p className="mt-3 text-gray-700">
  📞 <strong>Contact:</strong> {hospital.contact_number}
</p>
                          <p className="mt-2 text-gray-700">
  📍 <strong>Address:</strong> {hospital.address}
</p>                 <a
                          
  href={hospital.google_maps}
  target="_blank"
  rel="noreferrer"
  className="inline-block mt-4 bg-blue-600 hover:bg-blue-700 text-white px-5 py-2 rounded-xl shadow transition duration-300"
>
  🗺️ Open in Google Maps
</a>
                      </div>
                    ))}

                  </div>
              )}

            </div>

          </div>

        ))

      )}

    </div>
          {showHistory && history.length > 0 && (
        <div className="mb-4 border-t pt-3">

          <h3 className="text-lg font-bold text-green-700 mb-2">
            📜 Chat History
          </h3>

          {history.map((item, index) => (
            <div
              key={index}
              className="bg-gray-100 rounded-lg p-3 mb-2 border"
            >
              <p><strong>🕒 Time:</strong> {item.time}</p>
              <p><strong>💬 Symptoms:</strong> {item.symptoms}</p>
              <p><strong>🩺 Prediction:</strong> {item.prediction}</p>
            </div>
          ))}

        </div>
      )}

      <div className="flex flex-wrap gap-2 mb-3">

        <button
          onClick={() => setSymptom("fever")}
          className="bg-gray-200 hover:bg-gray-300 px-3 py-1 rounded"
        >
          🤒 Fever
        </button>

        <button
          onClick={() => setSymptom("stomach pain")}
          className="bg-gray-200 hover:bg-gray-300 px-3 py-1 rounded"
        >
          🤢 Stomach Pain
        </button>

        <button
          onClick={() => setSymptom("cough")}
          className="bg-gray-200 hover:bg-gray-300 px-3 py-1 rounded"
        >
          🤧 Cough
        </button>

        <button
          onClick={() => setSymptom("burning urination")}
          className="bg-gray-200 hover:bg-gray-300 px-3 py-1 rounded"
        >
          🚽 Burning Urination
        </button>

      </div>

      <div className="flex flex-col md:flex-row gap-4 mt-6">

  <input
    type="text"
    placeholder="🔍 Enter symptoms (e.g. fever, cough, headache)"
    value={symptom}
    onChange={(e) => setSymptom(e.target.value)}
    onKeyDown={(e) => {
      if (e.key === "Enter") {
        handlePredict();
      }
    }}
    className="flex-1 border-2 border-blue-200 rounded-2xl px-5 py-4 text-lg focus:outline-none focus:ring-4 focus:ring-blue-100 focus:border-blue-500 shadow-sm"
  />

  <button
    onClick={() => {
      resetTranscript();

      SpeechRecognition.startListening({
        continuous: false,
        language: "en-US",
      });

      setTimeout(() => {
        SpeechRecognition.stopListening();
      }, 5000);
    }}
    className={`px-6 py-4 rounded-2xl font-semibold text-white shadow-lg transition-all duration-300 ${
      listening
        ? "bg-red-600 hover:bg-red-700"
        : "bg-green-600 hover:bg-green-700"
    }`}
  >
    {listening ? "🎙 Listening..." : "🎤 Speak"}
  </button>

  <button
    onClick={handlePredict}
    disabled={loading}
    className={`px-8 py-4 rounded-2xl font-bold text-white shadow-lg transition-all duration-300 ${
      loading
        ? "bg-gray-400 cursor-not-allowed"
        : "bg-blue-600 hover:bg-blue-700"
    }`}
  >
    {loading ? "⏳ Analyzing..." : "🔍 Predict"}
  </button>

</div>
     <footer className="mt-8 border-t pt-4 text-center">

  <h3 className="text-lg font-bold text-blue-700">
    🩺 AI Healthcare Assistant
  </h3>

  <p className="text-gray-600 mt-2">
    Developed by <strong>Chandana</strong>
  </p>

  <p className="text-gray-500 text-sm">
    Final Year Project • Computer Science Engineering • 2026
  </p>

</footer> 

    </div>

  

);

}

export default Chatbot;