"use client";

import Image from "next/image";
import { useState } from "react";
import { getDrama, type Periodo, rankings } from "@/data/catalogo";
import { useMinhaLista } from "@/lib/estado";
import { cx } from "@/lib/marca";
import { rotaAssistir } from "@/lib/rotas";
import { useApp } from "./AppProvider";
import { Botao, BotaoIcone } from "./Botao";
import { IconCheck, IconFlame, IconPlay, IconPlus } from "./icons";
import { Meta } from "./Meta";
import styles from "./Ranking.module.css";

const periodos: { id: Periodo; rotulo: string }[] = [
  { id: "hoje", rotulo: "Hoje" },
  { id: "semana", rotulo: "Semana" },
  { id: "mes", rotulo: "Mês" },
];

/** Página "Em alta": ranking numerado por período. A capa abre os detalhes. */
export function Ranking() {
  const { abrirModal, alternarLista } = useApp();
  const { ids: lista } = useMinhaLista();
  const [periodo, setPeriodo] = useState<Periodo>("hoje");
  const itens = rankings[periodo].map(getDrama);
  const indice = periodos.findIndex((p) => p.id === periodo);

  return (
    <div className="page">
      <div className="page-head">
        <h1 className="page-title">
          <IconFlame />
          Em alta
        </h1>
        <div className={styles.abas} role="tablist" aria-label="Período">
          {/* pílula branca que desliza até a aba escolhida */}
          <span className={styles.pilula} style={{ "--i": indice } as React.CSSProperties} aria-hidden="true" />
          {periodos.map((p) => (
            <button key={p.id} role="tab" aria-selected={p.id === periodo} className={cx(styles.aba, p.id === periodo && styles.abaOn)} onClick={() => setPeriodo(p.id)}>
              {p.rotulo}
            </button>
          ))}
        </div>
      </div>

      <div className={styles.envoltorio}>
        <ol className={styles.lista} key={periodo}>
          {itens.map((d, i) => {
            const naLista = lista.includes(d.id);
            return (
              <li key={d.id} className={styles.item} style={{ "--i": i } as React.CSSProperties}>
                <span className={cx(styles.numero, i < 3 && styles.numeroTop)} aria-label={`${i + 1}º lugar`}>
                  {i + 1}
                </span>
                <button className={styles.capa} onClick={() => abrirModal(d.id)} aria-label={`Detalhes de ${d.titulo}`} style={{ backgroundColor: d.cor }}>
                  <Image src={d.capa} alt="" fill sizes="(min-width: 960px) 150px, 110px" />
                </button>
                <div className={styles.info}>
                  <h2 className={styles.titulo}>{d.titulo}</h2>
                  <Meta drama={d} tamanho="p" className={styles.meta} />
                  <div className={styles.acoes}>
                    <Botao href={rotaAssistir(d.id, 1)} variante="claro" tamanho="p" icone={<IconPlay size={16} />} className={styles.assistir}>
                      Assistir
                    </Botao>
                    <BotaoIcone tamanho="p" rotulo={naLista ? "Tirar da Minha lista" : "Salvar na Minha lista"} ativo={naLista} onClick={() => alternarLista(d.id)}>
                      {naLista ? <IconCheck size={17} /> : <IconPlus size={17} />}
                    </BotaoIcone>
                  </div>
                </div>
              </li>
            );
          })}
        </ol>
      </div>
    </div>
  );
}
