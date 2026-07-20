import { NavLink } from "react-router-dom";

export default function Sidebar() {
  return (
    <aside className="w-64 bg-slate-900 text-white min-h-screen">

      <div className="p-6 border-b border-slate-700">
        <h2 className="text-xl font-bold">
          Dashboard
        </h2>
      </div>

      <nav className="p-4 space-y-2">

        <NavLink
          to="/"
          className="block px-4 py-3 rounded-lg hover:bg-slate-700"
        >
          Dashboard
        </NavLink>

        <NavLink
          to="/upload"
          className="block px-4 py-3 rounded-lg hover:bg-slate-700"
        >
          Upload Image
        </NavLink>

        <NavLink
          to="/images"
          className="block px-4 py-3 rounded-lg hover:bg-slate-700"
        >
          My Images
        </NavLink>

        <NavLink
          to="/profile"
          className="block px-4 py-3 rounded-lg hover:bg-slate-700"
        >
          Profile
        </NavLink>

      </nav>

    </aside>
  );
}
