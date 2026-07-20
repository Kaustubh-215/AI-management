import api from "@/api/client";

export const getImages = async () => {

  const response =
    await api.get("/images");

  return response.data;
};

export const deleteImage = async (
  id: number
) => {

  return await api.delete(
    `/images/${id}`
  );
};

export const bulkDeleteImages =
  async (
    ids: number[]
  ) => {

    return await api.post(

      "/images/bulk-delete",

      {

        image_ids: ids,

      }

    );
  };

export const getDownloadUrl = (
  id: number
) => {

  return `${api.defaults.baseURL}/images/${id}/download`;
};

export const uploadImage = async (
  file: File
) => {

  const formData =
    new FormData();

  formData.append(
    "file",
    file
  );

  const response =
    await api.post(

      "/images/upload",

      formData,

      {

        headers: {

          "Content-Type":
            "multipart/form-data",

        },

      }

    );

  return response.data;
};

export const uploadMultipleImages =
  async (

    files: File[],

    onProgress?: (
      progress: number
    ) => void

  ) => {

    const formData =
      new FormData();

    files.forEach(

      (file) => {

        formData.append(
          "files",
          file
        );

      }

    );

    const response =
      await api.post(

        "/images/upload-multiple",

        formData,

        {

          headers: {

            "Content-Type":
              "multipart/form-data",

          },

          onUploadProgress: (
            progressEvent
          ) => {

            if (
              progressEvent.total
            ) {

              const progress =
                Math.round(

                  (
                    progressEvent.loaded /

                    progressEvent.total

                  ) * 100

                );

              onProgress?.(
                progress
              );
            }
          },

        }

      );

    return response.data;
  };
