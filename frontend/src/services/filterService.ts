import api from "@/api/client";

export const getFilters = async () => {
  const response = await api.get("/images/filters");

  return response.data;
};
