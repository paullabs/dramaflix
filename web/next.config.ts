import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // esconde o indicador "N" do modo de desenvolvimento (cobria a barra lateral e as abas)
  devIndicators: false,
  cacheComponents: true,
  partialPrefetching: true,
};

export default nextConfig;
