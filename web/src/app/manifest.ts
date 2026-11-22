import type { MetadataRoute } from "next";
import { MARCA } from "@/lib/marca";

// Deixa instalar como app (tela inicial do celular, janela própria no computador).
export default function manifest(): MetadataRoute.Manifest {
  return {
    name: MARCA.nome,
    short_name: MARCA.nome,
    description: "Dramas curtos para maratonar.",
    start_url: "/",
    scope: "/",
    display: "standalone",
    orientation: "portrait",
    background_color: "#141414",
    theme_color: "#141414",
    lang: "pt-BR",
    categories: ["entertainment"],
    icons: [
      { src: "/icone-192.png", sizes: "192x192", type: "image/png" },
      { src: "/icone-512.png", sizes: "512x512", type: "image/png" },
      { src: "/icone-maskable-512.png", sizes: "512x512", type: "image/png", purpose: "maskable" },
    ],
    shortcuts: [
      { name: "Para você", url: "/para-voce" },
      { name: "Minha lista", url: "/minha-lista" },
    ],
  };
}
