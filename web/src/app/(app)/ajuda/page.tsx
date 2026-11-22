import type { Metadata } from "next";
import { Faq } from "@/components/Faq";
import { IconHelp } from "@/components/icons";
import { MARCA } from "@/lib/marca";

export const metadata: Metadata = { title: `Ajuda — ${MARCA.nome}` };

export default function AjudaPage() {
  return (
    <div className="page">
      <div className="page-head">
        <h1 className="page-title">
          <IconHelp />
          Ajuda
        </h1>
      </div>
      <Faq />
    </div>
  );
}
