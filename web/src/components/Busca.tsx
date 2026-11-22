"use client";

import { useState } from "react";
import { atalhos, buscar, rankings } from "@/data/catalogo";
import { Chips } from "./Chips";
import { IconClose, IconFlame, IconSearch } from "./icons";
import { PosterGrid } from "./PosterGrid";
import styles from "./Busca.module.css";
import vazio from "./Vazio.module.css";

/** Busca por título, gênero, tema ou palavra da sinopse (sem acento, sem maiúscula). */
export function Busca() {
  const [termo, setTermo] = useState("");
  const resultados = buscar(termo);
  const temTermo = termo.trim().length > 0;

  return (
    <div className="page">
      <h1 className="visually-hidden">Buscar</h1>

      <label className={styles.campo}>
        <IconSearch size={24} />
        <span className="visually-hidden">Buscar dramas</span>
        <input type="search" value={termo} onChange={(e) => setTermo(e.target.value)} placeholder="Buscar drama" autoFocus enterKeyHint="search" />
        {temTermo && (
          <button className={styles.limpar} onClick={() => setTermo("")} aria-label="Limpar busca">
            <IconClose size={18} />
          </button>
        )}
      </label>

      <Chips itens={atalhos.slice(2)} className={styles.chips} />

      {temTermo ? (
        resultados.length > 0 ? (
          <>
            <p className={styles.resumo} aria-live="polite">
              <strong>{resultados.length}</strong> {resultados.length === 1 ? "drama" : "dramas"}
            </p>
            <PosterGrid ids={resultados.map((d) => d.id)} />
          </>
        ) : (
          <div className={vazio.vazio} aria-live="polite">
            <span className={vazio.icone} aria-hidden="true">
              <IconSearch size={30} />
            </span>
            <h2>Nada encontrado</h2>
            <p>Tente outra palavra.</p>
          </div>
        )
      ) : (
        <>
          <h2 className={styles.subtitulo}>
            <IconFlame size={24} />
            Mais vistos hoje
          </h2>
          <PosterGrid ids={rankings.hoje.slice(0, 12)} />
        </>
      )}
    </div>
  );
}
