"use client";

import { type TipoToast, useApp } from "./AppProvider";
import { IconBookmark, IconBookmarkCheck, IconClock, IconCoin, IconCrown, IconHeart, IconInfo, IconShare, IconUnlock } from "./icons";
import styles from "./Toast.module.css";

const icones: Record<TipoToast, React.ReactNode> = {
  lista: <IconBookmarkCheck size={20} className={styles.acento} />,
  listaFora: <IconBookmark size={20} className={styles.apagado} />,
  curtida: <IconHeart size={20} cheio className={styles.acento} />,
  moedas: <IconCoin size={20} className={styles.ouro} />,
  vip: <IconCrown size={20} className={styles.ouro} />,
  desbloqueio: <IconUnlock size={20} className={styles.verde} />,
  link: <IconShare size={18} className={styles.apagado} />,
  emBreve: <IconClock size={20} className={styles.apagado} />,
  info: <IconInfo size={20} className={styles.apagado} />,
};

export function Toast() {
  const { toast } = useApp();
  return (
    <div className={styles.area} aria-live="polite" role="status">
      {toast && (
        <p key={toast.id} className={styles.toast}>
          {icones[toast.tipo]}
          {toast.msg}
        </p>
      )}
    </div>
  );
}
