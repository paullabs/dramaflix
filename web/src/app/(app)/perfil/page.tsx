import type { Metadata } from "next";
import { Perfil } from "@/components/Perfil";
import { MARCA } from "@/lib/marca";

export const metadata: Metadata = { title: `Perfil — ${MARCA.nome}` };

export default function PerfilPage() {
  return <Perfil />;
}
