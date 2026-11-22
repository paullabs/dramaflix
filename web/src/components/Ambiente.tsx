"use client";

import { useState } from "react";
import { getDrama } from "@/data/catalogo";
import { useApp } from "./AppProvider";
import styles from "./Ambiente.module.css";

/**
 * Fundo ambiente: a capa do título em foco, borrada e quase transparente, atrás da página.
 * É o mesmo recurso medido nas páginas públicas da Netflix (blur + opacidade baixa) e o
 * "fundo que acompanha o título em foco" do refresh da web de 2026.
 */
export function Ambiente() {
  const { ambienteId } = useApp();
  const [camadas, setCamadas] = useState<string[]>([ambienteId]);

  // guarda a camada anterior para fazer a troca suave (estado derivado durante a renderização)
  if (camadas[camadas.length - 1] !== ambienteId) {
    setCamadas([...camadas.slice(-1), ambienteId]);
  }

  return (
    <div className={styles.ambiente} aria-hidden="true">
      {camadas.map((id, i) => (
        // eslint-disable-next-line @next/next/no-img-element -- imagem decorativa borrada; o otimizador não ajuda aqui
        <img key={`${id}-${i}`} src={getDrama(id).capa} alt="" className={i === camadas.length - 1 ? styles.atual : styles.anterior} />
      ))}
    </div>
  );
}
