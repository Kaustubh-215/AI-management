import { Link } from "react-router-dom";

interface EmptyStateProps {
  title?: string;
  description?: string;
  buttonText?: string;
  buttonLink?: string;
}

export default function EmptyState({
  title = "No Images Yet",
  description = "Upload your first image to start building your gallery.",
  buttonText = "Upload Image",
  buttonLink = "/upload",
}: EmptyStateProps) {
  return (
    <div className="flex flex-col items-center justify-center py-20">

      <div className="text-7xl mb-6">
        📷
      </div>

      <h2 className="text-3xl font-bold mb-3">
        {title}
      </h2>

      <p className="text-gray-500 mb-8 text-center max-w-md">
        {description}
      </p>

      <Link
        to={buttonLink}
        className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-lg transition"
      >
        {buttonText}
      </Link>

    </div>
  );
}
