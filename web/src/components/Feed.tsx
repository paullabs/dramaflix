"use client";

import Image from "next/image";
import { useCallback, useEffect, useRef, useState } from "react";
import { type Drama, getDrama, paraVoce, previaDe, rotuloSelo } from "@/data/catalogo";
import { alternarCurtida, useCarteira, useMinhaLista } from "@/lib/estado";
import { useProgresso } from "@/lib/historico";
import { cx } from "@/lib/marca";
import { rotaAssistir } from "@/lib/rotas";
import { useApp } from "./AppProvider";
import { Botao, BotaoIcone } from "./Botao";
import { Meta } from "./Meta";
import { IconCheck, IconChevronDown, IconChevronUp, IconHeart, IconList, IconPlay, IconPlus, IconShare, IconVolume } from "./icons";
import { useNoNavegador, useReducedMotion } from "./useReducedMotion";
import styles from "./Feed.module.css";

/**
 * "Para você": feed vertical, um drama por tela (como o "Clips" do app da Netflix e os apps de drama curto).
 * Rola com o dedo, a roda do mouse ou as setas do teclado; a tela em foco toca a prévia sozinha
 * (muda até a pessoa ligar o som). Cada tela leva ao player ou à grade de episódios.
 */
export function Feed() {
  const itens = paraVoce.map(getDrama);
  const ref = useRef<HTMLDivElement>(null);
  const [atual, setAtual] = useState(0);
  const [som, setSom] = useState(false);

  const irPara = useCallback(
    (i: number) => {
      const el = ref.current;
      const alvo = Math.max(0, Math.min(itens.length - 1, i));
      el?.scrollTo({ top: alvo * el.clientHeight, behavior: "smooth" });
    },
    [itens.length],
  );

  useEffect(() => {
    const aoTeclar = (e: KeyboardEvent) => {
      if (e.target instanceof HTMLInputElement || document.querySelector('[role="dialog"]')) return;
      if (e.key === "ArrowDown" || e.key === "PageDown") {
        e.preventDefault();
        irPara(atual + 1);
      } else if (e.key === "ArrowUp" || e.key === "PageUp") {
        e.preventDefault();
        irPara(atual - 1);
      }
    };
    window.addEventListener("keydown", aoTeclar);
    return () => window.removeEventListener("keydown", aoTeclar);
  }, [atual, irPara]);

  return (
    <div className={styles.envoltorio}>
      <h1 className="visually-hidden">Para você</h1>
      <div
        ref={ref}
        className={styles.feed}
        onScroll={(e) => {
          const el = e.currentTarget;
          setAtual(Math.round(el.scrollTop / el.clientHeight));
        }}
      >
        {itens.map((d, i) => (
          <Tela key={d.id} drama={d} prioridade={i === 0} ativa={i === atual} som={som} alternarSom={() => setSom((x) => !x)} />
        ))}
      </div>

      <div className={styles.navegacao} aria-label="Navegar no feed">
        <BotaoIcone rotulo="Drama anterior" onClick={() => irPara(atual - 1)} disabled={atual === 0}>
          <IconChevronUp size={22} />
        </BotaoIcone>
        <span className={styles.contador}>
          {atual + 1} / {itens.length}
        </span>
        <BotaoIcone rotulo="Próximo drama" onClick={() => irPara(atual + 1)} disabled={atual === itens.length - 1}>
          <IconChevronDown size={22} />
        </BotaoIcone>
      </div>
    </div>
  );
}

function Tela({ drama: d, prioridade, ativa, som, alternarSom }: { drama: Drama; prioridade: boolean; ativa: boolean; som: boolean; alternarSom: () => void }) {
  const { abrirModal, alternarLista, mostrarToast } = useApp();
  const { ids } = useMinhaLista();
  const { curtidas } = useCarteira();
  const naLista = ids.includes(d.id);
  const curtiu = curtidas.includes(d.id);
  const ep = useProgresso(d.id)?.episodio ?? 1;
  const previa = previaDe(d.id);
  const noNavegador = useNoNavegador();
  const reduz = useReducedMotion();
  const videoRef = useRef<HTMLVideoElement>(null);
  const [pausado, setPausado] = useState(false);
  const [andamento, setAndamento] = useState(0);
  const tocarPrevia = ativa && noNavegador && Boolean(previa);

  // a prévia só toca na tela em foco; com "reduzir movimento", começa parada
  useEffect(() => {
    const v = videoRef.current;
    if (!v) return;
    v.muted = !som;
    if (reduz) return;
    v.play().catch(() => {
      v.muted = true;
      void v.play().catch(() => {});
    });
  }, [tocarPrevia, reduz, som]);

  const alternarPrevia = () => {
    const v = videoRef.current;
    if (!v) return;
    if (v.paused) void v.play().catch(() => {});
    else v.pause();
  };

  const compartilhar = async () => {
    const url = `${window.location.origin}${rotaAssistir(d.id, 1)}`;
    try {
      await navigator.clipboard.writeText(url);
      mostrarToast("Link copiado", "link");
    } catch {
      mostrarToast(url, "link");
    }
  };

  return (
    <article className={cx(styles.tela, ativa && styles.ativa)} aria-label={d.titulo}>
      <div className={styles.cartao}>
        <div className={styles.midia} style={{ backgroundColor: d.cor }}>
          <Image src={d.foto} alt="" fill sizes="(min-width: 960px) 520px, 92vw" preload={prioridade} className={styles.foto} />
          {tocarPrevia && (
            <video
              ref={videoRef}
              className={styles.video}
              src={previa ?? undefined}
              poster={d.foto}
              muted
              loop
              playsInline
              preload="auto"
              aria-hidden="true"
              onPlay={() => setPausado(false)}
              onPause={() => setPausado(true)}
              onTimeUpdate={(e) => setAndamento(e.currentTarget.duration ? e.currentTarget.currentTime / e.currentTarget.duration : 0)}
            />
          )}
          <span className={styles.veu} aria-hidden="true" />
          {d.selo && <span className={cx(styles.selo, styles[d.selo])}>{rotuloSelo[d.selo]}</span>}
          <span className={styles.logo}>
            <Image src={d.logo.src} alt={d.titulo} width={d.logo.w} height={d.logo.h} sizes="(min-width: 960px) 420px, 76vw" />
          </span>

          {/* toque na imagem: pausa/continua a prévia */}
          <button className={styles.alvo} onClick={alternarPrevia} disabled={!tocarPrevia} aria-label={pausado ? `Tocar a prévia de ${d.titulo}` : `Pausar a prévia de ${d.titulo}`}>
            {tocarPrevia && pausado && (
              <span className={styles.play} aria-hidden="true">
                <IconPlay size={32} />
              </span>
            )}
          </button>
          {tocarPrevia && (
            <>
              <button className={styles.som} onClick={alternarSom} aria-label={som ? "Tirar o som" : "Ligar o som"} aria-pressed={som}>
                <IconVolume size={20} mudo={!som} />
              </button>
              <span className={styles.andamento} aria-hidden="true">
                <span style={{ transform: `scaleX(${andamento})` }} />
              </span>
            </>
          )}
        </div>

        <div className={styles.texto}>
          <Meta drama={d} />
          <p className={styles.sinopse}>{d.gancho}</p>
          <div className={styles.acoes}>
            <Botao href={rotaAssistir(d.id, ep)} variante="claro" tamanho="m" icone={<IconPlay size={20} />} className={styles.assistir}>
              <span className={styles.rotuloLongo}>{ep > 1 ? `Continuar ep. ${ep}` : "Assistir"}</span>
              <span className={styles.rotuloCurto}>{ep > 1 ? `Ep. ${ep}` : "Assistir"}</span>
            </Botao>
            <BotaoIcone
              rotulo={curtiu ? "Descurtir" : "Curtir"}
              ativo={curtiu}
              onClick={() => alternarCurtida(d.id) && mostrarToast("Curtido", "curtida")}
            >
              <IconHeart size={20} cheio={curtiu} />
            </BotaoIcone>
            <BotaoIcone rotulo={naLista ? "Tirar da Minha lista" : "Salvar na Minha lista"} ativo={naLista} onClick={() => alternarLista(d.id)}>
              {naLista ? <IconCheck size={20} /> : <IconPlus size={20} />}
            </BotaoIcone>
            <BotaoIcone rotulo="Episódios" onClick={() => abrirModal(d.id)}>
              <IconList size={19} />
            </BotaoIcone>
            <BotaoIcone rotulo="Compartilhar" onClick={compartilhar}>
              <IconShare size={19} />
            </BotaoIcone>
          </div>
        </div>
      </div>
    </article>
  );
}
