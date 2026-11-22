"use client";

import { useState } from "react";
import type { Drama } from "@/data/catalogo";
import { cx } from "@/lib/marca";
import { IconCheck, IconClock, IconLock, IconPlay } from "./icons";
import styles from "./EpisodeGrid.module.css";

export type EstadoEpisodio = "visto" | "atual" | "livre" | "bloqueado" | "emBreve";

const POR_FAIXA = 30;

const rotuloEstado: Record<EstadoEpisodio, string> = {
  livre: "",
  atual: ", parou aqui",
  visto: ", assistido",
  bloqueado: ", bloqueado",
  emBreve: ", em breve",
};

interface Props {
  drama: Drama;
  estadoDe: (n: number) => EstadoEpisodio;
  selecionado?: number | null;
  onEscolher: (n: number) => void;
  /** episódio que define a faixa aberta no início */
  foco?: number;
  compacto?: boolean;
}

/**
 * Grade numérica de episódios (1…N), em faixas de 30.
 * Cada quadrado se explica sozinho: cadeado = bloqueado, ✓ = já visto, ▶ = onde parou, relógio = ainda não saiu.
 */
export function EpisodeGrid({ drama: d, estadoDe, selecionado, onEscolher, foco = 1, compacto }: Props) {
  const faixas = Math.ceil(d.episodios / POR_FAIXA);
  const [faixa, setFaixa] = useState(Math.min(faixas - 1, Math.floor((foco - 1) / POR_FAIXA)));
  const inicio = faixa * POR_FAIXA + 1;
  const fim = Math.min(d.episodios, inicio + POR_FAIXA - 1);
  const numeros = Array.from({ length: fim - inicio + 1 }, (_, i) => inicio + i);

  return (
    <div className={cx(styles.bloco, compacto && styles.compacto)}>
      {faixas > 1 && (
        <div className={styles.faixas} role="tablist" aria-label="Faixa de episódios">
          {Array.from({ length: faixas }, (_, f) => {
            const a = f * POR_FAIXA + 1;
            const b = Math.min(d.episodios, a + POR_FAIXA - 1);
            return (
              <button key={f} role="tab" aria-selected={f === faixa} className={cx(styles.faixa, f === faixa && styles.faixaOn)} onClick={() => setFaixa(f)}>
                {a}–{b}
              </button>
            );
          })}
        </div>
      )}

      <ol className={styles.grade} key={faixa}>
        {numeros.map((n) => {
          const estado = estadoDe(n);
          return (
            <li key={n} style={{ "--n": n - inicio } as React.CSSProperties}>
              <button
                className={cx(styles.ep, styles[estado], selecionado === n && styles.sel)}
                onClick={() => onEscolher(n)}
                aria-label={`Episódio ${n}${rotuloEstado[estado]}`}
              >
                {n}
                {estado === "emBreve" && <IconClock size={13} className={styles.marca} />}
                {estado === "bloqueado" && <IconLock size={13} className={styles.marca} />}
                {estado === "visto" && <IconCheck size={12} className={styles.marca} />}
                {estado === "atual" && <IconPlay size={11} className={styles.marca} />}
              </button>
            </li>
          );
        })}
      </ol>

    </div>
  );
}
