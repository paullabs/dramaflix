"use client";

import { useState } from "react";
import { cx } from "@/lib/marca";
import { IconPlus } from "./icons";
import styles from "./Faq.module.css";

const perguntas = [
  { p: "O que são dramas curtos?", r: "Novelas de episódios de 1 a 2 minutos." },
  { p: "Quantos episódios são grátis?", r: "Os 10 primeiros de cada drama." },
  { p: "Quanto custa um episódio?", r: "40 moedas. Fica liberado para sempre." },
  { p: "O que o VIP libera?", r: "Todos os episódios." },
  { p: "Meus dados ficam onde?", r: "Só neste aparelho. Em Perfil, Recomeçar apaga tudo." },
];

/** Perguntas frequentes no formato de acordeão (padrão medido na Netflix: fundo #2D2D2D, "+" que gira). */
export function Faq() {
  const [aberta, setAberta] = useState<number | null>(0);
  return (
    <ul className={styles.lista}>
      {perguntas.map((item, i) => {
        const on = aberta === i;
        return (
          <li key={item.p} className={styles.item}>
            <h3>
              <button className={styles.pergunta} aria-expanded={on} onClick={() => setAberta(on ? null : i)}>
                {item.p}
                <IconPlus size={26} className={cx(styles.icone, on && styles.iconeOn)} />
              </button>
            </h3>
            <div className={cx(styles.resposta, on && styles.respostaOn)} hidden={!on}>
              <p>{item.r}</p>
            </div>
          </li>
        );
      })}
    </ul>
  );
}
