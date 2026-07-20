import DashboardLayout from "@/components/layout/DashboardLayout";

export default function Dashboard() {
  return (
    <DashboardLayout>

      <div className="space-y-6">

        <div>

          <h1 className="text-4xl font-bold">
            Welcome 👋
          </h1>

          <p className="text-gray-600 mt-2">
            Manage your AI generated images from one place.
          </p>

        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

          <div className="bg-white rounded-xl shadow p-6">

            <h2 className="text-xl font-semibold">
              Upload Images
            </h2>

            <p className="mt-2 text-gray-500">
              Upload new AI images.
            </p>

          </div>

          <div className="bg-white rounded-xl shadow p-6">

            <h2 className="text-xl font-semibold">
              My Images
            </h2>

            <p className="mt-2 text-gray-500">
              Browse your uploaded images.
            </p>

          </div>

          <div className="bg-white rounded-xl shadow p-6">

            <h2 className="text-xl font-semibold">
              Profile
            </h2>

            <p className="mt-2 text-gray-500">
              Manage your account.
            </p>

          </div>

        </div>

      </div>

    </DashboardLayout>
  );
}
