import { useState } from "react";

import DashboardLayout from "@/components/layout/DashboardLayout";

import {
  uploadMultipleImages,
} from "@/services/image.service";

import {
  UploadCloud,
  FolderOpen,
  File as FileIcon,
  CheckCircle,
  Loader2,
} from "lucide-react";

export default function Upload() {

  const [files, setFiles] =
    useState<File[]>([]);

  const [uploading, setUploading] =
    useState(false);

  const [progress, setProgress] =
    useState(0);

  const addFiles = (
    selectedFiles: FileList | null
  ) => {

    if (!selectedFiles) {
      return;
    }

    setFiles((prev) => [

      ...prev,

      ...Array.from(
        selectedFiles
      ),
    ]);
  };

  const removeFile = (
    index: number
  ) => {

    setFiles(

      files.filter(
        (_, i) =>
          i !== index
      )
    );
  };

  const handleDrop = (
    e: React.DragEvent
  ) => {

    e.preventDefault();

    addFiles(
      e.dataTransfer.files
    );
  };

  const handleUpload =
    async () => {

      if (
        files.length === 0
      ) {
        return;
      }

      try {

        setUploading(
          true
        );

        setProgress(0);

        await uploadMultipleImages(

          files,

          (
            percent
          ) => {

            setProgress(
              percent
            );
          }
        );

        setFiles([]);

      } catch (error) {

        console.error(
          error
        );

      } finally {

        setUploading(
          false
        );
      }
    };

  return (

    <DashboardLayout>

      <h1 className="text-4xl font-bold mb-8">

        Upload Files

      </h1>

      <div className="bg-white rounded-3xl shadow-xl p-8">

        <div

          onDragOver={(
            e
          ) =>
            e.preventDefault()
          }

          onDrop={
            handleDrop
          }

          className="border-2 border-dashed border-blue-300 rounded-2xl p-10 text-center transition hover:border-blue-500"

        >

          <UploadCloud
            className="mx-auto text-blue-600"
            size={60}
          />

          <h2 className="text-2xl font-bold mt-4">

            Drag & Drop Files

          </h2>

          <p className="text-gray-500 mt-2">

            Upload images, CSV, PDFs, videos,
            ZIPs and more

          </p>

          <div className="flex gap-4 justify-center mt-8">

            <label className="bg-blue-600 text-white px-6 py-3 rounded-xl cursor-pointer hover:bg-blue-700">

              Browse Files

              <input
                type="file"
                multiple
                className="hidden"
                onChange={(e) =>
                  addFiles(
                    e.target.files
                  )
                }
              />

            </label>

            <label className="bg-gray-200 px-6 py-3 rounded-xl cursor-pointer hover:bg-gray-300 flex items-center gap-2">

              <FolderOpen
                size={18}
              />

              Folder

              <input
                type="file"
                multiple
                // @ts-ignore
                webkitdirectory=""
                className="hidden"
                onChange={(e) =>
                  addFiles(
                    e.target.files
                  )
                }
              />

            </label>

          </div>

        </div>

        {files.length > 0 && (

          <div className="mt-10">

            <h3 className="text-2xl font-semibold mb-4">

              Upload Queue

            </h3>

            <div className="space-y-3">

              {files.map(
                (
                  file,
                  index
                ) => (

                  <div

                    key={index}

                    className="border rounded-xl p-4 flex justify-between items-center"

                  >

                    <div className="flex items-center gap-3">

                      <FileIcon
                        size={20}
                      />

                      <div>

                        <p className="font-medium">

                          {file.name}

                        </p>

                        <p className="text-sm text-gray-500">

                          {(
                            file.size /
                            1024
                          ).toFixed(
                            2
                          )}{" "}
                          KB

                        </p>

                      </div>

                    </div>

                    {!uploading && (

                      <button

                        onClick={() =>
                          removeFile(
                            index
                          )
                        }

                        className="text-red-500"

                      >

                        Remove

                      </button>

                    )}

                  </div>
                )
              )}

            </div>

          </div>
        )}

        {uploading && (

          <div className="mt-8">

            <div className="flex justify-between mb-2">

              <span>

                Uploading...

              </span>

              <span>

                {progress}%

              </span>

            </div>

            <div className="w-full bg-gray-200 rounded-full h-4">

              <div

                className="bg-blue-600 h-4 rounded-full transition-all"

                style={{
                  width: `${progress}%`,
                }}

              />

            </div>

          </div>
        )}

        <button

          onClick={
            handleUpload
          }

          disabled={
            uploading ||
            files.length === 0
          }

          className="mt-10 w-full bg-blue-600 text-white py-4 rounded-2xl text-lg font-semibold disabled:opacity-50 flex justify-center items-center gap-3"

        >

          {uploading ? (

            <>

              <Loader2
                className="animate-spin"
                size={22}
              />

              Uploading...

            </>

          ) : (

            <>

              <CheckCircle
                size={22}
              />

              Upload {files.length} Files

            </>

          )}

        </button>

      </div>

    </DashboardLayout>
  );
}
