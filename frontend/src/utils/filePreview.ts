export const getFilePreview = (
  file: File | null,
  mimeType?: string
) => {
  if (!file && !mimeType) {
    return "/icons/file.png";
  }

  const type = mimeType || file?.type || "";

  if (type.startsWith("image/")) {
    return file
      ? URL.createObjectURL(file)
      : "/icons/image.png";
  }

  if (type.includes("pdf")) {
    return "/icons/pdf.png";
  }

  if (
    type.includes("spreadsheet") ||
    type.includes("excel") ||
    type.includes("csv")
  ) {
    return "/icons/csv.png";
  }

  if (
    type.includes("word") ||
    type.includes("document")
  ) {
    return "/icons/doc.png";
  }

  if (
    type.includes("zip") ||
    type.includes("rar")
  ) {
    return "/icons/zip.png";
  }

  if (type.startsWith("video/")) {
    return "/icons/video.png";
  }

  if (type.startsWith("audio/")) {
    return "/icons/audio.png";
  }

  if (type.includes("text")) {
    return "/icons/text.png";
  }

  return "/icons/file.png";
};
