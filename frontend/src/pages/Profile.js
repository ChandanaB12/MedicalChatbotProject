function Profile() {

    const user = localStorage.getItem("user");

    return (

        <div className="min-h-screen bg-gray-100 p-8">

            <div className="bg-white rounded-xl shadow-lg p-8 max-w-xl mx-auto">

                <h1 className="text-3xl font-bold text-blue-700 mb-6">
                    👤 My Profile
                </h1>

                <p className="text-xl mb-4">
                    <strong>Name:</strong> {user}
                </p>

                <p className="text-xl mb-4">
                    <strong>Role:</strong> Patient
                </p>

                <p className="text-xl">
                    <strong>Status:</strong> Logged In ✅
                </p>

            </div>

        </div>

    );

}

export default Profile;