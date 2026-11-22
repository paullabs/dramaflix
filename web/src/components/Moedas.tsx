"use client";

import { adicionarMoedas, definirVip, useCarteira } from "@/lib/estado";
import { cx } from "@/lib/marca";
import { useApp } from "./AppProvider";
import { Botao } from "./Botao";
import { IconCoin, IconCrown, IconGift, IconInfo, IconLock } from "./icons";
import styles from "./Moedas.module.css";

// Valores de EXEMPLO para o protótipo — preços reais ainda não definidos.
const pacotes = [
  { moedas: 100, bonus: 0, preco: "R$ 4,90" },
  { moedas: 300, bonus: 30, preco: "R$ 12,90", destaque: true },
  { moedas: 600, bonus: 90, preco: "R$ 24,90" },
  { moedas: 1500, bonus: 300, preco: "R$ 54,90" },
];

const planos = [
  { id: "semanal", nome: "Semanal", preco: "R$ 9,90", periodo: "/semana", extra: "", fundo: styles.plano1 },
  { id: "mensal", nome: "Mensal", preco: "R$ 29,90", periodo: "/mês", extra: "Estreias antes", fundo: styles.plano2, destaque: true },
  { id: "anual", nome: "Anual", preco: "R$ 199,90", periodo: "/ano", extra: "−44%", fundo: styles.plano3 },
];

const fmt = (n: number) => n.toLocaleString("pt-BR");

export function Moedas() {
  const { saldo, vip, plano } = useCarteira();
  const planoAtivo = planos.find((p) => p.id === plano);
  const { mostrarToast } = useApp();

  return (
    <div className="page">
      <div className="page-head">
        <h1 className="page-title">
          <IconCoin className={styles.moedaTitulo} />
          Moedas e VIP
        </h1>
        <p className={styles.simulacao} title="Nada é cobrado">
          <IconInfo size={18} />
          Simulação
        </p>
      </div>

      {/* saldo */}
      <section className={styles.carteira} aria-label="Seu saldo">
        <p className={styles.saldo}>
          <IconCoin size={40} />
          <span key={saldo} className={styles.numero}>
            {fmt(saldo)}
          </span>
          <span className={styles.unidade}>moedas</span>
        </p>
        <span className={cx(styles.status, vip && styles.statusVip)}>
          {vip ? <IconCrown size={20} /> : <IconLock size={18} />}
          {vip ? `VIP ${planoAtivo?.nome ?? ""}`.trim() : "Grátis"}
        </span>
      </section>

      {/* como funciona, em três figuras */}
      <ul className={styles.passos} aria-label="Como funciona">
        <li>
          <IconGift size={30} />
          <strong>10 ep.</strong>
          <span>grátis</span>
        </li>
        <li>
          <IconCoin size={30} />
          <strong>40</strong>
          <span>moedas por ep.</span>
        </li>
        <li>
          <IconCrown size={30} />
          <strong>VIP</strong>
          <span>libera tudo</span>
        </li>
      </ul>

      {/* pacotes */}
      <section className={styles.secao} aria-labelledby="pacotes">
        <h2 id="pacotes" className={styles.h2}>
          Moedas
        </h2>
        <ul className={styles.pacotes}>
          {pacotes.map((p) => (
            <li key={p.moedas} className={cx(styles.pacote, p.destaque && styles.pacoteDestaque)}>
              {p.destaque && <span className={styles.etiqueta}>Mais escolhido</span>}
              <p className={styles.qtd}>
                <IconCoin size={26} />
                {fmt(p.moedas)}
              </p>
              {p.bonus > 0 && <p className={styles.bonus}>+{fmt(p.bonus)} grátis</p>}
              <Botao
                variante={p.destaque ? "destaque" : "neutro"}
                tamanho="m"
                bloco
                className={styles.comprar}
                aria-label={`Adicionar ${fmt(p.moedas + p.bonus)} moedas por ${p.preco} (simulação)`}
                onClick={() => {
                  adicionarMoedas(p.moedas + p.bonus);
                  mostrarToast(`+${fmt(p.moedas + p.bonus)} moedas`, "moedas");
                }}
              >
                {p.preco}
              </Botao>
            </li>
          ))}
        </ul>
      </section>

      {/* VIP */}
      <section id="vip" className={styles.secao} aria-labelledby="titulo-vip">
        <h2 id="titulo-vip" className={styles.h2}>
          <IconCrown size={26} className={styles.coroa} />
          VIP
        </h2>
        <ul className={styles.planos}>
          {planos.map((p) => {
            const ativo = p.id === plano;
            return (
              <li key={p.id} className={cx(styles.plano, p.fundo, (ativo || (!vip && p.destaque)) && styles.planoDestaque)}>
                {ativo ? (
                  <span className={cx(styles.etiqueta, styles.etiquetaAtivo)}>Ativo</span>
                ) : (
                  !vip && p.destaque && <span className={styles.etiqueta}>Recomendado</span>
                )}
                <h3 className={styles.planoNome}>{p.nome}</h3>
                <p className={styles.planoPreco}>
                  {p.preco}
                  <span>{p.periodo}</span>
                </p>
                {p.extra && <p className={styles.planoExtra}>{p.extra}</p>}
                <Botao
                  variante={ativo ? "contorno" : "claro"}
                  tamanho="m"
                  bloco
                  aria-label={ativo ? "Cancelar VIP (simulação)" : `${vip ? "Trocar para" : "Assinar"} VIP ${p.nome} (simulação)`}
                  onClick={() => {
                    definirVip(ativo ? null : p.id);
                    mostrarToast(ativo ? "VIP cancelado" : `VIP ${p.nome} ativo`, "vip");
                  }}
                >
                  {ativo ? "Cancelar" : vip ? "Trocar" : "Assinar"}
                </Botao>
              </li>
            );
          })}
        </ul>
      </section>
    </div>
  );
}
