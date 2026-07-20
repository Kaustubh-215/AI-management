import { useNavigate } from "react-router-dom";

import { useAuth } from "@/context/AuthContext";

export default function Navbar() {
  const navigate = useNavigate();

  const { logout } = useAuth();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    <header className="h-16 bg-white border-b border-gray-200 flex items-center justify-between px-6 shadow-sm">

      <h1 className="text-xl font-bold text-blue-600">
        AI Image Management
      </h1>

      <button
        onClick={handleLogout}
        className="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-lg transition"
      >
        Logout
      </button>

    </header>
  );
}
