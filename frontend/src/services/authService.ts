import api from "@/api/client";
import type {
  LoginRequest,
  RegisterRequest,
  TokenResponse,
} from "@/types/auth";

export const login = async (
  data: LoginRequest
): Promise<TokenResponse> => {
  const formData = new URLSearchParams();

  formData.append("username", data.username);
  formData.append("password", data.password);

  const response = await api.post(
    "/auth/login",
    formData,
    {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    }
  );

  return response.data;
};

export const register = async (
  data: RegisterRequest
) => {
  const response = await api.post("/auth/register", data);
  return response.data;
};

export const getCurrentUser = async () => {
  const response = await api.get("/users/me");
  return response.data;
};
