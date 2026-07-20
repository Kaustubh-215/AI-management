import api from "@/api/client";

export interface Image {
  id: number;
  filename: string;
  original_filename: string;
  file_path: string;
  file_size: number;
  mime_type: string;
  width: number;
  height: number;
  image_format: string;
}

export async function uploadImage(file: File) {
  const formData = new FormData();

  formData.append("file", file);

  const response = await api.post(
    "/images/upload",
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
}

export async function getImages() {
  const response = await api.get("/images");
  return response.data;
}

export async function deleteImage(id: number) {
  const response = await api.delete(`/images/${id}`);
  return response.data;
}

export function downloadImage(id: number) {
  window.open(
    `${api.defaults.baseURL}/images/${id}/download`,
    "_blank"
  );
}
