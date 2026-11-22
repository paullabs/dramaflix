"use client";

import { existeDrama } from "@/data/catalogo";
import { useMinhaLista } from "@/lib/estado";
import { Botao } from "./Botao";
import { IconBookmark, IconFeed, IconHome, IconPlus } from "./icons";
import { PosterGrid } from "./PosterGrid";
import styles from "./Vazio.module.css";

export function MinhaLista() {
  const { ids } = useMinhaLista();
  const validos = ids.filter(existeDrama);

  return (
    <div className="page">
      <div className="page-head">
        <h1 className="page-title">
          <IconBookmark />
          Minha lista
          {validos.length > 0 && (
            <span className={styles.contagem} aria-label={`${validos.length} salvos`}>
              {validos.length}
            </span>
          )}
        </h1>
      </div>

      {validos.length > 0 ? (
        <PosterGrid ids={validos} />
      ) : (
        <div className={styles.vazio}>
          <span className={styles.icone} aria-hidden="true">
            <IconBookmark size={32} />
          </span>
          <h2>Lista vazia</h2>
          <p className={styles.dica}>
            Toque no
            <span className={styles.tecla} aria-label="botão mais">
              <IconPlus size={14} />
            </span>
            para salvar
          </p>
          <div className={styles.botoes}>
            <Botao href="/" variante="claro" icone={<IconHome size={20} />}>
              Início
            </Botao>
            <Botao href="/para-voce" variante="neutro" icone={<IconFeed size={20} />}>
              Para você
            </Botao>
          </div>
        </div>
      )}
    </div>
  );
}
