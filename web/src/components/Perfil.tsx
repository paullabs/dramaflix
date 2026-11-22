"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useState } from "react";
import { fileiras } from "@/data/catalogo";
import { definirNome, recomecar, useCarteira, useMinhaLista, usePerfil } from "@/lib/estado";
import { cx } from "@/lib/marca";
import { useApp } from "./AppProvider";
import { IconBookmark, IconCheck, IconChevronRight, IconCoin, IconCrown, IconHelp, IconRepetir } from "./icons";
import { Row } from "./Row";
import styles from "./Perfil.module.css";

const continuar = fileiras.find((f) => f.tipo === "continuar");

export function Perfil() {
  const { saldo, vip, plano } = useCarteira();
  const { ids } = useMinhaLista();
  const { nome } = usePerfil();
  const [editando, setEditando] = useState(false);
  const [rascunho, setRascunho] = useState("");
  const [confirmar, setConfirmar] = useState(false);
  const router = useRouter();
  const { mostrarToast } = useApp();
  const mostrarCampo = editando || !nome;

  // uma palavra + um número; a figura diz o resto
  const itens = [
    { href: "/minha-lista", rotulo: "Minha lista", valor: String(ids.length), Icone: IconBookmark, cor: styles.rosa },
    { href: "/moedas", rotulo: "Moedas", valor: saldo.toLocaleString("pt-BR"), Icone: IconCoin, cor: styles.ouro },
    { href: "/moedas#vip", rotulo: "VIP", valor: vip && plano ? plano.charAt(0).toUpperCase() + plano.slice(1) : "", Icone: IconCrown, cor: styles.ouro },
    { href: "/ajuda", rotulo: "Ajuda", valor: "", Icone: IconHelp, cor: styles.verde },
  ];

  const salvar = (e: React.FormEvent) => {
    e.preventDefault();
    if (!rascunho.trim()) return;
    definirNome(rascunho);
    setEditando(false);
  };

  return (
    <div className="page">
      <h1 className="visually-hidden">Perfil</h1>
      <section className={styles.cabecalho}>
        <span className={styles.avatar} aria-hidden="true">
          {nome.charAt(0).toUpperCase()}
        </span>
        <div className={styles.dados}>
          {mostrarCampo ? (
            <form className={styles.form} onSubmit={salvar}>
              <input
                className={styles.campo}
                value={rascunho}
                onChange={(e) => setRascunho(e.target.value)}
                placeholder="Seu nome"
                aria-label="Seu nome"
                maxLength={24}
                autoComplete="given-name"
                enterKeyHint="done"
                autoFocus={editando}
              />
              <button className={styles.ok} type="submit" aria-label="Salvar nome" disabled={!rascunho.trim()}>
                <IconCheck size={20} />
              </button>
            </form>
          ) : (
            <button
              className={styles.nome}
              onClick={() => {
                setRascunho(nome);
                setEditando(true);
              }}
              aria-label={`${nome}, trocar nome`}
            >
              {nome}
            </button>
          )}
          <p className={cx(styles.status, vip && styles.vip)}>
            {vip && <IconCrown size={16} />}
            {vip ? "VIP" : "Grátis"}
          </p>
        </div>
      </section>

      {continuar && (
        <div className={styles.continuar}>
          <Row fileira={continuar} />
        </div>
      )}

      <ul className={styles.menu}>
        {itens.map(({ href, rotulo, valor, Icone, cor }) => (
          <li key={href}>
            <Link href={href} className={styles.item}>
              <span className={cx(styles.icone, cor)}>
                <Icone size={24} />
              </span>
              <strong className={styles.rotulo}>{rotulo}</strong>
              {valor && <span className={styles.valor}>{valor}</span>}
              <IconChevronRight size={18} className={styles.seta} />
            </Link>
          </li>
        ))}
        <li>
          <button
            className={cx(styles.item, confirmar && styles.perigo)}
            onClick={() => {
              if (!confirmar) return setConfirmar(true);
              recomecar();
              setConfirmar(false);
              setRascunho("");
              mostrarToast("Tudo apagado");
              router.push("/");
            }}
            onBlur={() => setConfirmar(false)}
          >
            <span className={cx(styles.icone, styles.cinza)}>
              <IconRepetir size={22} />
            </span>
            <strong className={styles.rotulo}>{confirmar ? "Apagar tudo?" : "Recomeçar"}</strong>
            {confirmar && <span className={styles.valor}>Tocar de novo</span>}
          </button>
        </li>
      </ul>
    </div>
  );
}
