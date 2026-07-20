import {
  Download,
  Trash2,
  Loader2,
} from "lucide-react";

import { useState } from "react";

import {
  deleteImage,
  getDownloadUrl,
} from "@/services/image.service";

interface ImageCardProps {

  image: any;

  onDelete: () => void;

  showCheckbox?: boolean;

  checked?: boolean;

  onSelect?: (
    checked: boolean
  ) => void;
}

export default function ImageCard({

  image,

  onDelete,

  showCheckbox = false,

  checked = false,

  onSelect,

}: ImageCardProps) {

  const [deleting, setDeleting] =
    useState(false);

  const getFileIcon = (
    image: any
  ): string => {

    const category =
      image.file_category?.toLowerCase();

    const mime =
      image.mime_type?.toLowerCase();

    if (
      mime?.startsWith("image/")
    ) {

      return "/icons/image.png";
    }

    const iconMap: Record<
      string,
      string
    > = {

      jpg: "/icons/image.png",
      jpeg: "/icons/image.png",
      png: "/icons/image.png",
      webp: "/icons/image.png",

      csv: "/icons/csv.png",
      tsv: "/icons/csv.png",
      xls: "/icons/csv.png",
      xlsx: "/icons/csv.png",

      pdf: "/icons/pdf.png",

      doc: "/icons/doc.png",
      docx: "/icons/doc.png",

      txt: "/icons/text.png",

      zip: "/icons/zip.png",
      rar: "/icons/zip.png",

      video: "/icons/video.png",

      audio: "/icons/audio.png",
    };

    return (
      iconMap[category] ||
      "/icons/file.png"
    );
  };

  const handleDelete = async () => {

    const confirmed = window.confirm(

      `Delete "${image.original_filename}" ?`

    );

    if (!confirmed) {

      return;
    }

    try {

      setDeleting(true);

      await deleteImage(image.id);

      alert(
        "File deleted successfully"
      );

      onDelete();

    } catch (error: any) {

      console.error(
        "Delete error:",
        error
      );

      alert(

        error?.response?.data?.detail ||

        "Failed to delete file"

      );

    } finally {

      setDeleting(false);
    }
  };

  return (

    <div className="relative bg-white rounded-2xl shadow-md overflow-hidden hover:shadow-xl transition">

      {showCheckbox && (

        <input

          type="checkbox"

          checked={checked}

          onChange={(e) =>

            onSelect?.(
              e.target.checked
            )
          }

          className="
            absolute
            top-4
            left-4
            h-5
            w-5
            z-20
          "

        />

      )}

      <div className="h-72 bg-slate-100 flex items-center justify-center">

        {image.mime_type?.startsWith(
          "image/"
        ) ? (

          <img

            src={image.file_path}

            alt={
              image.original_filename
            }

            className="
              w-full
              h-full
              object-cover
            "

          />

        ) : (

          <img

            src={getFileIcon(
              image
            )}

            alt="preview"

            className="
              w-32
              h-32
              object-contain
            "

          />

        )}

      </div>

      <div className="p-6">

        <h3 className="text-xl font-bold break-words">

          {image.original_filename}

        </h3>

        <p className="text-gray-500 mt-2">

          {image.mime_type}

        </p>

        <div className="mt-3 flex gap-2 flex-wrap">

          <span className="px-3 py-1 rounded-full bg-blue-100 text-blue-700 text-sm">

            {image.file_category}

          </span>

          <span className="px-3 py-1 rounded-full bg-purple-100 text-purple-700 text-sm">

            {image.ai_status}

          </span>

        </div>

        {image.ai_summary && (

          <div className="mt-4">

            <h4 className="font-semibold">

              AI Summary

            </h4>

            <p className="text-gray-600 text-sm mt-1">

              {image.ai_summary}

            </p>

          </div>

        )}

        <div className="mt-6 flex gap-3">

          <a

            href={getDownloadUrl(
              image.id
            )}

            className="
              flex-1
              bg-green-600
              text-white
              py-3
              rounded-lg
              flex
              items-center
              justify-center
              gap-2
            "

          >

            <Download size={18} />

            Download

          </a>

          <button

            onClick={handleDelete}

            disabled={deleting}

            className="
              flex-1
              bg-red-600
              text-white
              py-3
              rounded-lg
              flex
              items-center
              justify-center
              gap-2
              disabled:opacity-60
            "

          >

            {deleting ? (

              <>

                <Loader2

                  size={18}

                  className="
                    animate-spin
                  "

                />

                Deleting...

              </>

            ) : (

              <>

                <Trash2 size={18} />

                Delete

              </>

            )}

          </button>

        </div>

      </div>

    </div>
  );
}
