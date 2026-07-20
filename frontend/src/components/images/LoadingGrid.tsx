export default function LoadingGrid() {
  return (
    <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">

      {Array.from({ length: 6 }).map((_, index) => (

        <div
          key={index}
          className="bg-white rounded-xl shadow-md overflow-hidden animate-pulse"
        >

          <div className="h-60 bg-gray-300"></div>

          <div className="p-5">

            <div className="h-5 bg-gray-300 rounded mb-4"></div>

            <div className="h-4 bg-gray-200 rounded mb-2"></div>

            <div className="h-4 bg-gray-200 rounded mb-2"></div>

            <div className="h-4 bg-gray-200 rounded"></div>

            <div className="flex gap-3 mt-6">

              <div className="h-10 flex-1 bg-gray-300 rounded"></div>

              <div className="h-10 flex-1 bg-gray-300 rounded"></div>

            </div>

          </div>

        </div>

      ))}

    </div>
  );
}
