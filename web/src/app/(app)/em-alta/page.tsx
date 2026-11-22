import type { Metadata } from "next";
import { Ranking } from "@/components/Ranking";
import { MARCA } from "@/lib/marca";

export const metadata: Metadata = { title: `Em alta — ${MARCA.nome}` };

export default function EmAltaPage() {
  return <Ranking />;
}
