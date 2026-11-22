import type { Metadata } from "next";
import { Feed } from "@/components/Feed";
import { MARCA } from "@/lib/marca";

export const metadata: Metadata = { title: `Para você — ${MARCA.nome}` };

export default function ParaVocePage() {
  return <Feed />;
}
