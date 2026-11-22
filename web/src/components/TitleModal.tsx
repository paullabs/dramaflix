"use client";

import Image from "next/image";
import { useRouter } from "next/navigation";
import { useEffect, useRef, useState } from "react";
import { createPortal } from "react-dom";
import { episodioSaiu, getDrama, rotuloSelo, semelhantes } from "@/data/catalogo";
import { desbloquear, temAcesso, useCarteira, useMinhaLista } from "@/lib/estado";
import { useProgresso } from "@/lib/historico";
import { cx } from "@/lib/marca";
import { rotaAssistir } from "@/lib/rotas";
import { useApp } from "./AppProvider";
import { Botao, BotaoIcone } from "./Botao";
import { EpisodeGrid, type EstadoEpisodio } from "./EpisodeGrid";
import { IconCheck, IconClose, IconCoin, IconCrown, IconEpisodios, IconGift, IconLock, IconPlay, IconPlus, IconThumb, IconUnlock } from "./icons";
import { Meta } from "./Meta";
import { useNoNavegador } from "./useReducedMotion";
import styles from "./TitleModal.module.css";

/** Modal de detalhes (o "jbv" da Netflix): banner 16:9 com logo, metadados, grade de episódios e semelhantes. */
export function TitleModal() {
  const { modal, fecharModal } = useApp();
  const montado = useNoNavegador();

  useEffect(() => {
    if (!modal) return;
    const anterior = document.activeElement as HTMLElement | null;
    const overflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    const aoTeclar = (e: KeyboardEvent) => {
      if (e.key === "Escape") fecharModal();
    };
    window.addEventListener("keydown", aoTeclar);
    return () => {
      document.body.style.overflow = overflow;
      window.removeEventListener("keydown", aoTeclar);
      anterior?.focus?.({ preventScroll: true });
    };
  }, [modal, fecharModal]);

  if (!montado || !modal) return null;

  return createPortal(
    <div
      className={styles.overlay}
      onMouseDown={(e) => {
        if (e.target === e.currentTarget) fecharModal();
      }}
    >
      <Conteudo key={modal.id} id={modal.id} />
    </div>,
    document.body,
  );
}

function Conteudo({ id }: { id: string }) {
  const { fecharModal, abrirModal, alternarLista, mostrarToast } = useApp();
  const router = useRouter();
  const carteira = useCarteira();
  const { ids: lista } = useMinhaLista();
  const d = getDrama(id);
  const prog = useProgresso(id);
  const epAtual = prog?.episodio ?? 1;
  const [selecionado, setSelecionado] = useState<number | null>(null);
  const [semSaldo, setSemSaldo] = useState(false);
  const [gostou, setGostou] = useState(false);
  const dialogRef = useRef<HTMLDivElement>(null);
  const naLista = lista.includes(d.id);

  useEffect(() => {
    dialogRef.current?.focus({ preventScroll: true });
  }, []);

  const estadoDe = (n: number): EstadoEpisodio => {
    if (!episodioSaiu(d.id, n)) return "emBreve";
    if (!temAcesso(carteira, d, n)) return "bloqueado";
    if (prog && n < epAtual) return "visto";
    if (prog && n === epAtual) return "atual";
    return "livre";
  };

  const assistir = (n: number) => {
    fecharModal();
    router.push(rotaAssistir(d.id, n));
  };

  const escolher = (n: number) => {
    setSemSaldo(false);
    const estado = estadoDe(n);
    if (estado === "emBreve") mostrarToast(`Ep. ${n} em breve`, "emBreve");
    else if (estado === "bloqueado") setSelecionado(n);
    else assistir(n);
  };

  const comprarEpisodio = (n: number) => {
    const r = desbloquear(d, n);
    if (r === "sem-saldo") {
      setSemSaldo(true);
      return;
    }
    mostrarToast(`Ep. ${n} liberado`, "desbloqueio");
    assistir(n);
  };

  return (
    <div ref={dialogRef} className={styles.dialog} role="dialog" aria-modal="true" aria-labelledby="modal-titulo" tabIndex={-1}>
      {/* ---------- banner ---------- */}
      <div className={styles.hero}>
        <Image src={d.banner} alt="" fill sizes="(min-width: 960px) 920px, 100vw" className={styles.heroImg} />
        <span className={styles.heroVeu} aria-hidden="true" />
        <button className={styles.fechar} onClick={fecharModal} aria-label="Fechar">
          <IconClose size={22} />
        </button>

        <div className={styles.heroConteudo}>
          <h2 id="modal-titulo" className={styles.titulo}>
            <Image src={d.logo.src} alt={d.titulo} width={d.logo.w} height={d.logo.h} sizes="(min-width: 720px) 380px, 70vw" className={styles.logo} />
          </h2>
          <div className={styles.heroAcoes}>
            <Botao href={rotaAssistir(d.id, epAtual)} onClick={fecharModal} variante="claro" tamanho="m" icone={<IconPlay size={20} />}>
              {prog ? `Continuar ep. ${epAtual}` : "Assistir"}
            </Botao>
            <BotaoIcone rotulo={naLista ? "Tirar da Minha lista" : "Salvar na Minha lista"} ativo={naLista} onClick={() => alternarLista(d.id)}>
              {naLista ? <IconCheck size={20} /> : <IconPlus size={20} />}
            </BotaoIcone>
            <BotaoIcone
              rotulo="Gostei"
              ativo={gostou}
              onClick={() => {
                setGostou((g) => !g);
                if (!gostou) mostrarToast("Gostei", "curtida");
              }}
            >
              <IconThumb size={19} />
            </BotaoIcone>
          </div>
        </div>
      </div>

      {/* ---------- informações: selos, uma linha de ícones e a sinopse ---------- */}
      <div className={styles.info}>
        {(d.emAlta <= 10 || d.selo) && (
          <div className={styles.selos}>
            {d.emAlta <= 10 && (
              <span className={styles.rank}>
                <span className={styles.top} aria-hidden="true">
                  <small>TOP</small>10
                </span>
                Nº {d.emAlta} hoje
              </span>
            )}
            {d.selo && <span className={cx(styles.selo, styles[d.selo])}>{rotuloSelo[d.selo]}</span>}
          </div>
        )}
        <Meta drama={d} duracao genero />
        <p className={styles.sinopse}>{d.sinopse}</p>
      </div>

      {/* ---------- episódios ---------- */}
      <section className={styles.secao} aria-labelledby="modal-episodios">
        <div className={styles.secaoCab}>
          <h3 id="modal-episodios">
            <IconEpisodios size={24} />
            Episódios
          </h3>
          {carteira.vip ? (
            <span className={cx(styles.etiqueta, styles.etiquetaOuro)}>
              <IconCrown size={18} />
              VIP: tudo liberado
            </span>
          ) : (
            <span className={styles.etiqueta}>
              <IconGift size={18} />
              1 a {d.gratisAte} grátis
            </span>
          )}
        </div>

        <EpisodeGrid drama={d} estadoDe={estadoDe} selecionado={selecionado} onEscolher={escolher} foco={epAtual} />

        {selecionado !== null && estadoDe(selecionado) === "bloqueado" && (
          <div className={styles.paywall} aria-live="polite">
            <p className={styles.paywallTexto}>
              <IconLock size={22} />
              <strong>Ep. {selecionado}</strong>
              <span className={styles.saldo} aria-label={`Seu saldo: ${carteira.saldo} moedas`}>
                <IconCoin size={18} />
                {carteira.saldo}
              </span>
            </p>
            <div className={styles.paywallBotoes}>
              {semSaldo ? (
                <Botao href="/moedas" onClick={fecharModal} variante="destaque" tamanho="m" icone={<IconCoin size={18} />}>
                  Comprar moedas
                </Botao>
              ) : (
                <Botao variante="destaque" tamanho="m" icone={<IconUnlock size={18} />} onClick={() => comprarEpisodio(selecionado)}>
                  Liberar por {d.moedasPorEpisodio}
                </Botao>
              )}
              <Botao href="/moedas#vip" onClick={fecharModal} variante="ouro" tamanho="m" icone={<IconCrown size={18} />}>
                VIP
              </Botao>
            </div>
            {semSaldo && <p className={styles.aviso}>Moedas insuficientes.</p>}
          </div>
        )}
      </section>

      {/* ---------- parecidos ---------- */}
      <section className={styles.secao} aria-labelledby="modal-semelhantes">
        <div className={styles.secaoCab}>
          <h3 id="modal-semelhantes">Parecidos</h3>
        </div>
        <ul className={styles.semelhantes}>
          {semelhantes(d.id, 6).map((s) => (
            <li key={s.id}>
              <button className={styles.semelhante} onClick={() => abrirModal(s.id)} aria-label={`Abrir ${s.titulo}`}>
                <span className={styles.semelhanteArte} style={{ backgroundColor: s.cor }}>
                  <Image src={s.capa} alt="" fill sizes="(min-width: 720px) 200px, 45vw" />
                  <span className={styles.semelhanteContador}>
                    <IconEpisodios size={15} />
                    {s.episodios} ep.
                  </span>
                </span>
                <span className={styles.semelhanteTitulo}>{s.titulo}</span>
              </button>
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}
